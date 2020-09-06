# Plan with the project

## Basic functions

The service will offer a platform for discussion. There will be a registration page that allows the user to register an account using a unique username and a password. Logging in will not be required for reading the general discussion forum, but unregistered users may not send messages or open threads.

The forum will be divided into a few categories, some of which are only visible to certain users. A logged in user may open a new thread for discussion and all logged in users may give replies to the thread.

There will be administrator accounts and regular accounts. Administrator accounts will be able to hide threads or messages.

There will be a tool for searching or filtering messages.

## Database

Following kinds of data will be neseccary to be stored in the database:

* Users
   User data has to include the username and a hash value of the password. It might also have other data, such as the creation time of the account.
* Discussion boards
   Boards need names and maybe some sort of descriptions.
* Threads
   Threads will need a topic, and maybe an included opening message. It will also need to be linked to a board.
* Messages
   Messages need the actual message data and they need to be linked to a thread.

## Possible additional functions

If the project is successful and there is time to spare, there might be additional features, such as:

* Personalizable profile pages
* Ability to report messages to the administrators
* Private messages between users

