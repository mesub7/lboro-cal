from datetime import datetime
import json
import requests
import os
import icalendar

cal = icalendar.Calendar()
cal.calendar_name = "Computer Science Timetable - David Oladiran"
cal.add('prodid', '-//mesub7//Lboro-Cal//')
cal.add('version', '2.0')
cal.add('calscale', 'GREGORIAN')

with requests.Session() as s:
    s.post('https://my.lboro.ac.uk/campusm/sso/ldap/2548', data={'username': os.environ['LboroUser'], 'password': os.environ['LboroPass']})
    x1 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-09-29T23%3A00%3A00.000Z&end=2025-10-04T23%3A59%3A59.000Z').text)
    period1 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-09-29T23%3A00%3A00.000Z&end=2025-12-01T23%3A59%3A59.000Z').text)
    period2 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-12-02T23%3A00%3A00.000Z&end=2026-02-19T23%3A59%3A59.000Z').text)
    period3 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2026-02-20T23%3A00%3A00.000Z&end=2026-05-02T23%3A59%3A59.000Z').text)
    period4 = json.loads(s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2026-05-03T23%3A00%3A00.000Z&end=2026-06-13T23%3A59%3A59.000Z').text)

print(x1['events'][0]['eventRef'])

# print(period1['events'])
periods = [period1, period2, period3, period4]
for period in periods:
    for i in range(len(period['events'])):
        teaching = period['events'][i]
        event = icalendar.Event()
        event.add('uid', teaching['eventRef'])
        event.add('dtstamp', datetime.now())
        event.add('dtstart', datetime.fromisoformat(teaching['start']))
        event.add('dtend', datetime.fromisoformat(teaching['end']))
        event.add('summary', teaching['desc1'])
        event.add('description', f"{teaching['desc1']} with {teaching['teacherName']}." if teaching['teacherName'] else f"{teaching['desc1']}.")
        event.add('location', teaching['locAdd1'])
        event.add('organiser', f"mailto:{teaching['teacherEmail']}")
        cal.add_component(event)

with open('test_cal.ics', 'wb') as f:
    f.write(cal.to_ical())

# period1['events']... - get len and interate through
# Get the relevant details: uid -> eventref, dtstamp -> now, dtstart/end -> start/end
# summary -> desc1, description - F STRING of {desc1} with {teacherName} location -> locAdd1, organiser -> mailto:teacherEmail
# populate to calendar
# save

# Find a way to host on a server (oracle!?!?)

# See if outlook will accept it

# Do batch jobs - update every day at midnight

# Advance stuff - overwrite the calendar every day.
