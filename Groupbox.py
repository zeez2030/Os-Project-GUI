from PyQt5.QtWidgets import QScrollArea,QCheckBox,QSpinBox,QRadioButton,QLabel,QWidget, QApplication,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout
import  sys
from PyQt5 import QtGui
from operator import itemgetter
from plotly.offline import   plot
import plotly.figure_factory as ff



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
        self.initBox()
        self.setLayout(self.hbox)
        self.show()
    def initBox(self):


        self.groupbox = QGroupBox("Type of scheduler")
        self.groupbox.setFont(QtGui.QFont("sanserif", 15))
        self.hbox.addWidget(self.groupbox)

        self.vbox = QVBoxLayout()

        self.FCFS = QRadioButton("FCFS")
        self.vbox.addWidget(self.FCFS)

        self.SJF = QRadioButton("SJF")
        self.vbox.addWidget(self.SJF)

        self.RR = QRadioButton("RR")
        self.vbox.addWidget(self.RR)

        self.pri = QRadioButton("Priority")
        self.vbox.addWidget(self.pri)

        self.button = QPushButton("Next", self)
        self.button.clicked.connect(self.next)
        self.vbox.addWidget(self.button)

        self.groupbox.setLayout(self.vbox)

        self.i = 0

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
        self.groupbox2 = QGroupBox("Process's info")
        self.groupbox2.setFont(QtGui.QFont("sanserif", 15))
        self.vbox2 = QVBoxLayout()
        if self.nonpree.isChecked():
            self.pree.hide()
            self.nonpree.hide()
            self.label = QLabel("Type : "+self.nonpree.text())
            self.label.setFont(QtGui.QFont("sanserif", 15))
            self.vbox2.addWidget(self.label)
        elif self.pree.isChecked():
            self.pree.hide()
            self.nonpree.hide()
            self.label = QLabel("Type : "+self.pree.text())
            self.label.setFont(QtGui.QFont("sanserif", 15))
            self.vbox2.addWidget(self.label)
        for j in range(i):
            self.label = QLabel("P"+str(j+1))
            self.lList.append(self.label)
            self.label.setFont(QtGui.QFont("sanserif",15))
            self.vbox2.addWidget(self.label)
            self.label = QLabel("Burst Time")
            self.timeShots.append(self.label)
            self.label.setFont(QtGui.QFont("sanserif",13))
            self.textbox = QSpinBox(self)
            self.tList.append(self.textbox)
            self.vbox2.addWidget(self.label)
            self.vbox2.addWidget(self.textbox)

            if not( self.pri.isChecked() and self.nonpree.isChecked()) :
                self.label = QLabel("Arrival Time:")
                self.timeShots.append(self.label)
                self.label.setFont(QtGui.QFont("sanserif", 13))
                self.vbox2.addWidget(self.label)
                self.textbox = QSpinBox(self)
                self.timeInserted.append(self.textbox)
                self.vbox2.addWidget(self.textbox)


            if self.pri.isChecked():
                self.label = QLabel("Priority (low number is higher in priority)")
                self.timeShots.append(self.label)
                self.label.setFont(QtGui.QFont("sanserif", 13))
                self.textbox = QSpinBox(self)
                self.pirority.append(self.textbox)
                self.vbox2.addWidget(self.label)
                self.vbox2.addWidget(self.textbox)
        if self.RR.isChecked() or (self.pri.isChecked() and self.nonpree.isChecked()):
            self.label = QLabel("Time Quantum:")
            self.label.setFont(QtGui.QFont("sanserif", 15))
            self.timeShots.append(self.label)
            self.vbox2.addWidget(self.label)
            self.textbox = QSpinBox(self)
            self.tList.append(self.textbox)
            self.vbox2.addWidget(self.textbox)
        self.button.hide()
        self.button = QPushButton("Draw", self)
        self.button.clicked.connect(self.Draw)
        self.vbox2.addWidget(self.button)
        self.groupbox2.setLayout(self.vbox2)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.groupbox2)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedWidth(600)
        self.hbox.addWidget(self.scroll)
    def Draw(self):
        df=list()
        self.button.hide()
        self.button = QPushButton("Restart", self)
        self.button.clicked.connect(self.restart)
        self.vbox.addWidget(self.button)
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
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted': inserted[i], 'waiting': 0}
                processList.append(process)
            SortedArrival = sorted(processList, key=itemgetter('TimeInserted'), reverse=False)
            SortedProcess = sorted(processList, key=itemgetter('Tburst'), reverse=False)



            timeinserted=0
            for p in SortedProcess:
                timeinserted = timeinserted + p['TimeInserted']

            if timeinserted==0:
                start = 0
                waiting=0
                for i in SortedProcess:
                    df.append(dict(Task=i['name'], Start=start , Finish=i['Tburst']+start))
                    waiting=waiting+(start)
                    start=i['Tburst']+start
                self.labelTime = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
                self.vbox.addWidget(self.labelTime)
                fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True ,showgrid_x=True ,showgrid_y=True)
                fig['layout']['xaxis'].update({'type': None})
                plot(fig)
            else:
                sum = 1
                min = 100
                index = 0
                start = SortedArrival[0]['TimeInserted']
                time = SortedArrival[0]['TimeInserted']
                while sum>0:
                    for i in range(len(SortedArrival)):
                        print("in the for loop")
                        if i == index:
                            df.append(dict(Task=SortedArrival[i]['name'], Start=start, Finish=start+SortedArrival[i]['Tburst']))
                            SortedArrival[i]['waiting']=start - SortedArrival[i]['TimeInserted']
                            time=start+SortedArrival[i]['Tburst']
                            start = time
                            SortedArrival[i]['Tburst'] = 0
                            min=100
                            for p in range(len(SortedArrival)):
                                if SortedArrival[p]['TimeInserted'] <= time and SortedArrival[p]['Tburst'] < min and SortedArrival[p]['Tburst'] > 0:
                                    index = p
                                    min = SortedArrival[p]['Tburst']
                    sum = 0
                    for p in SortedArrival:
                        sum = sum + p['Tburst']
                waiting=0
                for p in SortedArrival:
                    waiting = waiting + p['waiting']
                self.labelTime = QLabel("Average waiting time : " + str(waiting / len(SortedArrival)) + " ms")
                self.vbox.addWidget(self.labelTime)
                fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True, showgrid_x=True, showgrid_y=True)
                fig['layout']['xaxis'].update({'type': None})
                plot(fig)



        elif self.SJF.isChecked() and self.pree.isChecked():
            for i in range(len(numberList)):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted': inserted[i] , 'waiting':0 , 'finished':inserted[i]}
                processList.append(process)
            SortedArrival = sorted(processList, key=itemgetter('TimeInserted'), reverse=False)
            SortedBurst = sorted(processList, key=itemgetter('Tburst'), reverse=False)
            sum = 1
            start = SortedArrival[0]['TimeInserted']
            k = 0
            time = SortedArrival[0]['TimeInserted']
            min = 100
            while sum > 0:
                for i in range(len(SortedArrival)):
                    if SortedArrival[i]['TimeInserted'] <= time and SortedArrival[i]['Tburst'] < min and SortedArrival[i]['Tburst'] > 0:
                        if time > SortedArrival[0]['TimeInserted']:
                            df.append(dict(Task=SortedArrival[index]['name'], Start=start, Finish=time))
                            SortedArrival[index]['finished'] = time
                            start = time
                            SortedArrival[index]['Tburst'] = SortedArrival[index]['Tburst'] - k
                            k = 0
                        index = i
                        SortedArrival[index]['waiting'] = SortedArrival[index]['waiting'] + (time - SortedArrival[index]['finished'])
                        min = SortedArrival[index]['Tburst']
                        time = time + 1
                        k = k + 1
                    else:
                        SortedArrival[index]['Tburst'] = SortedArrival[index]['Tburst'] - 1
                        if SortedArrival[index]['Tburst'] == 0:
                            df.append(dict(Task=SortedArrival[index]['name'], Start=start, Finish=time))
                            start = time
                            k = 0
                            min = 100
                            found=0
                            for j in range(len(SortedArrival)):
                                if SortedArrival[j]['TimeInserted'] <= time and SortedArrival[j]['Tburst'] < min and SortedArrival[j]['Tburst'] > 0:
                                    min = SortedArrival[j]['Tburst']
                                    index = j
                                    found=1
                            if found==1:
                                SortedArrival[index]['waiting'] = SortedArrival[index]['waiting'] + (time - SortedArrival[index]['finished'])
                        else:
                            min = SortedArrival[index]['Tburst']

                        time = time + 1
                        k = k + 1
                        if SortedArrival[i]['TimeInserted'] <= time and SortedArrival[i]['Tburst'] < min and SortedArrival[i]['Tburst'] > 0:
                            df.append(dict(Task=SortedArrival[index]['name'], Start=start, Finish=time))
                            SortedArrival[index]['finished'] = time
                            start = time
                            SortedArrival[index]['Tburst'] = SortedArrival[index]['Tburst'] - k+1
                            k = 0
                            index = i
                            SortedArrival[index]['waiting'] = SortedArrival[index]['waiting'] + (time - SortedArrival[index]['finished'])
                            min = SortedArrival[index]['Tburst']
                            time=time+1
                            k=k+1
                sum = 0
                for p in SortedArrival:
                    sum = sum + p['Tburst']
            waiting=0
            for p in SortedArrival:
                waiting=waiting+p['waiting']
            self.labelTime = QLabel("Average waiting time : "+ str(waiting/len(SortedArrival))+" ms")
            self.vbox.addWidget(self.labelTime)
            fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True ,showgrid_x=True ,showgrid_y=True)
            fig['layout']['xaxis'].update({'type': None})
            plot(fig)

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
                if start < i['TimeInserted']:
                    start = i['TimeInserted']
                df.append(dict(Task=i['name'], Start=start , Finish=i['Tburst']+start))
                waiting=waiting+(start - i['TimeInserted'])
                start =i['Tburst'] + start
            self.labelTime = QLabel("Average waiting time : "+str(waiting/len(SortedProcess))+" ms")
            self.vbox.addWidget( self.labelTime)
            fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True ,showgrid_x=True ,showgrid_y=True)
            fig['layout']['xaxis'].update({'type': None})
            plot(fig)

        elif self.RR.isChecked():
            queue = list()
            timeSlice = numberList[-1]
            processList = list()
            sum = 1
            for i in range(len(numberList) - 1):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted': inserted[i], 'waiting': 0, 'finished': inserted[i]}
                processList.append(process)

            SortedProcess = sorted(processList, key=itemgetter('TimeInserted'), reverse=False)
            time = SortedProcess[0]['TimeInserted']
            start = SortedProcess[0]['TimeInserted']
            queue.append(SortedProcess[0])
            i = 0
            while (sum > 0):
                if len(queue) > 0:
                    if queue[0]['TimeInserted'] <= time:
                        if queue[0]['Tburst']>timeSlice:
                            df.append(dict(Task=queue[0]['name'], Start=time, Finish=timeSlice + time ))

                            if time != queue[0]['finished']:
                                queue[0]['waiting'] = queue[0]['waiting']+(time - queue[0]['finished'])
                            elif queue[0]['name'] == SortedProcess[0]['name']:
                                queue[0]['waiting'] = queue[0]['waiting'] + (time - queue[0]['finished'])
                            queue[0]['finished']=timeSlice + time
                            queue[0]['Tburst'] = queue[0]['Tburst'] - timeSlice
                            z=queue[0]
                            time = timeSlice + time
                            # queue.pop(0)
                            for j in SortedProcess:
                                if j['name'] == z['name']:
                                    j['Tburst'] = z['Tburst']
                                    j['finished']=z['finished']
                                    j['waiting']=z['waiting']

                            for j in SortedProcess:
                                found = 0
                                for p in queue:
                                    if j['name'] == p['name']:
                                        found = 1
                                        break
                                if found == 1:
                                    continue
                                else:
                                    if j['Tburst'] > 0 and j['TimeInserted'] <= time:
                                        queue.append(j)
                            queue.pop(0)
                            queue.append(z)



                        else:
                            df.append(dict(Task=queue[0]['name'], Start=time, Finish=queue[0]['Tburst'] + time))

                            if time != queue[0]['finished']:
                                queue[0]['waiting'] =queue[0]['waiting']+(time - queue[0]['finished'])
                            elif queue[0]['name'] == SortedProcess[0]['name']:
                                queue[0]['waiting'] = queue[0]['waiting'] + (time - queue[0]['finished'])
                            time = queue[0]['Tburst'] + time
                            queue[0]['Tburst'] = 0
                            z=queue[0]
                            queue.pop(0)
                            for j in SortedProcess:
                                if j['name'] == z['name']:
                                    j['Tburst'] =0
                                    j['finished'] = z['finished']
                                    j['waiting'] = z['waiting']

                            for j in SortedProcess:
                                found = 0
                                for p in queue:
                                    if j['name'] == p['name']:
                                        found=1
                                        break
                                if found==1:
                                    continue
                                else:
                                    if j['Tburst']>0 and j['TimeInserted'] <= time:
                                        queue.append(j)
                else:
                    time = time+1
                    for j in SortedProcess:
                        found = 0
                        for p in queue:
                            if j['name'] == p['name']:
                                found = 1
                                break
                        if found == 1:
                            continue
                        else:
                            if j['Tburst'] > 0 and j['TimeInserted'] <= time:
                                queue.append(j)


                print(queue)
                sum = 0
                for k in SortedProcess:
                    sum = sum + k['Tburst']
                print(sum)
            waiting = 0
            for i in SortedProcess:
                waiting = waiting + i['waiting']
            self.labelTime = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
            self.vbox.addWidget(self.labelTime)
            fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True, showgrid_x=True, showgrid_y=True)
            fig['layout']['xaxis'].update({'type': None})
            plot(fig)

        elif self.pri.isChecked() and self.nonpree.isChecked():
            timeSlice = numberList[-1]
            print(timeSlice)
            for i in range(len(numberList)-1):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted': 0, 'pri': pirority[i],'flag':0 ,'waiting':0 , 'finished':0}
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
                    df.append(dict(Task=m[0]['name'], Start=start, Finish=m[0]['Tburst'] + start))
                    waiting = waiting + (start - m[0]['TimeInserted'])
                    start = m[0]['Tburst'] + start
                else:
                    sum=0
                    for j in m :
                        sum = sum + j['Tburst']

                    i = 0


                    while (sum > 0):
                        for i in range(len(m)):
                            if m[i]['Tburst'] > 0:
                                if m[i]['Tburst'] > timeSlice:
                                    df.append(dict(Task=m[i]['name'], Start=start, Finish=timeSlice + start))
                                    if start != m[i]['finished']:
                                        m[i]['waiting'] = m[i]['waiting'] + (start - m[i]['finished'])
                                    m[i]['finished'] = timeSlice + start
                                    m[i]['TimeInserted'] = timeSlice + start
                                    start = timeSlice + start
                                    m[i]['Tburst'] = m[i]['Tburst'] - timeSlice

                                else:
                                    df.append(dict(Task=m[i]['name'], Start=start, Finish= m[i]['Tburst'] + start))
                                    if start != m[i]['finished']:
                                        m[i]['waiting'] = m[i]['waiting'] + (start - m[i]['finished'])
                                    m[i]['finished'] = timeSlice + start
                                    m[i]['TimeInserted'] = m[i]['Tburst'] + start
                                    start = m[i]['Tburst'] + start
                                    m[i]['Tburst'] = m[i]['Tburst'] - timeSlice
                        sum = 0
                        for k in range(len(m)):
                            sum = sum + m[k]['Tburst']

                    for k in range(len(m)):
                        waiting = waiting + m[k]['waiting']
            self.labelTime = QLabel("Average waiting time : " + str(waiting / len(SortedProcess)) + " ms")
            self.vbox.addWidget( self.labelTime)
            fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True ,showgrid_x=True ,showgrid_y=True)
            fig['layout']['xaxis'].update({'type': None})
            #
            plot(fig)

        elif self.pri.isChecked() and self.pree.isChecked():
            for i in range(len(numberList)):
                process = {'name': nameList[i], 'Tburst': numberList[i],
                           'TimeInserted': inserted[i] , 'waiting':0 ,'pri': pirority[i],'finished':inserted[i]}
                processList.append(process)
            SortedArrival = sorted(processList, key=itemgetter('TimeInserted'), reverse=False)

            sum = 1
            start = SortedArrival[0]['TimeInserted']
            k = 0
            time = SortedArrival[0]['TimeInserted']
            min = 100

            while sum > 0:

                for i in range(len(SortedArrival)):

                    if SortedArrival[i]['TimeInserted'] <= time and SortedArrival[i]['pri'] < min and SortedArrival[i]['Tburst'] > 0:
                        if time > SortedArrival[0]['TimeInserted']:
                            df.append(dict(Task=SortedArrival[index]['name'], Start=start, Finish=time))
                            SortedArrival[index]['finished'] = time
                            start = time
                            SortedArrival[index]['Tburst'] = SortedArrival[index]['Tburst'] - k
                            k = 0
                        index = i
                        SortedArrival[index]['waiting']=  SortedArrival[index]['waiting']+(time - SortedArrival[index]['finished'])
                        min = SortedArrival[index]['pri']
                        time = time + 1
                        k = k + 1
                    else:
                        SortedArrival[index]['Tburst'] = SortedArrival[index]['Tburst'] - 1
                        if SortedArrival[index]['Tburst'] == 0:
                            df.append(dict(Task=SortedArrival[index]['name'], Start=start, Finish=time))
                            start = time
                            k = 0
                            min = 100
                            found=0
                            for j in range(len(SortedArrival)):
                                if SortedArrival[j]['TimeInserted'] <= time and SortedArrival[j]['pri'] < min and SortedArrival[j]['Tburst'] > 0:
                                    min = SortedArrival[j]['pri']
                                    index = j
                                    found=1
                            if found == 1:
                                SortedArrival[index]['waiting'] = SortedArrival[index]['waiting'] + (time - SortedArrival[index]['finished'])
                        else:
                            min = SortedArrival[index]['pri']

                        time = time + 1
                        k = k + 1
                        if SortedArrival[i]['TimeInserted'] <= time and SortedArrival[i]['pri'] < min and  SortedArrival[i]['Tburst'] > 0:
                            df.append(dict(Task=SortedArrival[index]['name'], Start=start, Finish=time))
                            SortedArrival[index]['finished'] = time
                            start = time
                            SortedArrival[index]['Tburst'] = SortedArrival[index]['Tburst'] - k +1
                            k = 0
                            index = i
                            SortedArrival[index]['waiting']= SortedArrival[index]['waiting']+(time - SortedArrival[index]['finished'])
                            min = SortedArrival[index]['pri']
                            time = time + 1
                            k = k + 1
                sum = 0
                for p in SortedArrival:
                    sum = sum + p['Tburst']
            waiting=0
            for p in SortedArrival:
                waiting=waiting+p['waiting']
                print(p['waiting'])
            self.labelTime = QLabel("Average waiting time : "+ str(waiting/len(SortedArrival))+" ms")
            self.vbox.addWidget(self.labelTime)
            fig = ff.create_gantt(df, show_colorbar=True, group_tasks=True ,showgrid_x=True ,showgrid_y=True)
            fig['layout']['xaxis'].update({'type': None})
            plot(fig)

    def restart(self):

        self.button.hide()
        self.labelTime.hide()
        self.groupbox.hide()
        self.scroll.hide()
        self.initBox()









if __name__ =="__main__":

    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
