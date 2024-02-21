# encoding: UTF-8

from objectmaphelper import *

mainWindow_QQuickApplicationWindow = {"name": "mainWindow", "type": "QQuickApplicationWindow", "visible": True}
mainWindow_header_ToolBar = {"container": mainWindow_QQuickApplicationWindow, "id": "header", "type": "ToolBar", "unnamed": 1, "visible": True}
header_Remove_ToolButton = {"checkable": False, "container": mainWindow_header_ToolBar, "text": "Remove", "type": "ToolButton", "unnamed": 1, "visible": True}
mainWindow_addressBookView_AddressBookView = {"container": mainWindow_QQuickApplicationWindow, "id": "addressBookView", "type": "AddressBookView", "unnamed": 1, "visible": True}
addressBookView_Item = {"container": mainWindow_addressBookView_AddressBookView, "type": "Item", "unnamed": 1, "visible": True}
mainWindow_activeFocusControl_ToolBar = {"container": mainWindow_QQuickApplicationWindow, "id": "activeFocusControl", "type": "ToolBar", "unnamed": 1, "visible": True}
activeFocusControl_Add_ToolButton = {"checkable": False, "container": mainWindow_header_ToolBar, "text": "Add", "type": "ToolButton", "unnamed": 1, "visible": True}
mainWindow_addViewComponent_EditView = {"container": mainWindow_QQuickApplicationWindow, "id": "addViewComponent", "type": "EditView", "unnamed": 1, "visible": True}
addViewComponent_firstNameField_TextField = {"container": mainWindow_addViewComponent_EditView, "echoMode": 0, "id": "firstNameField", "type": "TextField", "unnamed": 1, "visible": True}
addViewComponent_lastNameField_TextField = {"container": mainWindow_addViewComponent_EditView, "echoMode": 0, "id": "lastNameField", "type": "TextField", "unnamed": 1, "visible": True}
addViewComponent_phoneNumberField_TextField = {"container": mainWindow_addViewComponent_EditView, "echoMode": 0, "id": "phoneNumberField", "type": "TextField", "unnamed": 1, "visible": True}
addViewComponent_emailAddressField_TextField = {"container": mainWindow_addViewComponent_EditView, "echoMode": 0, "id": "emailAddressField", "type": "TextField", "unnamed": 1, "visible": True}
header_Back_ToolButton = {"checkable": False, "container": mainWindow_header_ToolBar, "text": "Back", "type": "ToolButton", "unnamed": 1, "visible": True}
