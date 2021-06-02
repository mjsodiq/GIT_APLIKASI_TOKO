import sys
from PyQt5 import QtGui, QtWidgets


def TabStyleSheet1(Resolusi):
    # Untuk Tab
    if Resolusi == '1280x720':
        styleSheets = ''
        pass
    elif Resolusi == '2880x1620':
        styleSheets = "QTabBar::tab {height: 30; background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); border: 2px solid #C4C4C3; border-bottom-color: #C2C7CB; border-top-left-radius: 7px; border-top-right-radius: 7px; min-width: 0ex; padding: 0px; margin: 0; padding-left: 20px; padding-right: 20px; padding-top: 10px; padding-bottom: 10px}" \
                      "QTabBar::tab:selected,QTabBar::tab:hover {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa)}" \
                      "QTabBar::tab:selected {border-color: #9B9B9B; border-bottom-color: #C2C7CB;}" \
                      "QTabBar::tab:!selected {margin-top: 2px;}" \
                      "QTabBar::tab:selected {margin-left: -4px; margin-right: -1px;}" \
                      "QTabBar::tab:first:selected {margin-left: 0;}" \
                      "QTabBar::tab:last:selected {margin-right: 0;}" \
                      "QTabBar::tab:only-one {margin: 0; padding-left: 20px; padding-right: 20px; padding-top: 10px; padding-bottom: 10px}"
    else:
        styleSheets = ''
        pass
    return str(styleSheets)


def TabStyleSheet2(Resolusi):
    if Resolusi == '1280x720':
        styleSheets = ''
        pass
    elif Resolusi == '2880x1620':
        styleSheets = "QTabBar::tab {height: 30; background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); border: 1px solid #C4C4C3; border-bottom-color: #C2C7CB; border-top-left-radius: 7px; border-top-right-radius: 7px; min-width: 0ex; padding: 0px; margin: 0; padding-left: 20px; padding-right: 20px; padding-top: 10px; padding-bottom: 5px}" \
                      "QTabBar::tab:selected,QTabBar::tab:hover {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FCFCFC, stop: 0.4 #FCFCFC, stop: 0.5 #FCFCFC, stop: 1.0 #FCFCFC)}" \
                      "QTabBar::tab:selected {border-color: #ABABAB; border-bottom-color: #FCFCFC; border-bottom: 4px solid #FCFCFC}" \
                      "QTabBar::tab:!selected {margin-top: 4px;}" \
                      "QTabBar::tab:selected {margin-left: -2px; margin-right: -2px; margin-top: 1px; margin-bottom: 3px}" \
                      "QTabBar::tab:first:selected {margin-left: 0;}" \
                      "QTabBar::tab:last:selected {margin-right: 0;}" \
                      "QTabBar::tab:only-one {margin: 0; padding-left: 20px; padding-right: 20px; padding-top: 10px; padding-bottom: 10px; margin-top: 1px; margin-bottom: 3px}"
    else:
        styleSheets = ''
        pass
    return str(styleSheets)


