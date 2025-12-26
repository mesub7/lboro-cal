from datetime import datetime
import json
import requests
import os
import icalendar

OUTPUT_PATH = '...'  # Fill this out

cal = icalendar.Calendar()
cal.calendar_name = "Timetable"  # May want to change to suit
cal.add('prodid', '-//mesub7//Lboro-Cal//')
cal.add('version', '2.0')
cal.add('calscale', 'GREGORIAN')

with requests.Session() as s:
    s.post('https://my.lboro.ac.uk/campusm/sso/ldap/2548', data={'username': os.environ['LBOROUSER'], 'password': os.environ['LBOROPASS']})
    period1 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-09-28T23%3A00%3A00.000Z&end=2025-12-01T23%3A59%3A59.000Z').text)
    period2 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-12-02T23%3A00%3A00.000Z&end=2026-02-19T23%3A59%3A59.000Z').text)
    period3 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2026-02-20T23%3A00%3A00.000Z&end=2026-05-02T23%3A59%3A59.000Z').text)
    period4 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2026-05-03T23%3A00%3A00.000Z&end=2026-06-13T23%3A59%3A59.000Z').text)

periods = [period1, period2, period3, period4]
for period in periods:
    for i in range(len(period['events'])):
        teaching = period['events'][i]
        try:
            teaching['teacherName']
        except KeyError:
            teaching['teacherName'] = None
        try:
            teaching['teacherEmail']
        except KeyError:
            teaching['teacherEmail'] = None
        if teaching['teacherEmail']:
            teachers = teaching['teacherEmail'].split('; ')
        else:
            teachers = ["anonymous@lboro.ac.uk"]
        event = icalendar.Event()
        event.add('uid', teaching['eventRef'])
        event.add('dtstamp', datetime.now())
        event.add('dtstart', datetime.fromisoformat(teaching['start']))
        event.add('dtend', datetime.fromisoformat(teaching['end']))
        event.add('summary', teaching['desc1'])
        event.add('description', f"{teaching['desc1']} with {teaching['teacherName']}." if teaching['teacherName'] else f"{teaching['desc1']}.")
        event.add('location', teaching['locAdd1'])
        if len(teachers) == 1:
            event.add('organizer', f"mailto:{teachers[0]}")
        else:
            event.add('organizer', f"mailto:{teachers[0]}")
            for teacher in teachers[1:]:
                event.add('attendee', f"mailto:{teacher}")
        cal.add_component(event)

tmp_path = OUTPUT_PATH + ".tmp"
with open(tmp_path, "wb") as f:
    f.write(cal.to_ical())
os.replace(tmp_path, OUTPUT_PATH)
