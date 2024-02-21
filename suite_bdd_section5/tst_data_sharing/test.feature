Feature: Filling of quickaddressbook
    As a user I want to fill the Address Book with entries

#Sharing data with context.userData
     Scenario: Forename and surname are added to the table
        Given quickaddressbook application is running
        When I add a new person 'Bob','Koo','500600800','bob@m.com' to address book
        Then previously entered forename and surname are in the table