def TabStyleSheet3(Resolusi):
    if Resolusi == '1280x720':
        styleSheets = ''
        pass
    elif Resolusi == '2880x1620':
        styleSheets = '''
                        QTabBar::tab {
                                    height: 25; 
                                    background: 
                                    qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); 
                                    border: 1px solid #C4C4C3; 
                                    border-bottom-color: #C2C7CB; 
                                    border-top-left-radius: 7px; 
                                    border-top-right-radius: 7px; 
                                    min-width: 0ex; 
                                    margin: 0; 
                                    padding: 0px; 
                                    padding-left: 20px; 
                                    padding-right: 20px; 
                                    padding-top: 10px; 
                                    padding-bottom: 5px;
                                    }
                                
                        QTabBar::tab:selected,QTabBar::tab:hover {
                                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FCFCFC, stop: 0.4 #FCFCFC, stop: 0.5 #FCFCFC, stop: 1.0 #FCFCFC)
                                    }
                                
                        QTabBar::tab:selected {
                                    border-color: #ABABAB; 
                                    border-bottom-color: #FCFCFC; 
                                    border-bottom: 4px solid #FCFCFC
                                    }
                                
                        QTabBar::tab:!selected {
                                    margin-top: 4px;
                                    }
                                
                        QTabBar::tab:selected {
                                    margin-left: -2px; 
                                    margin-right: -2px; 
                                    margin-top: 1px; 
                                    margin-bottom: 3px
                                    }
                                
                        QTabBar::tab:first:selected {
                                    margin-left: 0;
                                    }
                                
                        QTabBar::tab:last:selected {
                                    margin-right: 0;
                                    }
                                
                        QTabBar::tab:only-one {
                                    margin-left: 0px;
                                    margin-right: 0px;
                                    margin-top: 1px;
                                    margin-bottom: 3px;
                                    
                                    padding-left: 20px; 
                                    padding-right: 20px; 
                                    padding-top: 10px; 
                                    padding-bottom: 5px
                                    }
                        '''
    else:
        styleSheets = ''
        pass
    return str(styleSheets)


def TabStyleSheet4(Resolusi):
    if Resolusi == '1280x720':
        styleSheets = '''
                        QTabBar::tab {
                                        height: 15; 
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); 
                                        border: 1px solid #C4C4C3; 
                                        border-bottom-color: #C2C7CB; 
                                        border-top-left-radius: 3px; 
                                        border-top-right-radius: 3px; 
                                        min-width: 0ex; 
                                        margin: 0; 
                                        padding: 0px; 
                                        padding-left: 8px; 
                                        padding-right: 5px; 
                                        padding-top: 8px; 
                                        padding-bottom: 5px;
                                        }

                        QTabBar::tab:selected,QTabBar::tab:hover {
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FCFCFC, stop: 0.4 #FCFCFC, stop: 0.5 #FCFCFC, stop: 1.0 #FCFCFC);
                                        }

                        QTabBar::tab:selected {
                                        border-color: #ABABAB; 
                                        border-bottom-color: #FCFCFC; 
                                        border-bottom: 3px solid #FCFCFC
                                        }

                        QTabBar::tab:!selected {
                                        margin-top: 3px;
                                        }

                        QTabBar::tab:selected {
                                        margin-left: -2px; 
                                        margin-right: -2px; 
                                        margin-top: 1px; 
                                        margin-bottom: 1px
                                        }

                        QTabBar::tab:first:selected {
                                        margin-left: 0;
                                        }
                        
                        QTabBar::tab:first:!selected {
                                        margin-left: 0;
                                        padding-left: 6px;
                                        }

                        QTabBar::tab:last:selected {
                                        margin-right: 0;
                                        }

                        QTabBar::tab:only-one {
                                        margin-left: 0px;
                                        margin-right: 0px;
                                        margin-top: 1px;
                                        margin-bottom: 1px;

                                        padding-left: 8px; 
                                        padding-right: 5px; 
                                        padding-top: 8px; 
                                        padding-bottom: 5px
                                        }
                        '''
    elif Resolusi == '2880x1620':
        styleSheets = '''
                        QTabBar::tab {
                                        height: 50; 
                                        background: 
                                        qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); 
                                        border: 1px solid #C4C4C3; 
                                        border-bottom-color: #C2C7CB; 
                                        border-top-left-radius: 7px; 
                                        border-top-right-radius: 7px; 
                                        min-width: 0ex; 
                                        margin: 0; 
                                        padding: 0px; 
                                        padding-left: 20px; 
                                        padding-right: 20px; 
                                        padding-top: 10px; 
                                        padding-bottom: 5px;
                                        }
    
                        QTabBar::tab:selected,QTabBar::tab:hover {
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FCFCFC, stop: 0.4 #FCFCFC, stop: 0.5 #FCFCFC, stop: 1.0 #FCFCFC)
                                        }
    
                        QTabBar::tab:selected {
                                        border-color: #ABABAB; 
                                        border-bottom-color: #FCFCFC; 
                                        border-bottom: 4px solid #FCFCFC
                                        }
    
                        QTabBar::tab:!selected {
                                        margin-top: 4px;
                                        }
    
                        QTabBar::tab:selected {
                                        margin-left: -2px; 
                                        margin-right: -2px; 
                                        margin-top: 1px; 
                                        margin-bottom: 3px
                                        }
    
                        QTabBar::tab:first:selected {
                                        margin-left: 0;
                                        }
    
                        QTabBar::tab:last:selected {
                                        margin-right: 0;
                                        }
    
                        QTabBar::tab:only-one {
                                        margin-left: 0px;
                                        margin-right: 0px;
                                        margin-top: 1px;
                                        margin-bottom: 3px;
        
                                        padding-left: 20px; 
                                        padding-right: 20px; 
                                        padding-top: 10px; 
                                        padding-bottom: 5px
                                        }
                        '''
    else:
        styleSheets = ''
        pass
    return str(styleSheets)


