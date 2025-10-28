# Lboro Cal

<img width="1226" height="720" alt="image" src="https://github.com/user-attachments/assets/4bd3a66d-56b3-4c6a-abd5-9d19eb61ea25" />


This is a little passion project made because there's no way to export your timetable to external calendars (how unfortunate).

This repo aims to solve this.
Others have constructed a few solutions, but these are static. This solution is dynamic (if you allow it to be).

It is mostly RFC 5545 compliant. The title is your module and the type of contact. The location is the room code and the description is who you'll be having it with.

At the moment, it's kind of offered s-is (I am very busy). In the future, I will try and smooth it out so it's easier for you to deploy.

Dependencies are: iCalendar and requests.
You'll need your credentials to access the service. These are currently environment variables (so only run this on a system you trust or have full control over).

1) Get the file
2) Install dependencies
3) Run the script (This will generate an .ics file)
5) Upload this to your calendar provider of choice

If you want it to be dynamic, you need to find a way to host it somewhere and update the file. A cloud storage solution may work but I've never tried it.
I have a VPS running Nginx, which statically serves the file over the internet. A cron job runs every day during a quiet time to pick up the latest changes (room changes etc).

A known issue for Outlook is that past events are not synced. This is a design choice by Microsoft.

## Bugs and development
If there's a bug or issue then please make an issue.
If you think you can improve this, by all means make a PR.
