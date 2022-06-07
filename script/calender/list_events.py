import datetime
from .calc_setup import get_calendar_service
from . import engine_speak
def list_event():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting List of 10 events')
    events_result = service.events().list(
    calendarId='primary', timeMin=now,
    maxResults=10, singleEvents=True,
    orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        engine_speak.engine_speak('No upcoming events found.')
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            temp=(start.split("T")[1]).split(":")
            date=(start.split("T"))[0].split("-")
            engine_speak.engine_speak("remainder of "+event['summary']+" on "+str(int(date[2]))+"/"+str(int(date[1]))+"/"+str(int(date[0]))+" at "+temp[0]+" "+temp[1].split(":")[0])