def TabStyleSheet5(Resolusi):
    if Resolusi == '1280x720':
        styleSheets = '''
                            QTabBar::tab {
                                            height: 10; 
                                            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); 
                                            border: 1px solid #C4C4C3; 
                                            border-bottom-color: #C2C7CB; 
                                            border-top-left-radius: 3px; 
                                            border-top-right-radius: 3px; 
                                            min-width: 0ex; 
                                            margin: 0; 
                                            padding: 0px; 
                                            padding-left: 8px; 
                                            padding-right: 5px; 
                                            padding-top: 8px; 
                                            padding-bottom: 5px;
                                            }
    
                            QTabBar::tab:selected,QTabBar::tab:hover {
                                            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FCFCFC, stop: 0.4 #FCFCFC, stop: 0.5 #FCFCFC, stop: 1.0 #FCFCFC);
                                            }
    
                            QTabBar::tab:selected {
                                            border-color: #ABABAB; 
                                            border-bottom-color: #FCFCFC; 
                                            border-bottom: 3px solid #FCFCFC
                                            }
    
                            QTabBar::tab:!selected {
                                            margin-top: 3px;
                                            }
    
                            QTabBar::tab:selected {
                                            margin-left: -2px; 
                                            margin-right: -2px; 
                                            margin-top: 1px; 
                                            margin-bottom: 1px
                                            }
    
                            QTabBar::tab:first:selected {
                                            margin-left: 0;
                                            }
    
                            QTabBar::tab:last:selected {
                                            margin-right: 0;
                                            }
    
                            QTabBar::tab:only-one {
                                            margin-left: 0px;
                                            margin-right: 0px;
                                            margin-top: 1px;
                                            margin-bottom: 1px;
    
                                            padding-left: 8px; 
                                            padding-right: 5px; 
                                            padding-top: 8px; 
                                            padding-bottom: 5px
                                            }
                            '''
    elif Resolusi == '2880x1620':
        styleSheets = ''
        pass
    else:
        styleSheets = ''
        pass
    return str(styleSheets)


