# encoding: UTF-8

from objectmaphelper import *

mainWindow_QQuickApplicationWindow = {"name": "mainWindow", "type": "QQuickApplicationWindow", "visible": True}
mainWindow_header_ToolBar = {"container": mainWindow_QQuickApplicationWindow, "id": "header", "type": "ToolBar", "unnamed": 1, "visible": True}
header_Remove_ToolButton = {"checkable": False, "container": mainWindow_header_ToolBar, "text": "Remove", "type": "ToolButton", "unnamed": 1, "visible": True}
mainWindow_addressBookView_AddressBookView = {"container": mainWindow_QQuickApplicationWindow, "id": "addressBookView", "type": "AddressBookView", "unnamed": 1, "visible": True}
addressBookView_Item = {"container": mainWindow_addressBookView_AddressBookView, "type": "Item", "unnamed": 1, "visible": True}