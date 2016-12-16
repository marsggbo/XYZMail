# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem\Email\Libs\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1069, 583)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 570))
        MainWindow.setMaximumSize(QtCore.QSize(1069, 590))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/XYZ.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("\n"
"font: 11pt \"Microsoft YaHei UI\";"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 200, 590))
        self.widget.setWhatsThis(_fromUtf8(""))
        self.widget.setStyleSheet(_fromUtf8("#widget{background-color: rgb(242, 242, 242);}\n"
"\n"
"QPushButton{border:none;}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.headpic_2 = QtGui.QGraphicsView(self.widget)
        self.headpic_2.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.headpic_2.setMaximumSize(QtCore.QSize(200, 50))
        self.headpic_2.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/XYZ.jpg);"))
        self.headpic_2.setObjectName(_fromUtf8("headpic_2"))
        self.slidebar = QtGui.QGroupBox(self.widget)
        self.slidebar.setGeometry(QtCore.QRect(0, 425, 29, 171))
        self.slidebar.setStyleSheet(_fromUtf8("QGroupBox{background-color: rgb(79, 79, 79);}\n"
"QPushButton{\n"
"    width:20px;\n"
"    height:20px;\n"
"}\n"
"QPushButton:hover {\n"
"       Background-color:rgb(29,171,123);\n"
"}"))
        self.slidebar.setObjectName(_fromUtf8("slidebar"))
        self.about = QtGui.QPushButton(self.slidebar)
        self.about.setGeometry(QtCore.QRect(2, 19, 25, 25))
        self.about.setMouseTracking(False)
        self.about.setAccessibleName(_fromUtf8(""))
        self.about.setStyleSheet(_fromUtf8("#sliderbar1:hover{\n"
"background-color: rgb(255, 170, 127);}"))
        self.about.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/邮箱 (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon1)
        self.about.setObjectName(_fromUtf8("about"))
        self.addressbook = QtGui.QPushButton(self.slidebar)
        self.addressbook.setGeometry(QtCore.QRect(2, 56, 25, 25))
        self.addressbook.setStyleSheet(_fromUtf8("leftbar QPushButtom{background-color:gray;}"))
        self.addressbook.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/通讯录.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addressbook.setIcon(icon2)
        self.addressbook.setObjectName(_fromUtf8("addressbook"))
        self.calender = QtGui.QPushButton(self.slidebar)
        self.calender.setGeometry(QtCore.QRect(2, 93, 25, 25))
        self.calender.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/日历.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calender.setIcon(icon3)
        self.calender.setObjectName(_fromUtf8("calender"))
        self.settings = QtGui.QPushButton(self.slidebar)
        self.settings.setGeometry(QtCore.QRect(2, 130, 25, 25))
        self.settings.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/设置.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon4)
        self.settings.setObjectName(_fromUtf8("settings"))
        self.headlogo = QtGui.QGraphicsView(self.widget)
        self.headlogo.setGeometry(QtCore.QRect(60, 110, 80, 80))
        self.headlogo.setStyleSheet(_fromUtf8("#headlogo{\n"
"border-image: url(:/souce/souce/登录.png);\n"
"border-radius:40px;\n"
"}"))
        self.headlogo.setObjectName(_fromUtf8("headlogo"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 200, 50))
        self.groupBox.setStyleSheet(_fromUtf8("QPushButton{background-color:rgb(41,189,139);}\n"
"QPushButton:hover {\n"
"       Background-color:rgb(29,171,123);\n"
"}"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mainwriteletter = QtGui.QPushButton(self.groupBox)
        self.mainwriteletter.setGeometry(QtCore.QRect(0, 0, 102, 50))
        self.mainwriteletter.setObjectName(_fromUtf8("mainwriteletter"))
        self.mainreceiveletter = QtGui.QPushButton(self.groupBox)
        self.mainreceiveletter.setGeometry(QtCore.QRect(100, 0, 100, 50))
        self.mainreceiveletter.setObjectName(_fromUtf8("mainreceiveletter"))
        self.mainlogin = QtGui.QPushButton(self.widget)
        self.mainlogin.setGeometry(QtCore.QRect(80, 230, 41, 41))
        self.mainlogin.setStyleSheet(_fromUtf8("#mainlogin{\n"
"background-color: rgb(41, 189, 139);\n"
"\n"
"}\n"
"#mainlogin:hover{\n"
"background-color: rgb(29,171,123);\n"
"border-radius:20px;\n"
"}"))
        self.mainlogin.setObjectName(_fromUtf8("mainlogin"))
        self.mainUserName = QtGui.QLabel(self.widget)
        self.mainUserName.setGeometry(QtCore.QRect(0, 210, 199, 20))
        self.mainUserName.setStyleSheet(_fromUtf8("background-color: rg(b242,242,242);"))
        self.mainUserName.setText(_fromUtf8(""))
        self.mainUserName.setAlignment(QtCore.Qt.AlignCenter)
        self.mainUserName.setObjectName(_fromUtf8("mainUserName"))
        self.sendedBox = QtGui.QPushButton(self.widget)
        self.sendedBox.setGeometry(QtCore.QRect(0, 340, 201, 31))
        self.sendedBox.setStyleSheet(_fromUtf8("#sendedBox{background-color: rgb(85, 255, 127);}\n"
"#sendedBox:hover{\n"
"background-color: rgb(123,25,36);\n"
"}"))
        self.sendedBox.setObjectName(_fromUtf8("sendedBox"))
        self.receivedBox = QtGui.QPushButton(self.widget)
        self.receivedBox.setGeometry(QtCore.QRect(0, 300, 201, 31))
        self.receivedBox.setStyleSheet(_fromUtf8("#receivedBox{background-color: rgb(85, 255, 127);}\n"
"#receivedBox:hover{\n"
"background-color: rgb(123,25,36);\n"
"}"))
        self.receivedBox.setObjectName(_fromUtf8("receivedBox"))
        self.receivedletter = QtGui.QGroupBox(self.centralWidget)
        self.receivedletter.setGeometry(QtCore.QRect(200, 50, 260, 540))
        self.receivedletter.setStyleSheet(_fromUtf8("#receivedletter{background-color: white;}\n"
"#receivedletter QPushButton{\n"
"    background-color: rgb(243,243,243);\n"
"    border:none;\n"
"}\n"
"#receivedletter QPushButton:hover{\n"
"    color:rgb(29,171,123);\n"
"}"))
        self.receivedletter.setTitle(_fromUtf8(""))
        self.receivedletter.setObjectName(_fromUtf8("receivedletter"))
        self.emailsort = QtGui.QPushButton(self.receivedletter)
        self.emailsort.setGeometry(QtCore.QRect(0, 0, 132, 50))
        self.emailsort.setObjectName(_fromUtf8("emailsort"))
        self.emaillist = QtGui.QListWidget(self.receivedletter)
        self.emaillist.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.emaillist.setStyleSheet(_fromUtf8("#emaillist{background-color: rgb(242,242,242);}\n"
"#emaillist::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#emaillist::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.emaillist.setTabKeyNavigation(True)
        self.emaillist.setObjectName(_fromUtf8("emaillist"))
        self.sendedList = QtGui.QListWidget(self.receivedletter)
        self.sendedList.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.sendedList.setStyleSheet(_fromUtf8("#sendedList{background-color: rgb(242,242,242);}\n"
"#sendedList::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#sendedList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.sendedList.setTabKeyNavigation(True)
        self.sendedList.setObjectName(_fromUtf8("sendedList"))
        self.searchList = QtGui.QListWidget(self.receivedletter)
        self.searchList.setGeometry(QtCore.QRect(0, 50, 260, 490))
        self.searchList.setStyleSheet(_fromUtf8("#searchList{background-color: rgb(242,242,242);}\n"
"#searchList::Item{\n"
"width:260px;\n"
"height:80px;\n"
"}\n"
"#searchList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.searchList.setTabKeyNavigation(True)
        self.searchList.setObjectName(_fromUtf8("searchList"))
        self.emailsort_2 = QtGui.QPushButton(self.receivedletter)
        self.emailsort_2.setGeometry(QtCore.QRect(130, 0, 132, 50))
        self.emailsort_2.setObjectName(_fromUtf8("emailsort_2"))
        self.moreemail = QtGui.QPushButton(self.receivedletter)
        self.moreemail.setGeometry(QtCore.QRect(200, 460, 41, 41))
        self.moreemail.setStyleSheet(_fromUtf8("#moreemail{\n"
"background-color:rgb(56,56,78);\n"
"    border-radius:20px;\n"
"color:white;\n"
"    font-size:30px;\n"
"}\n"
"#moreemail:hover{\n"
"background-color:rgb(123,25,65);\n"
"}\n"
""))
        self.moreemail.setObjectName(_fromUtf8("moreemail"))
        self.emailsort.raise_()
        self.sendedList.raise_()
        self.searchList.raise_()
        self.emaillist.raise_()
        self.emailsort_2.raise_()
        self.moreemail.raise_()
        self.showemail = QtGui.QGroupBox(self.centralWidget)
        self.showemail.setGeometry(QtCore.QRect(459, 50, 611, 540))
        self.showemail.setStyleSheet(_fromUtf8("#showemail{background-color: white;}\n"
""))
        self.showemail.setTitle(_fromUtf8(""))
        self.showemail.setObjectName(_fromUtf8("showemail"))
        self.emailShow = QtWebKit.QWebView(self.showemail)
        self.emailShow.setGeometry(QtCore.QRect(0, 82, 611, 461))
        self.emailShow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.emailShow.setUrl(QtCore.QUrl(_fromUtf8("qrc:/souce/index.html")))
        self.emailShow.setObjectName(_fromUtf8("emailShow"))
        self.contInfoTop = QtGui.QGroupBox(self.showemail)
        self.contInfoTop.setGeometry(QtCore.QRect(0, 0, 611, 80))
        self.contInfoTop.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 14px \"微软雅黑\";"))
        self.contInfoTop.setTitle(_fromUtf8(""))
        self.contInfoTop.setObjectName(_fromUtf8("contInfoTop"))
        self.contLogo = QtGui.QLabel(self.contInfoTop)
        self.contLogo.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.contLogo.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/登录.png);"))
        self.contLogo.setText(_fromUtf8(""))
        self.contLogo.setObjectName(_fromUtf8("contLogo"))
        self.contName = QtGui.QLabel(self.contInfoTop)
        self.contName.setGeometry(QtCore.QRect(70, 20, 181, 20))
        self.contName.setStyleSheet(_fromUtf8(""))
        self.contName.setObjectName(_fromUtf8("contName"))
        self.contEmail = QtGui.QLabel(self.contInfoTop)
        self.contEmail.setGeometry(QtCore.QRect(340, 20, 251, 20))
        self.contEmail.setStyleSheet(_fromUtf8(""))
        self.contEmail.setObjectName(_fromUtf8("contEmail"))
        self.contEmailTime = QtGui.QLabel(self.contInfoTop)
        self.contEmailTime.setGeometry(QtCore.QRect(70, 50, 231, 20))
        self.contEmailTime.setStyleSheet(_fromUtf8(""))
        self.contEmailTime.setObjectName(_fromUtf8("contEmailTime"))
        self.contEmailSubject = QtGui.QLabel(self.contInfoTop)
        self.contEmailSubject.setGeometry(QtCore.QRect(340, 50, 251, 20))
        self.contEmailSubject.setStyleSheet(_fromUtf8(""))
        self.contEmailSubject.setObjectName(_fromUtf8("contEmailSubject"))
        self.attachList = QtGui.QListWidget(self.showemail)
        self.attachList.setGeometry(QtCore.QRect(0, 401, 271, 131))
        self.attachList.setStyleSheet(_fromUtf8("#attachList{background-color: tomato;\n"
"}\n"
"#attachList::Item{\n"
"height:50px;\n"
"}\n"
"#attachList::Item:hover{\n"
"background-color: rgb(41, 189, 139);\n"
"}"))
        self.attachList.setObjectName(_fromUtf8("attachList"))
        item = QtGui.QListWidgetItem()
        self.attachList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.attachList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.attachList.addItem(item)
        self.searchlineEdit = QtGui.QLineEdit(self.centralWidget)
        self.searchlineEdit.setGeometry(QtCore.QRect(237, 19, 190, 21))
        self.searchlineEdit.setStyleSheet(_fromUtf8("#searchlineEdit{background-color:white;}"))
        self.searchlineEdit.setText(_fromUtf8(""))
        self.searchlineEdit.setObjectName(_fromUtf8("searchlineEdit"))
        self.mainclose = QtGui.QPushButton(self.centralWidget)
        self.mainclose.setGeometry(QtCore.QRect(1030, 15, 20, 20))
        self.mainclose.setStyleSheet(_fromUtf8("#mainclose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#mainclose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.mainclose.setText(_fromUtf8(""))
        self.mainclose.setObjectName(_fromUtf8("mainclose"))
        self.mainmin = QtGui.QPushButton(self.centralWidget)
        self.mainmin.setGeometry(QtCore.QRect(1000, 15, 20, 20))
        self.mainmin.setToolTip(_fromUtf8(""))
        self.mainmin.setStyleSheet(_fromUtf8("#mainmin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#mainmin:hover{\n"
"border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.mainmin.setText(_fromUtf8(""))
        self.mainmin.setObjectName(_fromUtf8("mainmin"))
        self.mainSearch = QtGui.QPushButton(self.centralWidget)
        self.mainSearch.setGeometry(QtCore.QRect(207, 20, 25, 25))
        self.mainSearch.setStyleSheet(_fromUtf8("#mainSearch{\n"
"    border:none;\n"
"    border-radius:12px;\n"
"}\n"
"#mainSearch:hover{\n"
"    background-color:rgb(49,126,243);\n"
"}"))
        self.mainSearch.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/搜索框－搜索.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainSearch.setIcon(icon5)
        self.mainSearch.setObjectName(_fromUtf8("mainSearch"))
        self.mainReply = QtGui.QPushButton(self.centralWidget)
        self.mainReply.setGeometry(QtCore.QRect(580, 20, 61, 31))
        self.mainReply.setStyleSheet(_fromUtf8("#mainForward{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color: rgb(219,219,219);\n"
"}\n"
"#mainForward:hover{\n"
"background-color:rgb(41,189,139);\n"
"color:white;\n"
"}"))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainReply.setIcon(icon6)
        self.mainReply.setObjectName(_fromUtf8("mainReply"))
        self.mainForward = QtGui.QPushButton(self.centralWidget)
        self.mainForward.setGeometry(QtCore.QRect(670, 20, 61, 31))
        self.mainForward.setStyleSheet(_fromUtf8("#mainForward{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color: rgb(219,219,219);\n"
"}\n"
"#mainForward:hover{\n"
"background-color:rgb(41,189,139);\n"
"color:white;\n"
"}"))
        self.mainForward.setIcon(icon6)
        self.mainForward.setObjectName(_fromUtf8("mainForward"))
        self.delEmail = QtGui.QPushButton(self.centralWidget)
        self.delEmail.setGeometry(QtCore.QRect(800, 20, 61, 31))
        self.delEmail.setStyleSheet(_fromUtf8("#delEmail{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color: rgb(219,219,219);\n"
"}\n"
"#delEmail:hover{\n"
"background-color:tomato;\n"
"color:white;\n"
"}"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/关闭1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delEmail.setIcon(icon7)
        self.delEmail.setObjectName(_fromUtf8("delEmail"))
        self.mainAttach = QtGui.QPushButton(self.centralWidget)
        self.mainAttach.setGeometry(QtCore.QRect(890, 20, 91, 31))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/附件.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainAttach.setIcon(icon8)
        self.mainAttach.setObjectName(_fromUtf8("mainAttach"))
        self.searchMode = QtGui.QComboBox(self.centralWidget)
        self.searchMode.setGeometry(QtCore.QRect(430, 20, 91, 21))
        self.searchMode.setObjectName(_fromUtf8("searchMode"))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        self.searchMode.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.emaillist.setCurrentRow(-1)
        self.sendedList.setCurrentRow(-1)
        self.searchList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "XYZ Mail", None))
        self.about.setToolTip(_translate("MainWindow", "关于", None))
        self.addressbook.setToolTip(_translate("MainWindow", "通讯录", None))
        self.addressbook.setWhatsThis(_translate("MainWindow", "通讯录", None))
        self.calender.setToolTip(_translate("MainWindow", "日历", None))
        self.settings.setToolTip(_translate("MainWindow", "设置", None))
        self.mainwriteletter.setText(_translate("MainWindow", "写信", None))
        self.mainreceiveletter.setText(_translate("MainWindow", "收信", None))
        self.mainlogin.setText(_translate("MainWindow", "登录", None))
        self.sendedBox.setText(_translate("MainWindow", "已发送", None))
        self.receivedBox.setText(_translate("MainWindow", "收件箱", None))
        self.emailsort.setText(_translate("MainWindow", "主题排序", None))
        self.emaillist.setSortingEnabled(True)
        self.sendedList.setSortingEnabled(True)
        self.searchList.setSortingEnabled(True)
        self.emailsort_2.setText(_translate("MainWindow", "发信人排序", None))
        self.moreemail.setText(_translate("MainWindow", "+", None))
        self.contName.setText(_translate("MainWindow", "用户名", None))
        self.contEmail.setText(_translate("MainWindow", "邮  箱", None))
        self.contEmailTime.setText(_translate("MainWindow", "时  间", None))
        self.contEmailSubject.setText(_translate("MainWindow", "主  题", None))
        __sortingEnabled = self.attachList.isSortingEnabled()
        self.attachList.setSortingEnabled(False)
        item = self.attachList.item(0)
        item.setText(_translate("MainWindow", "每次看见大客车绝对是.json", None))
        item = self.attachList.item(1)
        item.setText(_translate("MainWindow", "hello world", None))
        item = self.attachList.item(2)
        item.setText(_translate("MainWindow", "小撒爱上.jpg", None))
        self.attachList.setSortingEnabled(__sortingEnabled)
        self.searchlineEdit.setPlaceholderText(_translate("MainWindow", "搜索邮件信息", None))
        self.mainReply.setText(_translate("MainWindow", "回复", None))
        self.mainForward.setText(_translate("MainWindow", "转发", None))
        self.delEmail.setText(_translate("MainWindow", "删除", None))
        self.mainAttach.setText(_translate("MainWindow", "查看附件", None))
        self.searchMode.setItemText(0, _translate("MainWindow", "请选择", None))
        self.searchMode.setItemText(1, _translate("MainWindow", "主题", None))
        self.searchMode.setItemText(2, _translate("MainWindow", "时间", None))
        self.searchMode.setItemText(3, _translate("MainWindow", "联系人", None))
        self.searchMode.setItemText(4, _translate("MainWindow", "邮件内容", None))

from PyQt4 import QtWebKit
import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

