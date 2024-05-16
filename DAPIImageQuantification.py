from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi
import cv2
import numpy as np
import glob
import os
import ui_dapiquantification as dapi_ui
import sys
import tempfile
import shutil

class DAPIImageQuantification(QMainWindow, dapi_ui.Ui_DAPIQuantification):

    _progressBarSignal = pyqtSignal(int)
    _progressBarMaximum = pyqtSignal(int)
    _progressBarReset = pyqtSignal()

    def __init__(self):
        super(DAPIImageQuantification, self).__init__()
        self.window = loadUi('dapiquantification.ui', self)

        self.temporalPath = os.path.join(tempfile.gettempdir(), "DAPIImageQuantificationTemp")
        self.calculationResults = []
        self._progressBarSignal.connect(self.progressBarUpdate)
        self._progressBarMaximum.connect(self.progresBarMaximum)
        self._progressBarReset.connect(self.progressBarReset)
        self.progressBar.reset()

        if not os.path.exists(self.temporalPath):
            os.mkdir(self.temporalPath)
        elif not len(os.listdir(self.temporalPath)) == 0:
            fileList = glob.glob(os.path.join(self.temporalPath, "*"))
            for f in fileList:
                os.remove(f)

    def progressBarReset(self):
        self.progressBar.reset()

    def progresBarMaximum(self, msg):
        self.progressBar.setMaximum(int(msg))

    def progressBarUpdate(self, msg):
        self.progressBar.setValue(int(msg))

    def getImagesFromDirectory(self, rootPath):
        filetypes = ('*.jpg', '*.png', '*.tif')
        imageList = []
        for files in filetypes:
            imageList.extend(glob.glob(os.path.join(rootPath, files)))

        return imageList


    def exportClicked(self):
        if len(self.calculationResults) < 1:
            warning = QMessageBox()
            warning.setIcon(QMessageBox.Warning)
            warning.setInformativeText("No results to export!")
            warning.setDefaultButton(QMessageBox.Ok)
            warning.exec()
            return

        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)

        location = dialog.getExistingDirectory()
        filename = os.path.join(location, "percentages.txt")

        output = open(filename, "w")

        for result in self.calculationResults:
            name = os.path.basename(result[0])
            percentage = result[1]
            output.write(name + ": " + str(percentage) + "% \n")

            newImagePath = os.path.join(location, name)
            if os.path.isfile(newImagePath):
                os.remove(newImagePath)
            shutil.copyfile(result[0], newImagePath)

        output.close()


    def searchClicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        self.directoryLineEdit.setText(dialog.getExistingDirectory())


    def calculateClicked(self):
        currentPath = self.directoryLineEdit.text()
        if currentPath == "" or not os.path.isdir(currentPath):
            self.statusbar.showMessage("Invalid input folder!", 5000)
            return

        images = self.getImagesFromDirectory(currentPath)
        if len(images) < 1:
            self.statusbar.showMessage("No images found in directory", 5000)
            return

        self.resultsTableWidget.setRowCount(0)
        self.calculationResults.clear()

        if os.path.isdir(self.temporalPath) and not len(os.listdir(self.temporalPath)) == 0:
            fileList = glob.glob(os.path.join(self.temporalPath, "*"))
            for f in fileList:
                os.remove(f)

        self._progressBarReset.emit()
        self._progressBarMaximum.emit(len(images))

        for image in images:
            imgName = os.path.basename(image)
            result = self.processImage(imgName, image)

            self.resultsTableWidget.insertRow(self.resultsTableWidget.rowCount())

            imgCell = QTableWidgetItem(imgName)
            imgCell.setTextAlignment(Qt.AlignHCenter)
            self.resultsTableWidget.setItem(self.resultsTableWidget.rowCount()-1, 0 ,imgCell)

            percentageCell = QTableWidgetItem(str(result[1]) + " %")
            percentageCell.setTextAlignment(Qt.AlignHCenter)
            self.resultsTableWidget.setItem(self.resultsTableWidget.rowCount()-1, 1, percentageCell)

            self.calculationResults.append(result)
            self._progressBarSignal.emit(self.resultsTableWidget.rowCount()-1)
        
        #self.statusbar.messageChanged("Done!")
        self._progressBarSignal.emit(self.resultsTableWidget.rowCount())


    def processImage(self, imageName, imagePath):

        orig = cv2.imread(imagePath)
        img = cv2.bitwise_not(orig)
        #up_width = 600
        #up_height = 400
        #up_points = (up_width, up_height)
        #img = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #obtain the grayscale image of the original image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #set the bounds for the blue hue
        lower = np.array([0,30,30])
        upper = np.array([180,255,255])

        #create a mask using the bounds set
        mask = cv2.inRange(hsv, lower, upper)
        #create an inverse of the mask
        mask_inv = cv2.bitwise_not(mask)
        #Filter only the red colour from the original image using the mask(foreground)
        res = cv2.bitwise_and(img, img, mask=mask)
        #Filter the regions containing colours other than red from the grayscale image(background)
        background = cv2.bitwise_and(gray, gray, mask = mask_inv)

        #convert the one channelled grayscale background to a three channelled image
        background = np.stack((background,)*3, axis=-1)
        #add the foreground and the background
        added_img = cv2.add(res, background)

        whites = cv2.countNonZero(mask)
        grays = cv2.countNonZero(gray)
        percentage = whites * 100 / grays
        percentage = round(percentage, 3)

        #print("percentage: ",percentage)
        resultImage = os.path.join(self.temporalPath, imageName + "_result.png")
        cv2.imwrite(resultImage, res)

        return (resultImage, percentage)


    def selectionChanged(self, row, col):
        imgPath = self.calculationResults[row][0]
        image = QPixmap(imgPath)
        w = self.imageLabel.width()
        h = self.imageLabel.height()

        self.imageLabel.setPixmap(image.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        #img = cv2.imread(self.calculationResults[row][0])
        #up_points = (600, 400)
        #img = cv2.resize(img, up_points, interpolation=cv2.INTER_LINEAR)
        #cv2.imshow("image", img)

        #cv2.waitKey(0)


if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = DAPIImageQuantification()
    widget.show()
    sys.exit(app.exec_())

