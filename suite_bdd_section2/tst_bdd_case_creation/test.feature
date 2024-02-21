Feature: Filling of quickaddressbook
    As a user I want to fill the Address Book with entries

#Initial
    Scenario: Initial state of empty address book
        Given quickaddressbook application is running
        When I remove initial entries
        Then Address book should have zero entry