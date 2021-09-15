# auto-attendance

PREREQUISITES: selenium, webdriver of choice, pyautogui

A python based script that marks your attendance on Google classroom
The with the help of selenium the bot fires up the browser of your choice; with your credentials logs into your gmail account.
Notifications regarding your attendance end up in your gmail. The bot searches your inbox for emails having "attendance" as its subject clicks on it
and eventually ends up in the classroom. Once it arrives into the classroom page, mouse-clicks on predetermined coordinates with the help of pyautogui
begin to take place. After 45 ish seconds of running the program submits your attendance and quits all tabs. The script can be used along side 
task scheduler for complete automation.

