import requests

with requests.Session() as s:
    s.post('https://my.lboro.ac.uk/campusm/sso/ldap/2548', data={'username': 'xxx', 'password': 'xxx'})
    x1 = s.get('https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-08-31T23%3A00%3A00.000Z&end=2025-10-31T23%3A59%3A59.000Z')
    print(x1.text)
