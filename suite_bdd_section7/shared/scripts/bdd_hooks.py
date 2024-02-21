# -*- coding: utf-8 -*-

# This file contains hook functions to run as the .feature file is executed.
#
# A common use-case is to use the OnScenarioStart/OnScenarioEnd hooks to
# start and stop an AUT, e.g.
#
# @OnScenarioStart
# def hook(context):
#     startApplication("quickaddressbook")
#
# @OnScenarioEnd
# def hook(context):
#     currentApplicationContext().detach()
#
# For the complete reference to this and similar available APIs
# (OnFeatureStart/OnFeatureEnd, OnStepStart/OnStepEnd) see the section
# 'Performing Actions During Test Execution Via Hooks' in the Squish manual:
#
# https://doc.qt.io/squish/behavior-driven-testing.html#performing-actions-during-test-execution-via-hooks

# Detach (i.e. potentially terminate) all AUTs at the end of a scenario

@OnFeatureStart
def hook(context):
    test.log("Feature starts: " + context.title)
    global counter
    counter = 0

@OnFeatureEnd
def hook(context):
    global counter
    test.log(str(counter) + " steps executed")
    test.log("Feature ends: " + context.title)
@OnScenarioStart
def hook(context):
    test.log("Scenario starts: " + context.title)
    startApplication("quickaddressbook")
    for ctx in applicationContextList():
        test.log("Host: " + str(ctx.host))

@OnScenarioEnd
def hook(context):
    for ctx in applicationContextList():
        ctx.detach()
    test.log("Scenario ended: " + context.title)
   
@OnStepStart
def hook(context):
    test.log("Step starts: " + context.text)
    global counter
    counter += 1 

@OnStepStart
def hook(context):
    text = context.text
    if text.find("parameters") > -1:
        test.warning("About to execute a step that should be refactored to include arguments: %s" % text)

@OnStepEnd
def hook(context):
    test.log("Step ended: " + context.text)