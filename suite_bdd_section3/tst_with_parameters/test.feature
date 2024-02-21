Feature: Filling of quickaddressbook
    As a user I want to fill the Address Book with entries

#Steps for new entry
    Scenario: State after adding one entry
        Given quickaddressbook application is running
        When I remove initial entries
        And I add a new person 'John','Doe','500600700','john@m.com' to address book
        Then '1' entries should be present

#Parameters
     Scenario: State after adding one entry
        Given quickaddressbook application is running
        When I remove initial entries
        And I add a new person 'Bob','Koo','500600800','bob.com' to address book
        Then '1' entries should be present