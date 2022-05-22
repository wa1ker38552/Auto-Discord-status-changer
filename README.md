# Auto-Discord-status-changer

Script that uses PATCH requests to change your status on Discord using Discord's API (v9). 

You can type your own messages and the script will cycle through each word from each message. The messages are picked at random and you can set your own timing. 
Custom emoji can be set in the json payload. keepAlive() function since Replit hosting is flaky. 

Inspect and find 'authorization' under the request headers in the Network tab.
![image](https://user-images.githubusercontent.com/100868154/169673655-9431aee6-9130-4d5b-af48-f95f06b6ca0b.png)
