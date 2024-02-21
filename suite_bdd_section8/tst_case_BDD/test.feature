Feature: Filling of quickaddressbook
    As a user I want to fill the Address Book with entries

#Initial
    Scenario: Initial state of empty address book
        Given quickaddressbook application is running
        When I remove initial entries
        Then Address Book should have zero entry

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

#Table with context.table
     Scenario: State after adding two entries
     Given quickaddressbook application is running
     When I remove initial entries
     And I add new persons to address book
        | forename   | surname  | phone   | email       |
        | John      | Smith     |  123123 |john@m.com   |
        | Alice     | Thomson   | 234234  | alice@m.com |
     Then '2' entries should be present

#Table with context.table and test data
     Scenario: State after adding two entries with external test data
     Given quickaddressbook application is running
     When I remove initial entries
     And I add new persons to address book
        From testdata/contact_list.tsv
     Then '2' entries should be present

#Sharing data with context.userData
     Scenario: Forename and surname are added to the table
        Given quickaddressbook application is running
        When I add a new person 'Bob','Koo','500600800','bob@m.com' to address book
        Then previously entered forename and surname are in the table

#Outline
Scenario Outline: Adding a single entry multiple times
		Given quickaddressbook application is running
		When I remove initial entries
		And I add a new person '<forename>','<surname>','<phone>','<email>' to address book
		Then '1' entries should be present
		And previously entered forename and surname are in the table
		Examples:
	      | forename | surname | phone     | email       |
	      | John     | Doe      | 500600700 | john@m.com  |
	      | Bob      | Koo      | 500600800 | bob@m.com   |


#Outline using external table
Scenario Outline: Adding a single entry multiple times with external test data
		Given quickaddressbook application is running
		When I remove initial entries
		And I add a new person '<forename>','<surname>','<phone>','<email>' to address book
		Then '1' entries should be present
		And previously entered forename and surname are in the table
		Examples:
	    	From testdata/contact_list.tsv