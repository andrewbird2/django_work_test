Draftable Django JS work test
=============================

Tips
----

* If you have questions about specs/clarifications or what you're supposed to do,
  please do ask. You should make your own decisions about how to structure the
  code etc. Think of me as the product person and you the software engineer. That
  said, if you get stuck on a technical thing, please do ask, I may be able to
  help.

* You don't need to do things in order.

* After you're done, please push your code. If you're done before the time limit,
  just finish early and we'll take that into account.


The Task
--------

Draftable's CRM (Contact Relationship Management) system currently stores the list of Draftable customers.
We want to group these customers into their relevant organisations to make it easier to manage our contact list
going forwards.  In this task we are ultimately trying to add a column called "Organisation" to the table on
the front page of this sample app.


Setup
--------------
This project was setup using Python 3.6, Ubuntu 18, postgresql 10, and Node 8.  It should be possible to complete it
with any operating systems, but you may well have to fix small things as this is untested.  Please perform the following steps
at the start of the work test and let us know if you have having problems.

To setup a local environment, follow the following steps:

* Clone this repository

* Install the pip requirements::

    $ pip install -r requirements/local.txt

* Create the database::

    $ createdb worktest

* Migrate the database::

    $ ./manage.py migrate

* Create an **superuser account** using this command::

    $ python manage.py createsuperuser

* Install the npm packages and build the frontend::

    $ cd frontend
    $ npm install
    $ npm run build

* You should now be able to run a server::

    $ ./manage.py runserver

If everything is working as expected, you should be able to see a table on the root URL of the website containing a list
of customer names and email addresses.

Detailed instructions
-----------------------------

* Create a new model called "Organisation", it should have two fields
    * Name
    * Date/time created
* Add a nullable foreign key to the Customer model that links to Organisation
* Using the existing data in the Customer table, create organisations. Note the following:
    * If a customer has an email such as andrew@johnsonlegal.com, we want to create a new organisation with the name johnsonlegal, and link this customer to the organisation
    * If a customer has a common domain name such as @gmail.com, skip these customers, as we don't want "gmail" as an organisation in our system
    * We prefer you put this code in a django migration using RunPython, but providing a separate script is also fine.
* Create an OrganisationAdmin class that allows users to view organisations in the Django admin. Also add an inline allowing users to see which customers are part of each organisation.
* Modify the existing API endpoint such that it includes the customer organisation
* Modify the react app so that it displays the customer's organisation in the table.
