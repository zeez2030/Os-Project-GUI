from PyQt5.QtWidgets import QCheckBox,QSpinBox,QRadioButton,QButtonGroup,QLabel,QMainWindow,QLineEdit,QWidget, QApplication,QPushButton,QDialog,QGroupBox,QHBoxLayout,QVBoxLayout,QGridLayout
import  sys
from PyQt5 import QtGui , QtCore
from PyQt5.QtCore import QRect
from operator import itemgetter



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "OS Project Group 10"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height =300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.hbox = QHBoxLayout()

        self.groupbox = QGroupBox("Type of scheduler")
        self.groupbox.setFont(QtGui.QFont("sanserif",15))
        self.hbox.addWidget(self.groupbox)

        self.vbox =QVBoxLayout()

        self.FCFS = QRadioButton("FCFS")
        self.vbox.addWidget(self.FCFS)

        self.SJF = QRadioButton("SJF")
        self.vbox.addWidget(self.SJF)

        self.RR = QRadioButton("RR")
        self.vbox.addWidget(self.RR)

        self.pri = QRadioButton("Priority")
        self.vbox.addWidget(self.pri)

        self.button = QPushButton("Next",self)
        self.button.clicked.connect(self.next)
        self.vbox.addWidget(self.button)


        self.groupbox.setLayout(self.vbox)


        self.i =0
        self.setLayout(self.hbox)
        self.show()

    def next(self):
        self.SJF.hide()
        self.FCFS.hide()
        self.RR.hide()
        self.pri.hide()
        self.pree = QCheckBox('Preemptive')
        self.nonpree=QCheckBox('Non-Preemptive')
        if self.SJF.isChecked():
            self.label = QLabel( "SJF")
            self.label.setFont(QtGui.QFont("sanserif", 20))
            self.vbox.addWidget(self.label)
            self.vbox.addWidget(self.pree)
            self.vbox.addWidget(self.nonpree)
        elif self.FCFS.isChecked():
            self.label = QLabel("FCFS")
            self.label.setFont(QtGui.QFont("sanserif", 20))
            self.vbox.addWidget(self.label)

        elif self.RR.isChecked():
            self.label = QLabel("RR")
            self.label.setFont(QtGui.QFont("sanserif", 20))
            self.vbox.addWidget(self.label)
        elif self.pri.isChecked():
            self.label = QLabel("Priority")
            self.label.setFont(QtGui.QFont("sanserif", 20))
            self.vbox.addWidget(self.label)
            self.vbox.addWidget(self.pree)
            self.vbox.addWidget(self.nonpree)
        if self.i == 0:
            self.button.hide()
            self.labelProcess = QLabel("Number of process")
            self.processBox = QSpinBox(self)
            self.vbox.addWidget(self.labelProcess)
            self.vbox.addWidget(self.processBox)
            self.button = QPushButton("Next", self)
            self.button.clicked.connect(self.nextPressed)
            self.vbox.addWidget(self.button)
        self.i = 5



    def nextPressed(self):
        self.processBox.hide()
        i=self.processBox.text()
        self.labelProcess.setText("Number of process = "+i)
        i=int(i,10)
        self.tList=list()
        self.lList=list()
        self.timeShots = list()
        self.timeInserted=list()
        self.pirority=list()
        for j in range(i):
            self.label = QLabel("P"+str(j+1))
            self.lList.append(self.label)
            self.label.setFont(QtGui.QFont("sanserif",15))
            self.vbox.addWidget(self.label)
            self.label = QLabel("Burst Time")
            self.timeShots.append(self.label)
            self.label.setFont(QtGui.QFont("sanserif",13))
            self.textbox = QSpinBox(self)
            self.tList.append(self.textbox)
            self.vbox.addWidget(self.label)
            self.vbox.addWidget(self.textbox)

            if (not self.SJF.isChecked()) and (not self.nonpree.isChecked()) and (not self.pri.isChecked())  :
                self.label = QLabel("Arrival Time:")
                self.timeShots.append(self.label)
                self.label.setFont(QtGui.QFont("sanserif", 13))
                self.vbox.addWidget(self.label)
                self.textbox = QSpinBox(self)
                self.timeInserted.append(self.textbox)
                self.vbox.addWidget(self.textbox)

            if self.pri.isChecked():
                self.label = QLabel("Priority (low number is higher in priority)")
                self.timeShots.append(self.label)
                self.label.setFont(QtGui.QFont("sanserif", 13))
                self.textbox = QSpinBox(self)
                self.pirority.append(self.textbox)
                self.vbox.addWidget(self.label)
                self.vbox.addWidget(self.textbox)
        if self.RR.isChecked() or (self.pri.isChecked() and self.pree.isChecked()):
            self.label = QLabel("Time Quantum:")
            self.label.setFont(QtGui.QFont("sanserif", 15))
            self.timeShots.append(self.label)
            self.vbox.addWidget(self.label)
            self.textbox = QSpinBox(self)
            self.tList.append(self.textbox)
            self.vbox.addWidget(self.textbox)
        self.button.hide()
        self.button = QPushButton("Draw", self)
        self.button.clicked.connect(self.Draw)
        self.vbox.addWidget(self.button)

    def Draw(self):
        self.button.hide()
        numberList=list()
        nameList=list()
        processList=list()
        inserted =list()
        pirority=list()
        for i in self.timeShots:
            i.hide()
        for i in self.lList:
            i.hide()
            nameList.append(i.text())
        for i in self.tList:
            i.hide()
            numberList.append(i.value())
        for i in self.timeInserted:
            i.hide()
            inserted.append(i.value())

        for i in self.pirority:
            i.hide()
            pirority.append(i.value())


        if self.SJF.isChecked() and self.nonpree.isChecked():
            for i in range(len(numberList)):
                process={'name':nameList[i] ,'Tburst':numberList[i]}
                processList.append(process)

            SortedProcess = sorted(processList,key=itemgetter('Tburst'),reverse=False)
            start = 0
            waiting=0
            for i in SortedProcess:
                self.pushB = QPushButton("" + i['name'], self)
                self.pushB.setFixedWidth(i['Tburst'] * 30)
                self.pushB.setToolTip("<h3>start from: "+str(start)+
                                      "<br> end: "+str(i['Tburst']+start)+"</h3>")
                waiting=waiting+(start)
                start=i['Tburst']+start
                self.hbox.addWidget(self.pushB)
            label = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
            self.vbox.addWidget(label)


        # elif self.SJF.isChecked() and self.pree.isChecked():
        #     for i in range(len(numberList)):
        #         process = {'name': nameList[i], 'Tburst': numberList[i],
        #                    'TimeInserted': inserted[i]}
        #         processList.append(process)
        #     SortedArrival = sorted(processList,key=itemgetter('TimeInserted'),reverse=False)
        #     SortedBurst = sorted(processList,key=itemgetter('Tburst'),reverse=False)
        #     sum =1
        #     start = SortedBurst[0]['TimeInserted']
        #     process = SortedBurst[0]
        #     flag= 0
        #     k=0
        #     min = 100
        #     while sum > 0 :
        #         for i in range(len(numberList)):
        #             if SortedBurst[i]['TimeInserted'] <= min  and SortedBurst[i]['Tburst'] > 0:
        #                 if flag != SortedBurst[i]['Tburst']:
        #                     process = SortedBurst[i]
        #                     min = process['TimeInserted']
        #                 else:
        #                     continue






        elif self.FCFS.isChecked():
            for i in range(len(numberList)):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted':inserted[i]}
                processList.append(process)
            SortedProcess = sorted(processList, key=itemgetter('TimeInserted'), reverse=False)
            i = 0
            waiting=0
            start = SortedProcess[0]['TimeInserted']
            for i in SortedProcess:
                self.pushB = QPushButton("" + i['name'], self)
                self.pushB.setFixedWidth(i['Tburst'] * 30)
                self.pushB.setToolTip("<h2>start from: " + str(start) +
                                      "<br> end: " + str(i['Tburst'] + start) + "</h2>")
                waiting=waiting+(start - i['TimeInserted'])
                start =i['Tburst'] + start
                self.hbox.addWidget(self.pushB)
            label = QLabel("Average waiting time : "+str(waiting/len(SortedProcess))+" ms")
            self.vbox.addWidget(label)


        elif self.RR.isChecked():
            timeSlice = numberList[-1]
            processList=list()
            sum=0
            for i in range(len(numberList)-1):
                 process={'name':nameList[i] ,'Tburst':numberList[i],
                          'TimeInserted':inserted[i] , 'waiting':0}
                 processList.append(process)
                 sum=sum+processList[i]['Tburst']
            SortedProcess = sorted(processList, key=itemgetter('TimeInserted'), reverse=False)

            start = SortedProcess[0]['TimeInserted']
            i=0
            while(sum>0):
                for i in range(len(SortedProcess)):
                    if SortedProcess[i]['Tburst']>0:
                        if SortedProcess[i]['Tburst']>timeSlice:
                            self.pushB = QPushButton("" + SortedProcess[i]['name'], self)
                            self.pushB.setFixedWidth(timeSlice * 60)
                            self.pushB.setToolTip("<h3>start from: " + str(start) +
                                              "<br> end: " + str(timeSlice + start) + "</h3>")
                            SortedProcess[i]['waiting'] = start - SortedProcess[i]['TimeInserted']
                            SortedProcess[i]['TimeInserted'] =timeSlice + start
                            start =timeSlice + start
                            self.hbox.addWidget(self.pushB)
                            SortedProcess[i]['Tburst']=SortedProcess[i]['Tburst']-timeSlice

                        else:
                            self.pushB = QPushButton("" + SortedProcess[i]['name'], self)
                            self.pushB.setFixedWidth(SortedProcess[i]['Tburst'] * 30)
                            self.pushB.setToolTip("<h3>start from: " + str(start) +
                                                  "<br> end: " + str(SortedProcess[i]['Tburst'] + start) + "</h3>")
                            SortedProcess[i]['waiting'] = start - SortedProcess[i]['TimeInserted']
                            SortedProcess[i]['TimeInserted'] = SortedProcess[i]['Tburst'] + start
                            start = SortedProcess[i]['Tburst'] + start
                            self.hbox.addWidget(self.pushB)
                            SortedProcess[i]['Tburst'] = SortedProcess[i]['Tburst'] - timeSlice
                sum=0
                for k in range(len(numberList)-1):
                    sum = sum + processList[k]['Tburst']
            waiting=0
            for i in SortedProcess:
                waiting=waiting+i['waiting']
            label = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
            self.vbox.addWidget(label)



        elif self.pri.isChecked() and self.nonpree.isChecked():
            for i in range(len(numberList) ):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted':0 , 'pri': pirority[i]}
                processList.append(process)
            SortedProcess = sorted(processList, key=itemgetter('pri'), reverse=False)
            start = 0
            waiting=0
            for i in SortedProcess:
                self.pushB = QPushButton("" + i['name'], self)
                self.pushB.setFixedWidth(i['Tburst'] * 30)
                self.pushB.setToolTip("<h3>start from: " + str(start) +
                                      "<br> end: " + str(i['Tburst'] + start) + "</h3>")
                waiting=waiting+(start-i['TimeInserted'])
                start = i['Tburst'] + start
                self.hbox.addWidget(self.pushB)
            label = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
            self.vbox.addWidget(label)


        elif self.pri.isChecked() and self.pree.isChecked():
            timeSlice = numberList[-1]
            for i in range(len(numberList)-1):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted': 0, 'pri': pirority[i],'flag':0 ,'waiting':0}
                processList.append(process)
            SortedProcess = sorted(processList, key=itemgetter('pri'), reverse=False)
            duplicateList = list()

            i=0
            while i<len(SortedProcess):
                pairList = list()
                if SortedProcess[i]['flag']==0:
                    pairList.append(SortedProcess[i])
                    SortedProcess[i]['flag']=1
                    for j in range(i + 1, len(SortedProcess)):
                        if (SortedProcess[j]['pri'] == SortedProcess[i]['pri']) and SortedProcess[j]['flag'] == 0:
                            pairList.append(SortedProcess[j])
                            SortedProcess[j]['flag'] = 1
                        else:
                            continue
                    duplicateList.append(pairList)
                    i = i + 1
                else:
                    i = i+1

            start = 0
            waiting=0
            for m in duplicateList:

                if len(m) == 1:

                    self.pushB = QPushButton("" + m[0]['name'], self)
                    self.pushB.setFixedWidth(m[0]['Tburst'] * 30)
                    self.pushB.setToolTip("<h3>start from: " + str(start) +
                                          "<br> end: " + str(m[0]['Tburst'] + start) + "</h3>")
                    waiting = waiting + (start - i['TimeInserted'])
                    start = m[0]['Tburst'] + start
                    self.hbox.addWidget(self.pushB)
                else:
                    sum=0
                    for j in m :
                        sum = sum + j['Tburst']

                    i = 0

                    while (sum > 0):
                        for i in range(len(m)):
                            if m[i]['Tburst'] > 0:
                                if m[i]['Tburst'] > timeSlice:
                                    self.pushB = QPushButton("" + m[i]['name'], self)
                                    self.pushB.setFixedWidth(timeSlice * 60)
                                    self.pushB.setToolTip("<h3>start from: " + str(start) +
                                                          "<br> end: " + str(timeSlice + start) + "</h3>")
                                    m[i]['waiting'] = start - m[i]['TimeInserted']
                                    m[i]['TimeInserted'] = timeSlice + start
                                    start = timeSlice + start
                                    self.hbox.addWidget(self.pushB)
                                    m[i]['Tburst'] = m[i]['Tburst'] - timeSlice

                                else:
                                    self.pushB = QPushButton("" + m[i]['name'], self)
                                    self.pushB.setFixedWidth(m[i]['Tburst'] * 30)
                                    self.pushB.setToolTip("<h3>start from: " + str(start) +
                                                          "<br> end: " + str(
                                        m[i]['Tburst'] + start) + "</h3>")
                                    m[i]['waiting'] = start - m[i]['TimeInserted']
                                    m[i]['TimeInserted'] = m[i]['Tburst'] + start
                                    start = m[i]['Tburst'] + start
                                    self.hbox.addWidget(self.pushB)
                                    m[i]['Tburst'] = m[i]['Tburst'] - timeSlice
                        sum = 0
                        for k in range(len(m)):
                            sum = sum + m[k]['Tburst']

                    for k in range(len(m)):
                        waiting = waiting + m[k]['waiting']
            label = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
            self.vbox.addWidget(label)










if __name__ =="__main__":

    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())