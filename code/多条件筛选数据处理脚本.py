# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:26:21 2020

@author: gongdc
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import os
import pandas as pd
import time
import sys
import logging

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(935, 690)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(620, 60, 54, 12))
        self.label_5.setObjectName("label_5")
        self.textBrowserRizi = QtWidgets.QTextBrowser(Form)
        self.textBrowserRizi.setGeometry(QtCore.QRect(600, 80, 271, 381))
        self.textBrowserRizi.setObjectName("textBrowserRizi")
        self.pushButtonOut = QtWidgets.QPushButton(Form)
        self.pushButtonOut.setGeometry(QtCore.QRect(600, 470, 271, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButtonOut.setFont(font)
        self.pushButtonOut.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonOut.setObjectName("pushButtonOut")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 60, 61, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 570, 421, 111))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(480, 570, 401, 111))
        self.textEdit_2.setObjectName("textEdit_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(271, 30, 133, 47))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_hebing = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_hebing.setObjectName("checkBox_hebing")
        self.verticalLayout.addWidget(self.checkBox_hebing)
        self.checkBox_guanlian = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_guanlian.setObjectName("checkBox_guanlian")
        self.verticalLayout.addWidget(self.checkBox_guanlian)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 30, 73, 40))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButtonfenzu = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButtonfenzu.setObjectName("radioButtonfenzu")
        self.verticalLayout_3.addWidget(self.radioButtonfenzu)
        self.radioButton_toushi = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_toushi.setObjectName("radioButton_toushi")
        self.verticalLayout_3.addWidget(self.radioButton_toushi)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(61, 81, 512, 461))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonYuanshi = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonYuanshi.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonYuanshi.setFont(font)
        self.pushButtonYuanshi.setObjectName("pushButtonYuanshi")
        self.verticalLayout_2.addWidget(self.pushButtonYuanshi)
        self.pushButtonZidian = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonZidian.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonZidian.setFont(font)
        self.pushButtonZidian.setObjectName("pushButtonZidian")
        self.verticalLayout_2.addWidget(self.pushButtonZidian)
        self.pushButtonJieguo = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonJieguo.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonJieguo.setFont(font)
        self.pushButtonJieguo.setObjectName("pushButtonJieguo")
        self.verticalLayout_2.addWidget(self.pushButtonJieguo)
        self.pushButtonJieguoming = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonJieguoming.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButtonJieguoming.setFont(font)
        self.pushButtonJieguoming.setObjectName("pushButtonJieguoming")
        self.verticalLayout_2.addWidget(self.pushButtonJieguoming)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditYuanshi = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditYuanshi.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditYuanshi.setObjectName("lineEditYuanshi")
        self.verticalLayout_4.addWidget(self.lineEditYuanshi)
        self.lineEditZidian = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditZidian.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditZidian.setObjectName("lineEditZidian")
        self.verticalLayout_4.addWidget(self.lineEditZidian)
        self.lineEditJieguo = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditJieguo.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditJieguo.setObjectName("lineEditJieguo")
        self.verticalLayout_4.addWidget(self.lineEditJieguo)
        self.lineEditJieguoming = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditJieguoming.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditJieguoming.setObjectName("lineEditJieguoming")
        self.verticalLayout_4.addWidget(self.lineEditJieguoming)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 170, 0);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEditcheck = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditcheck.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditcheck.setObjectName("lineEditcheck")
        self.gridLayout.addWidget(self.lineEditcheck, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 170, 0);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEditcondition = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditcondition.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditcondition.setObjectName("lineEditcondition")
        self.gridLayout.addWidget(self.lineEditcondition, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 170, 0);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEditHang = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditHang.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditHang.setObjectName("lineEditHang")
        self.gridLayout.addWidget(self.lineEditHang, 2, 1, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 2, 1)
        self.lineEditLie = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditLie.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditLie.setObjectName("lineEditLie")
        self.gridLayout.addWidget(self.lineEditLie, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEditJisuan = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditJisuan.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditJisuan.setObjectName("lineEditJisuan")
        self.gridLayout.addWidget(self.lineEditJisuan, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.lineEditJisF = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditJisF.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEditJisF.setObjectName("lineEditJisF")
        self.gridLayout.addWidget(self.lineEditJisF, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据(透视)处理分析工具(By:可以叫我才哥)"))
        self.label_5.setText(_translate("Form", "操作日志"))
        self.pushButtonOut.setText(_translate("Form", "数据处理并导出"))
        self.label_6.setText(_translate("Form", "工作设置台"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">分组统计及数据透视 选择逻辑</span>：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、大部分情况下 分组统计即可完成操作（默认采取分组统计）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、数据透视的情况限于 透视列 非统计是类型字段</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3、筛选条件支持‘==’，‘!=’,‘&gt;=’,‘&lt;=’，常见聚合方法见右侧说明</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4、以上黄色部分为统计 计算，支持输入多个参数，参数之间用英文\'/\'隔开</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5、行列 与 计算字段 不能重复，若需要请采用替换的字段</p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">常见计算字段方法说明：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">count    计数            min、max           最小或最大值</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sum      求和            prod               乘积</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mean     平均            first/last         第一个或最后一个值</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">median   算术中位数      pd.Series.nunique  非重复计数</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">std/var  标准差和方差</p></body></html>"))
        self.checkBox_hebing.setText(_translate("Form", "原始数据合并后导出"))
        self.checkBox_guanlian.setText(_translate("Form", "关联字典后数据导出"))
        self.radioButtonfenzu.setText(_translate("Form", "分组统计"))
        self.radioButton_toushi.setText(_translate("Form", "数据透视"))
        self.pushButtonYuanshi.setText(_translate("Form", "原始数据所在文件夹"))
        self.pushButtonZidian.setText(_translate("Form", "关联字典所在文件夹"))
        self.pushButtonJieguo.setText(_translate("Form", "结果数据导出文件夹"))
        self.pushButtonJieguoming.setText(_translate("Form", "结果数据导出文件名"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"center\">原始数据筛选字段</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">原始数据筛选条件</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">数据透视表 行 列表</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffaa00;\">数据透视表 列 列表</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffaa00;\">需要计算的字段列表</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffaa00;\">需要计算的字段方法</span></p></body></html>"))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__()
        self.setupUi(self)
        log = '程序启动完成,目前支持csv(含zip压缩文件)、xlsx和xls文件类型进行横向合表和纵向合表\
        \n使用流程：\
        \n1、先选择原始数据文件目录、需要使用的字典目录和需要导出的文件信息;\
        \n2、参考excel的数据透视表，设置你想要展示的行列数据字段及计算字段和方法;\
        \n3、点击数据处理并导出 即可获得 计算结果文件（默认以xlsx文件存在）'
        logging.info(log)
        self.textBrowserRizi.append(log)
        self.pushButtonYuanshi.clicked.connect(self.openinFile)
        self.pushButtonZidian.clicked.connect(self.openoutFile)
        self.pushButtonJieguo.clicked.connect(self.openjieguoFile)

        self.pushButtonOut.clicked.connect(self.piv_data)  # 获取并导出数据

    def openinFile(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.lineEditYuanshi.setText(str(get_directory_path))
        log = '需要合并的文件目录已选择'
        logging.info(log)
        self.textBrowserRizi.append(log)

    def openoutFile(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.lineEditZidian.setText(str(get_directory_path))
        log = '需要存放合并后的文件目录已选择'
        logging.info(log)
        self.textBrowserRizi.append(log)

    def openjieguoFile(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              "C:/")
        self.lineEditJieguo.setText(str(get_directory_path))
        log = '需要存放计算后的文件目录已选择'
        logging.info(log)
        self.textBrowserRizi.append(log)

    #合并原始数据
    def merge_data(self):
        log = '正在合并原始数据ing'
        logging.info(log)
        self.textBrowserRizi.append(log)
        location = self.lineEditYuanshi.text()
        fileList = []
        n = 0
        start_time = time.perf_counter()
        for fileName in os.walk(location):
            for table in fileName[2]:
                path = fileName[0] + '/' + table
                filetype = os.path.splitext(path)[1]
                if filetype == '.csv'or filetype == '.zip':
                    Li = pd.read_csv(path, header=0)
                    if len(self.lineEditcheck.text())!=0:
                        try :
                            checkli = self.lineEditcheck.text().split('/')
                            conditionli = self.lineEditcondition.text().split('/')
                            for inum in range(len(checkli)):
                                s = f"Li['{checkli[0]}']{conditionli[0]}"
                                Li = Li[eval(s)]
                            fileList.append(Li)
                        except :
                            log = '<font color=\"#FF0000\">是不是筛选及条件字段填写有误？</font>'
                            logging.info('是不是筛选及条件字段填写有误？')
                            self.textBrowserRizi.append(log)
                    else:
                        fileList.append(Li)                             
                elif filetype == '.xlsx' or filetype == '.xls':
                    Li = pd.read_excel(path, header=0)
                    if len(self.lineEditcheck.text())!=0:
                        try :
                            checkli = self.lineEditcheck.text().split('/')
                            conditionli = self.lineEditcondition.text().split('/')
                            for inum in range(len(checkli)):
                                s = f"Li['{checkli[0]}']{conditionli[0]}"
                                Li = Li[eval(s)]
                            fileList.append(Li)
                        except :
                            log = '<font color=\"#FF0000\">是不是筛选及条件字段填写有误？</font>'
                            logging.info('是不是筛选及条件字段填写有误？')
                            self.textBrowserRizi.append(log)
                    else :
                        fileList.append(Li)
                else:
                    log = '<font color=\"#FF0000\">不是支持的文件类型,该工具暂时只支持csv、xlsx和xls文件类型</font>'
                    logging.info('不是支持的文件类型,该工具暂时只支持csv、xlsx和xls文件类型')
                    self.textBrowserRizi.append(log)
                n = n+1
                log = f'第{n}个表已经读取'
                logging.info(log)
                self.textBrowserRizi.append(log)
            log = '正在合并全部数据'
            logging.info(log)
            self.textBrowserRizi.append(log)
            if len(fileList)>1:
                data_result = pd.concat(fileList, ignore_index=True)
            else:
                data_result = fileList[0]
            data_result['@timestamp'] = pd.to_datetime(data_result["@timestamp"]).dt.strftime('%Y-%m-%d')
            lenth = len(data_result.index)
            use_time = time.perf_counter()
            log = f'<font color=\"#228B22\">数据合并共{lenth}条,合计用时{use_time-start_time:0.2f}秒</font>'
            logging.info(f'数据合并共{lenth}条,合计用时{use_time-start_time:0.2f}秒')
            self.textBrowserRizi.append(log)
            if self.checkBox_hebing.isChecked():
                try:
                    out_path = f'{self.lineEditJieguo.text()}/合并后数据.xlsx'
                    data_result.to_excel(out_path,index =0)
                except:
                    out_path = f'{self.lineEditJieguo.text()}/合并后数据.csv'
                    data_result.to_csv(out_path,index=0) 
                    
                use_time = time.perf_counter()                    
                log = f'<font color=\"#228B22\">合并数据导出完成,合计用时{use_time-start_time:0.2f}秒</font>'
                logging.info(f'合并数据导出完成,合计用时{use_time-start_time:0.2f}秒')
                self.textBrowserRizi.append(log)
            mergedata = data_result
            return mergedata

    # 关联字典表
    def concat_data(self):
        data = self.merge_data()
        log = '正在关联字典表ing'
        logging.info(log)
        self.textBrowserRizi.append(log)
        location = self.lineEditZidian.text()
        fileList = []
        n = 0
        start_time = time.perf_counter()
        for fileName in os.walk(location):
            for table in fileName[2]:
                path = fileName[0] + '/' + table
                filetype = os.path.splitext(path)[1]
                if filetype == '.csv'or filetype == '.zip':
                    Li = pd.read_csv(path, header=0)
                    fileList.append(Li)
                elif filetype == '.xlsx' or filetype == '.xls':
                    Li = pd.read_excel(path, header=0)
                    fileList.append(Li)
                else:
                    log = '<font color=\"#FF0000\">不是支持的文件类型,该工具暂时只支持csv、xlsx和xls文件类型</font>'
                    logging.info('不是支持的文件类型,该工具暂时只支持csv、xlsx和xls文件类型')
                    self.textBrowserRizi.append(log)
                n = n+1
                log = f'第{n}个字典表已经记录'
                logging.info(log)
                self.textBrowserRizi.append(log)
            log = '正在关联字典表'
            logging.info(log)
            self.textBrowserRizi.append(log)
            for i in range(0,len(fileList)):
                data = pd.merge(data,fileList[i],how = 'left')
            
            use_time = time.perf_counter()
            log = f'<font color=\"#228B22\">字典关联完成,合计用时{use_time-start_time:0.2f}秒</font>'
            logging.info(f'字典关联完成,合计用时{use_time-start_time:0.2f}秒')
            self.textBrowserRizi.append(log) 
               
            if self.checkBox_guanlian.isChecked():
                try:
                    out_path = f'{self.lineEditJieguo.text()}/合并关联后数据.xlsx'
                    data.to_excel(out_path,index = 0)
                except:
                    out_path = f'{self.lineEditJieguo.text()}/合并关联后数据.csv'
                    data.to_csv(out_path,index = 0)  
                    
                use_time = time.perf_counter()
                log = f'<font color=\"#228B22\">字典关联导出完成,合计用时{use_time-start_time:0.2f}秒</font>'
                logging.info(f'字典关联导出完成,合计用时{use_time-start_time:0.2f}秒')
                self.textBrowserRizi.append(log)

            concat_data = data
            return concat_data

    #数据透视处理
    def piv_data(self):
        if len(self.lineEditZidian.text())==0:
            df = self.merge_data()
        else:
            df = self.concat_data()
            
        log = '正在进行数据运算...'
        logging.info(log)
        self.textBrowserRizi.append(log)
        hang = self.lineEditHang.text().split(',')
        lie = self.lineEditLie.text().split(',') if len(self.lineEditLie.text())!=0 else []
        ziduan = self.lineEditJisuan.text().split(',')
        fangfa = self.lineEditJisF.text().split(',')
        start_time = time.perf_counter()
        
        try:
            if self.radioButton_toushi.isChecked():
                # li = []
                # for i in range(len(fangfa)):
                #     if fangfa[i] == 'pd.Series.nunique':
                #         li.append(eval(fangfa[i]))
                #     else:
                #         li.append(fangfa[i])  
                dic = {}
                for i in range(len(fangfa)):
                    if fangfa[i] == 'pd.Series.nunique':
                        dic[ziduan[i]] = eval(fangfa[i])
                    else:
                        dic[ziduan[i]] = fangfa[i]   
                result = pd.pivot_table(df, values=ziduan,
                              aggfunc=dic, 
                              columns=lie,
                              index=hang,
                              ).reset_index()
            else:
                # dic = {key:values for key,values in zip(ziduan,fangfa)}
                dic = {}
                for i in range(len(fangfa)):
                    if fangfa[i] == 'pd.Series.nunique':
                        dic[ziduan[i]] = eval(fangfa[i])
                    else:
                        dic[ziduan[i]] = fangfa[i]   
                result = df.groupby(hang).agg(dic).reset_index()  
            
            use_time = time.perf_counter()  
            log = f'<font color=\"#228B22\">数据运算完成,合计用时{use_time-start_time:0.2f}秒</font>'
            logging.info(f'数据运算完成,合计用时{use_time-start_time:0.2f}秒')
            self.textBrowserRizi.append(log)   
                                          
        except:
            log = '<font color=\"#FF0000\">是不是行列或计算字段填写有误？</font>'
            logging.info('是不是行列或计算字段填写有误？')
            self.textBrowserRizi.append(log)                                    
                  
        try:
            out_path = f'{self.lineEditJieguo.text()}/{self.lineEditJieguoming.text()}.xlsx'
            result.to_excel(out_path,index = 0)
        except:
            out_path = f'{self.lineEditJieguo.text()}/{self.lineEditJieguoming.text()}.csv'
            result.to_csv(out_path,index = 0)
            
        use_time = time.perf_counter()            
        log = f'<font color=\"#228B22\">计算数据导出完成,合计用时{use_time-start_time:0.2f}秒</font>'
        logging.info(f'计算数据导出完成,合计用时{use_time-start_time:0.2f}秒')
        self.textBrowserRizi.append(log)



if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO,
                    format = '%(asctime)s-%(levelname)s:%(message)s')
    logging.info('程序启动中...')
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出
    sys.exit(app.exec_())
