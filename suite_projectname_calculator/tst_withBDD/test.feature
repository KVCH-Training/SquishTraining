# This is a sample .feature file
# Squish feature files use the Gherkin language for describing features, a short example
# is given below. You can find a more extensive introduction to the Gherkin format at
# https://cucumber.io/docs/gherkin/reference/
Feature: As a user i want to test calculator app

    Scenario: User check/verify addition operation
        Given I am at Calculator App
          And another precondition
         When some action is performed
         Then the results should be as expected
#          And some other testable outcome is achieved

	Scenario: User check/verify substraction operation
        Given I am at Calculator App
         When some action is not performed
         Then the results should be as not expected