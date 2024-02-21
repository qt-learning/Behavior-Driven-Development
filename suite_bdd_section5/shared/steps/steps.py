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


@Given("quickaddressbook application is running")
def step(context):
    startApplication("quickaddressbook")
    test.compare(waitForObjectExists(names.mainWindow_QQuickApplicationWindow).visible, True)

@When("I add a new person '|word|','|word|','|integer|','|any|' to address book")
def step(context, forename, surname, phone, email):
    type(waitForObject(names.mainWindow_QQuickApplicationWindow), "<Tab>")
    mouseClick(waitForObject(names.activeFocusControl_Add_ToolButton))
    mouseClick(waitForObject(names.addViewComponent_firstNameField_TextField))
    type(waitForObject(names.addViewComponent_firstNameField_TextField), forename)
    type(waitForObject(names.addViewComponent_firstNameField_TextField), "<Tab>")
    type(waitForObject(names.addViewComponent_lastNameField_TextField), surname)
    type(waitForObject(names.addViewComponent_lastNameField_TextField), "<Tab>")
    type(waitForObject(names.addViewComponent_phoneNumberField_TextField), phone)
    type(waitForObject(names.addViewComponent_phoneNumberField_TextField), "<Tab>")
    type(waitForObject(names.addViewComponent_emailAddressField_TextField), email)
    mouseClick(waitForObject(names.header_Back_ToolButton))
    context.userData = {}
    context.userData['forename'] = forename
    context.userData['surname'] = surname

@Then("previously entered forename and surname are in the table")
def step(context):
    test.ocrTextPresent(context.userData['forename'], { "tesseract": { "psm": 3 } }, waitForObjectExists(names.mainWindow_addressBookView_AddressBookView))
    test.ocrTextPresent(context.userData['surname'], { "tesseract": { "psm": 3 } }, waitForObjectExists(names.mainWindow_addressBookView_AddressBookView))