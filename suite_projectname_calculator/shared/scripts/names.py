# encoding: UTF-8

from objectmaphelper import *

CalculatorApp_Window     = {"type": "QQuickView", "unnamed": 1, "visible": True}
ONE_BUTTON               = {"container": CalculatorApp_Window, "text": 1, "type": "Text", "unnamed": 1, "visible": True}
PLUS_BUTTON              = {"container": CalculatorApp_Window, "text": "+", "type": "Text", "unnamed": 1, "visible": True}
TWO_BUTTON               = {"container": CalculatorApp_Window, "text": 2, "type": "Text", "unnamed": 1, "visible": True}
o_Text_2                 = {"container": CalculatorApp_Window, "text": "=", "type": "Text", "unnamed": 1, "visible": True}
c_Text                   = {"container": CalculatorApp_Window, "text": "C", "type": "Text", "unnamed": 1, "visible": True}
o5_Text                  = {"container": CalculatorApp_Window, "text": 5, "type": "Text", "unnamed": 1, "visible": True}
listView_ListView        = {"container": CalculatorApp_Window, "id": "listView", "type": "ListView", "unnamed": 1, "visible": True}
listView_Item            = {"container": listView_ListView, "index": 2, "type": "Item", "unnamed": 1, "visible": True}
o163_Text                = {"container": listView_Item, "text": 163, "type": "Text", "unnamed": 1, "visible": True}
