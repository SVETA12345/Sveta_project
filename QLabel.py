# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow5(object):
    def setupUi(self, MainWindow5):
        MainWindow5.setObjectName("MainWindow5")
        MainWindow5.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow5)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 767, 1500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow5)
        self.statusbar.setObjectName("statusbar")
        MainWindow5.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow5)

    def retranslateUi(self, MainWindow5):
        _translate = QtCore.QCoreApplication.translate
        MainWindow5.setWindowTitle(_translate("MainWindow5", "MainWindow"))
        self.label.setText(_translate("MainWindow5", "<html>\n"
"<head>\n"
"<style>\n"
"\n"
"\n"
".blob-code-inner{overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:var(--color-text-primary);word-wrap:normal;white-space:pre}\n"
"\n"
".pl-k{color:#d73a49}\n"
".pl-v{color:#005cc5}\n"
".pl-en{color:#6f42c1}\n"
"</style>\n"
"</head>\n"
"<body>\n"
"<hr>\n"
"<br><b>\n"
"<h2 ALIGN=\"center\">Виджет QLabel </h2>\n"
"</b>\n"
"<p>\n"
"Виджет QLabel позволяет отображать текст или рисунок.\n"
"<p>\n"
"<h3>Меняем шрифт QLabel</h3 >\n"
"<p>\n"
"Чтобы поменять шрифт QLabel, используйте метод setFont() и передайте ему QFont следующим образом:\n"
"<p>\n"
"<table class=\"highlight tab-size js-file-line-container\" data-tab-size=\"8\" data-paste-markdown-skip>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC1\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>from</span> <span class=pl-v>PyQt5</span> <span class=pl-k>import</span> <span class=pl-v>QtWidgets</span>, <span class=pl-v>QtGui</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC2\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>from</span> <span class=pl-s1>mydesign</span> <span class=pl-k>import</span> <span class=pl-v>Ui_MainWindow</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC3\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>import</span> <span class=pl-s1>sys</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC5\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC6\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>class</span> <span class=pl-s1>mywindow</span>(<span class=pl-v>QtWidgets</span>.<span class=pl-v>QMainWindow</span>):</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC7\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC8\" class=\"blob-code blob-code-inner js-file-line\">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>):</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC9\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-en>super</span>(<span class=pl-s1>mywindow</span>, <span class=pl-s1>self</span>).<span class=pl-en>__init__</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC10\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span> <span class=pl-c1>=</span> <span class=pl-v>Ui_MainWindow</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC11\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-en>setupUi</span>(<span class=pl-s1>self</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC12\" class=\"blob-code blob-code-inner js-file-line\">        </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC13\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-s1>label</span>.<span class=pl-en>setFont</span>(</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC14\" class=\"blob-code blob-code-inner js-file-line\">            <span class=pl-v>QtGui</span>.<span class=pl-v>QFont</span>(<span class=pl-s>&#39;SansSerif&#39;</span>, <span class=pl-c1>30</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC15\" class=\"blob-code blob-code-inner js-file-line\">        ) <span class=pl-c># Изменение шрифта и размера</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC16\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC17\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC18\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>app</span> <span class=pl-c1>=</span> <span class=pl-v>QtWidgets</span>.<span class=pl-v>QApplication</span>([])</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC19\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>application</span> <span class=pl-c1>=</span> <span class=pl-en>mywindow</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC20\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>application</span>.<span class=pl-en>show</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC21\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-123-py-LC22\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>sys</span>.<span class=pl-en>exit</span>(<span class=pl-s1>app</span>.<span class=pl-en>exec</span>())</td>\n"
"      </tr>\n"
"\n"
"</table>\n"
"<p>\n"
"<h3>Меняем размер QLabel</h3>\n"
"<p>\n"
"Чтобы поменять размер QLabel, вам нужно указать его геометрию при помощи метода setGeometry(), вот так:\n"
"<p>\n"
"<table class=\"highlight tab-size js-file-line-container\" data-tab-size=\"8\" data-paste-markdown-skip>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC1\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>from</span> <span class=pl-v>PyQt5</span> <span class=pl-k>import</span> <span class=pl-v>QtWidgets</span>, <span class=pl-v>QtGui</span>,<span class=pl-v>QtCore</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC2\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>from</span> <span class=pl-s1>mydesign</span> <span class=pl-k>import</span> <span class=pl-v>Ui_MainWindow</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC3\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>import</span> <span class=pl-s1>sys</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC4\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC5\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>class</span> <span class=pl-s1>mywindow</span>(<span class=pl-v>QtWidgets</span>.<span class=pl-v>QMainWindow</span>):</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC6\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC7\" class=\"blob-code blob-code-inner js-file-line\">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>):</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC8\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-en>super</span>(<span class=pl-s1>mywindow</span>, <span class=pl-s1>self</span>).<span class=pl-en>__init__</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC9\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span> <span class=pl-c1>=</span> <span class=pl-v>Ui_MainWindow</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC10\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-en>setupUi</span>(<span class=pl-s1>self</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC11\" class=\"blob-code blob-code-inner js-file-line\">        </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC12\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-s1>label</span>.<span class=pl-en>setFont</span>(</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC13\" class=\"blob-code blob-code-inner js-file-line\">            <span class=pl-v>QtGui</span>.<span class=pl-v>QFont</span>(<span class=pl-s>&#39;SansSerif&#39;</span>, <span class=pl-c1>30</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC14\" class=\"blob-code blob-code-inner js-file-line\">        )</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC15\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC16\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-s1>label</span>.<span class=pl-en>setGeometry</span>(</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC17\" class=\"blob-code blob-code-inner js-file-line\">            <span class=pl-v>QtCore</span>.<span class=pl-v>QRect</span>(<span class=pl-c1>10</span>, <span class=pl-c1>10</span>, <span class=pl-c1>200</span>, <span class=pl-c1>200</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC18\" class=\"blob-code blob-code-inner js-file-line\">        ) <span class=pl-c># изменить геометрию ярлыка</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC19\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC20\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC21\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>app</span> <span class=pl-c1>=</span> <span class=pl-v>QtWidgets</span>.<span class=pl-v>QApplication</span>([])</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC22\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>application</span> <span class=pl-c1>=</span> <span class=pl-en>mywindow</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC23\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>application</span>.<span class=pl-en>show</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC24\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC25\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>sys</span>.<span class=pl-s1>exit</span>(<span class=pl-s1>app</span>.<span class=pl-en>exec</span>()</td>\n"
"      </tr>\n"
"</table>\n"
"<p>\n"
"<h3>Меняем текст в QLabel</h3>\n"
"<p>\n"
"Чтобы изменить текст в QLabel, вы можете использовать метод setText(), вот так:\n"
"<p>\n"
"<table class=\"highlight tab-size js-file-line-container\" data-tab-size=\"8\" data-paste-markdown-skip>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC1\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>from</span> <span class=pl-v>PyQt5</span> <span class=pl-k>import</span> <span class=pl-v>QtWidgets</span>, <span class=pl-v>QtGui</span>,<span class=pl-v>QtCore</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC2\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>from</span> <span class=pl-s1>qlabel</span> <span class=pl-k>import</span> <span class=pl-v>Ui_MainWindow</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC3\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>import</span> <span class=pl-s1>sys</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC4\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC5\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-k>class</span> <span class=pl-s1>mywindow</span>(<span class=pl-v>QtWidgets</span>.<span class=pl-v>QMainWindow</span>):</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC6\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC7\" class=\"blob-code blob-code-inner js-file-line\">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>):</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC8\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-en>super</span>(<span class=pl-s1>mywindow</span>, <span class=pl-s1>self</span>).<span class=pl-en>__init__</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC9\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span> <span class=pl-c1>=</span> <span class=pl-v>Ui_MainWindow</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC10\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-en>setupUi</span>(<span class=pl-s1>self</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC11\" class=\"blob-code blob-code-inner js-file-line\">        </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC12\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-s1>label</span>.<span class=pl-en>setFont</span>(</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC13\" class=\"blob-code blob-code-inner js-file-line\">            <span class=pl-v>QtGui</span>.<span class=pl-v>QFont</span>(<span class=pl-s>&#39;SansSerif&#39;</span>, <span class=pl-c1>30</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC14\" class=\"blob-code blob-code-inner js-file-line\">        )</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC15\" class=\"blob-code blob-code-inner js-file-line\">        </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC16\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-s1>label</span>.<span class=pl-en>setGeometry</span>(</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC17\" class=\"blob-code blob-code-inner js-file-line\">            <span class=pl-v>QtCore</span>.<span class=pl-v>QRect</span>(<span class=pl-c1>10</span>, <span class=pl-c1>10</span>, <span class=pl-c1>200</span>, <span class=pl-c1>200</span>)</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC18\" class=\"blob-code blob-code-inner js-file-line\">        )</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC19\" class=\"blob-code blob-code-inner js-file-line\">        </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC20\" class=\"blob-code blob-code-inner js-file-line\">        <span class=pl-s1>self</span>.<span class=pl-s1>ui</span>.<span class=pl-s1>label</span>.<span class=pl-en>setText</span>(<span class=pl-s>&quot;PyScripts&quot;</span>) <span class=pl-c># Меняем текст</span></td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC21\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC22\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC23\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>app</span> <span class=pl-c1>=</span> <span class=pl-v>QtWidgets</span>.<span class=pl-v>QApplication</span>([])</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC24\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>application</span> <span class=pl-c1>=</span> <span class=pl-en>mywindow</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC25\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>application</span>.<span class=pl-en>show</span>()</td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC26\" class=\"blob-code blob-code-inner js-file-line\"> </td>\n"
"      </tr>\n"
"      <tr>\n"
"        \n"
"        <td id=\"file-2-py-LC27\" class=\"blob-code blob-code-inner js-file-line\"><span class=pl-s1>sys</span>.<span class=pl-en>exit</span>(<span class=pl-s1>app</span>.<span class=pl-en>exec</span>())</td>\n"
"      </tr>\n"
"</table>\n"
"\n"
"\n"
"</body>\n"
"</html>"))