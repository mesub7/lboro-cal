import json
import requests
import os

with requests.Session() as s:
    s.post('https://my.lboro.ac.uk/campusm/sso/ldap/2548', data={'username': os.environ['LboroUser'], 'password': os.environ['LboroPass']})
    x1 = s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-09-29T23%3A00%3A00.000Z&end=2025-12-01T23%3A59%3A59.000Z')
    x2 = s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-12-02T23%3A00%3A00.000Z&end=2026-02-19T23%3A59%3A59.000Z')
    x3 = s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2026-02-20T23%3A00%3A00.000Z&end=2026-05-02T23%3A59%3A59.000Z')
    x4 = s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2026-05-03T23%3A00%3A00.000Z&end=2026-06-13T23%3A59%3A59.000Z')
    print(x4.text)
