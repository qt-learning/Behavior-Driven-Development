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

@When("I remove initial entries")
def step(context):
    mouseClick(waitForObject(names.header_Remove_ToolButton))
    mouseClick(waitForObject(names.header_Remove_ToolButton))

@Step("I add new persons to address book")
def step(context):
    table = context.table
    # Drop initial row with column headers
    table.pop(0)
    for (forename, surname, phone, email) in table:
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
        test.log("Added entry: "+ forename + ", " + surname + ", " + email + ", " + phone)
    
@Then("'|integer|' entries should be present")
def step(context, num):
    snooze(1) #make sure everything is added (animation)
    test.compare(waitForObjectExists(names.addressBookView_Item).children.count(), num + 2)