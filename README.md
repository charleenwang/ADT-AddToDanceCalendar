# ADT-AddToDanceCalendar
Add an event to your calendar! Currently this is set to events of 1 hour duration... will update in the future maybes :/

Make sure you have python 3

Enable the Google Calendar API
Go to https://developers.google.com/calendar/quickstart/python and click the button.
Click DOWNLOAD CLIENT CONFIGURATION and move the file credentials.json to working directory.

Run python create_event.py

First time running, it will ask you to authenticate.
Go back to terminal window and follow prompts.

The program will generate a file called token.pickle 
This saves your authentication, so if you want to change accounts... delete this file and rerun the program to generate a new one.