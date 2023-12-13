Current state is that backend is functional and GUI is incomplete and not merged(branch ui).

Initially I intended to write this largely based around SQL, which I believe is the
 correct way to do the data handling, however doing this without a full infrastructure 
 setup required me to learn sqlite3 and between learning and difficulties with writing
 the connecting points, like manipulating date in python and SQL, I concluded this was
 proving too slow and impractical. So I changed tack to OOP Python and was able to put
 together the system as it stands much more quickly and smoothly.

 Flaws in this choice include lack of normalised data structure (leading to assumption
 that there exists only one copy of any book) and a less standardised way of interacting
 with the "database".

 I have a clear plan for building a GUI using Flask and Jinja2 however between delay from
 changing tack and my rustiness making me have to look up most things, I have run out of 
 time. 

 Security is currently missing. I have made password a private attribute however this is
 clearly insufficient. I would like to hash the password on registration and store that
 however I am not currently confident I understand hashlib well enough to do this 
 correctly.

 I have GDPR concerns about showing all users the full name and email address of users
 who currently have a book on loan. There maybe a valid purpose but if not, I think this
 would breach confidentiality and purpose limitation.

