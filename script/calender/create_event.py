from datetime import datetime, timedelta,time
from .calc_setup import get_calendar_service

def create_event(summary="Event",description="This is a tutorial example of automating google calendar with python"
,date=datetime.now().day,month=datetime.now().month,year=datetime.now().year,
hour=datetime.now().hour,minute=datetime.now().minute,duration=1):
   service = get_calendar_service()
   day = datetime(year=year, month=month, day=date,hour=hour,minute=minute)
   start = day.isoformat()
   end = (day + timedelta(hours=duration)).isoformat()
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": summary,
           "description": description,
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
        }
   ).execute()
   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])