# BUTTON STYLESHEETS----------------------------------------------------------------------------------------------------
def ButtonStyleSheets1(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = """
                        QPushButton {
                                color: #ffffff;
                                border: 2px solid #052;
                                border-radius: 5px;
                                border-style: outset;
                                border-color: #bbbbbb;
                                font: bold 11px;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #002211, stop: 0.5 #006633, stop: 0.5 #006633, stop: 1.0 #002211);
                                padding: 2px;
                                }
    
                        QPushButton:hover {
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #002211, stop: 0.5 #559977, stop: 0.5 #559977, stop: 1.0 #002211);
                                font: bold 11px;
                                color: #ffffff
                                }
    
                        QPushButton:pressed {
                                border-style: inset;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #004422, stop: 0.5 #004422, stop: 0.5 #004422, stop: 1.0 #004422);
                                font: bold 11px;
                                color: #ffffff
                                }
                        """
        pass
    elif Resolusi == '2880x1620':
        StyleSheets = """
                        QPushButton {
                                color: #ffffff;
                                border: 2px solid #052;
                                border-radius: 10px;
                                border-style: outset;
                                border-color: #bbbbbb;
                                font: bold 22px;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #002211, stop: 0.5 #006633, stop: 0.5 #006633, stop: 1.0 #002211);
                                padding: 5px;
                                }
    
                        QPushButton:hover {
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #002211, stop: 0.5 #559977, stop: 0.5 #559977, stop: 1.0 #002211);
                                font: bold 22px;
                                color: #ffffff
                                }
    
                        QPushButton:pressed {
                                border-style: inset;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #004422, stop: 0.5 #004422, stop: 0.5 #004422, stop: 1.0 #004422);
                                font: bold 22px;
                                color: #ffffff
                                }
                        """
    else:
        StyleSheets = ''
        pass
    return StyleSheets


def ButtonStyleSheets2(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = """
                                QPushButton {
                                        color: white;
                                        font: bold;
                                        border: 2px solid #052;
                                        border-radius: 5px;
                                        border-style: outset;
                                        border-color: #bbbbbb;
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000000, stop: 0.6 #000000, stop: 0.6 #000000, stop: 1.0 #000000);
                                        padding-top: 5px;
                                        padding-bottom: 5px;
                                        padding-left: 5px;
                                        padding-right: 5px
                                        }

                                QPushButton:hover {
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BF3C30, stop: 0.5 #BF3C30, stop: 0.5 #BF3C30, stop: 1.0 #BF3C30);
                                        color: #ffffff;
                                        font: bold;
                                        }

                                QPushButton:pressed {
                                        border-style: inset;
                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000000, stop: 0.5 #000000, stop: 0.5 #000000, stop: 1.0 #000000);
                                        color: #ffffff
                                        }
                                """
    elif Resolusi == '2880x1620':
        StyleSheets = """
                        QPushButton {
                                color: white;
                                font: bold;
                                border: 2px solid #052;
                                border-radius: 10px;
                                border-style: outset;
                                border-color: #bbbbbb;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000000, stop: 0.6 #000000, stop: 0.6 #000000, stop: 1.0 #000000);
                                padding-top: 5px;
                                padding-bottom: 5px;
                                padding-left: 5px;
                                padding-right: 5px
                                }
    
                        QPushButton:hover {
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #BF3C30, stop: 0.5 #BF3C30, stop: 0.5 #BF3C30, stop: 1.0 #BF3C30);
                                color: #ffffff;
                                font: bold;
                                }
    
                        QPushButton:pressed {
                                border-style: inset;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000000, stop: 0.5 #000000, stop: 0.5 #000000, stop: 1.0 #000000);
                                color: #ffffff
                                }
                        """
    else:
        StyleSheets = ''
        pass
    return StyleSheets


def ButtonStyleSheets3(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = """
                        QPushButton {
                                color: #ffffff;
                                border: 2px solid #052;
                                border-radius: 5px;
                                border-style: outset;
                                border-color: #bbbbbb;
                                font: bold 11px;
                                background: #000000;
                                padding: 2px;
                                }
    
                        QPushButton:hover {
                                background: #009900;
                                font: bold 11px;
                                color: #ffffff
                                }
    
                        QPushButton:pressed {
                                border-style: inset;
                                background: #004422;
                                font: bold 11px;
                                color: #ffffff
                                }
                        """
        pass
    elif Resolusi == '2880x1620':
        StyleSheets = """
                        QPushButton {
                                color: #ffffff;
                                border: 2px solid #052;
                                border-radius: 10px;
                                border-style: outset;
                                border-color: #bbbbbb;
                                font: bold 22px;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #002211, stop: 0.5 #006633, stop: 0.5 #006633, stop: 1.0 #002211);
                                padding: 5px;
                                }
    
                        QPushButton:hover {
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #002211, stop: 0.5 #559977, stop: 0.5 #559977, stop: 1.0 #002211);
                                font: bold 22px;
                                color: #ffffff
                                }
    
                        QPushButton:pressed {
                                border-style: inset;
                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #004422, stop: 0.5 #004422, stop: 0.5 #004422, stop: 1.0 #004422);
                                font: bold 22px;
                                color: #ffffff
                                }
                        """
    else:
        StyleSheets = ''
        pass
    return StyleSheets


# LINEEDIT STYLESHEETS--------------------------------------------------------------------------------------------------
def LineEditStyleSheets1(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = ''
        pass
    elif Resolusi == '2880x1620':
        StyleSheets = '''
                    QLineEdit
                        {
                        background-color: #ffffff;
                        border: 1px solid #052;
                        border-color: #74a78e;
                        border-radius: 5px;
                        padding: 2px;
                        }
    
                        '''
    else:
        StyleSheets = ''
        pass
    return StyleSheets


# FRAME STYLESHEETS-----------------------------------------------------------------------------------------------------
def FrameStyleSheets1(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = '''
                        QFrame #Frame1,#frame_2, #frame_3, #frame_4
                        {
                        background-color: #DFE6E3;
                        border: 1px solid #052;
                        border-color: #74a78e;
                        border-radius: 5;
                        padding: 2px;}
    
                        '''
    elif Resolusi == '2880x1620':
        StyleSheets = '''
                        QFrame #Frame1 {
                        background-color: #DFE6E3;
                        border: 1px solid #052;
                        border-color: #74a78e;
                        border-radius: 5;
                        padding: 2px;}
    
                        '''
    else:
        StyleSheets = ''
        pass
    return StyleSheets


def FrameStyleSheets2(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = '''
                                    QFrame 
                                    #page1_dsi_Frame_2, 
                                    #frame_2,
                                    #page1_ht_frame_2, 
                                    #page1_ht_Frame_3,
                                    #page1_ht_Frame_4,
                                    #page1_ht_Frame_5 
                                    {
                                    border: 1px solid #052;
                                    border-color: #74a78e;
                                    border-radius: 2;
                                    padding: 2px;
                                    }

                                    '''
    elif Resolusi == '2880x1620':
        StyleSheets = '''
                            QFrame 
                            #page1_dsi_Frame_2, 
                            #page1_ht_frame_2, 
                            #page1_ht_Frame_3,
                            #page1_ht_Frame_4,
                            #page1_ht_Frame_5 
                            {
                            border: 1px solid #052;
                            border-color: #74a78e;
                            border-radius: 2;
                            padding: 2px;
                            }
    
                            '''
    else:
        StyleSheets = ''
        pass
    return StyleSheets


def FrameStyleSheets3(Resolusi):
    if Resolusi == '1280x720':
        StyleSheets = '''
                                    QFrame 
                                    #page1_dsi_Frame_2, 
                                    #frame_2,
                                    #frame_4,
                                    #page1_ht_frame_2, 
                                    #page1_ht_Frame_3,
                                    #page1_ht_Frame_4,
                                    #page1_ht_Frame_5 
                                    {
                                    background-color: #DFE6E3;
                                    border: 1px solid #052;
                                    border-color: #74a78e;
                                    border-radius: 0;
                                    padding: 1px;
                                    }

                                    '''
    elif Resolusi == '2880x1620':
        StyleSheets = '''
                            QFrame 
                            #page1_dsi_Frame_2, 
                            #page1_ht_frame_2, 
                            #page1_ht_Frame_3,
                            #page1_ht_Frame_4,
                            #page1_ht_Frame_5 
                            {
                            border: 1px solid #052;
                            border-color: #74a78e;
                            border-radius: 2;
                            padding: 2px;
                            }
    
                            '''
    else:
        StyleSheets = ''
        pass
    return StyleSheets

