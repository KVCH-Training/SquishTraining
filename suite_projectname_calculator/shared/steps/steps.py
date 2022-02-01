# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names


@Given("I am at Calculator App")
def step(context):
    startApplication("calqlatr")


@Given("another precondition")
def step(context):
    custom_func()

@When("some action is performed")
def step(context):
    mouseClick(waitForObject(names.ONE_BUTTON))
    mouseClick(waitForObject(names.o5_Text))
    mouseClick(waitForObject(names.ONE_BUTTON))
    mouseClick(waitForObject(names.PLUS_BUTTON))
    mouseClick(waitForObject(names.ONE_BUTTON))
    mouseClick(waitForObject(names.TWO_BUTTON))
    mouseClick(waitForObject(names.o_Text_2))


@Then("the results should be as expected")
def step(context):
    test.compare(str(waitForObjectExists(names.o163_Text).text), "163")

def custom_func():
    doubleClick(waitForObject(names.c_Text))
    doubleClick(waitForObject(names.c_Text))
    doubleClick(waitForObject(names.c_Text))
    doubleClick(waitForObject(names.c_Text))
    doubleClick(waitForObject(names.c_Text))
    mouseClick(waitForObject(names.c_Text))
    
# @Then("some other testable outcome is achieved")
# def step(context):
#     pass
