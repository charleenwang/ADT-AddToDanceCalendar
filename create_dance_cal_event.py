from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# scope set to modify calendar events 
# if you change this you have to delete the token.pickle file
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def format_time(number):
    if number < 10:
        return '0' + str(number)
    return str(number)

def main():
    """Uses the Google Calendar API to add ADT 
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Set this to the # of dances that you wanna add.
    NUM_DANCES = 18
    # Set this to the integer number of the first day of ADT!!!
    START_DAY = 9
    MONTH = 9
    YEAR = 2019

    # Converts to datetime format.
    string_dateTime = str(YEAR) + '-' + format_time(MONTH) + '-'

    for x in range(NUM_DANCES):
        # Inputs.
        dance = input("Dance Name: ")
        location = input("Location: ")
        description = input("Choreographer(s): ")
        day = int(input("Day (ex: 1 = Mon, 7 = Sun): "))
        time = int(input("Time (24-hr): "))
        # Converts to datetime format.
        startTime = string_dateTime + str(START_DAY + day - 1) + 'T' + format_time(time) + ':00:00'
        endTime = string_dateTime + str(START_DAY + day - 1) + 'T' + format_time(time + 1) + ':00:00'
        # Creates calendar event metadata
        event = {
          'summary': dance,
          'location': location,
          'description': 'choreogs: ' + description,
          'start': {
            'dateTime': startTime,
            'timeZone': 'America/New_York',
          },
          'end': {
            'dateTime': endTime,
            'timeZone': 'America/New_York',
          },
          'recurrence': [
            'RRULE:FREQ=WEEKLY;COUNT=13;'
          ],
        }
        # Creates the actual event
        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: ', (event.get('htmlLink')))

        print("__________________________\n")

if __name__ == '__main__':
    main()