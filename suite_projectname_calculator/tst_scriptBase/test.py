# -*- coding: utf-8 -*-

import names

def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o1_Text))
    mouseClick(waitForObject(names.o_Text))
    mouseClick(waitForObject(names.o2_Text))
    mouseClick(waitForObject(names.o_Text_2))
    # Addition done
    mouseClick(waitForObject(names.o2_Text))
    mouseClick(waitForObject(names.c_Text))
    doubleClick(waitForObject(names.c_Text))

    test.log("Hello World")
