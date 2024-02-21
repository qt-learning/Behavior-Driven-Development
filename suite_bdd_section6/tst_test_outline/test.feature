Feature: Filling of addressbook
    As a user I want to fill the Address Book with entries

#Outline
Scenario Outline: Adding a single entry multiple times
		Given quickaddressbook application is running
		When I remove initial entries
		And I add a new person '<forename>','<surname>','<phone>','<email>' to address book
		Then '1' entries should be present
		Examples:
	      | forename | surname  | phone      |   email     |
	      | John     | Doe      | 500600700  | john@m.com  |
	      | Bob      | Koo      |  500600800 | bob@m.com   |


#Outline using external table
Scenario Outline: Adding a single entry multiple times with external test data
		Given quickaddressbook application is running
		When I remove initial entries
		And I add a new person '<forename>','<surname>','<phone>','<email>' to address book
		Then '1' entries should be present
		Examples:
	    	From testdata/contact_list.tsv