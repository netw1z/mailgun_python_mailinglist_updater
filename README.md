# mailgun_python_mailinglist_updater
Update your mailgun mailing list via python V1.

This script will data from your mysql database and update your mailgun mailing list with new entries and add variables.
Mailgun has a limit of 1000 inserts at a time and this script doesn't check for that yet.
Duplicates or changes to the acccounts are set to UPSERT automatically.
This script also handles structing adding varibles to each mailing list entry - so you can access them when sending emails.
For example - you could add a users profile image to the email by storing it in a user varible.

I've included an example mysql structure DB to use with it so you can see how it works.

Modify this script as needed. Version One runs with an entry in crontab to run it once a month before the newsletter goes out.

www.mediathreat.com
