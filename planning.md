UI needs:
-login
-register
-signout
-display table
-filter table
-borrow action

Concern: data protection showing borrower's details to other members

backend

database
User table: ID, first name, last name, email, password(how to securely store?)
Book table: ID, Title, Description, Image, (Author, ISBN etc)
Copy table: ID, Available, Borrower, Due Date

Assumptions made:
Security is out of scope. While security is extremely important, I don't know the best crypto library for python and I don't know if researching this is in scope for 3 hours.
It is permissible for users to see personal details of other users.



