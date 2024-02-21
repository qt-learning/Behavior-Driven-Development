Feature: Filling of quickaddressbook
    As a user I want to fill the Address book with entries

#Table with context.table
     Scenario: State after adding two entries
     Given quickaddressbook application is running
     When I remove initial entries
     And I add new persons to address book
        | forename   | surname   | phone  | email        |
        | John       | Smith     | 123123 | john@m.com   |
        | Alice      | Thomson   | 234234 | alice@m.com  |
     Then '2' entries should be present

#Table with context.table and test data
     Scenario: State after adding two entries with external test data
     Given quickaddressbook application is running
     When I remove initial entries
     And I add new persons to address book
        From testdata/contact_list.tsv
     Then '2' entries should be present