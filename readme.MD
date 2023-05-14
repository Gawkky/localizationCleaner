# Localization Cleaner MacOS

This is a small Python script that lets you delete all unneeded ".lproj"-files from you application folders. This means all ".lproj"-files except base.lproj.

---

## How To Use

This is fairly simple and straightforward. You go to your Applications folder on your Macbook and look for all your **third party apps**, as Apple doesn't let you modify it's own apps.

Type these names in the applications list. If your mac is setup to show all extensions don't add the .app extension as the script does take care of this by itself.

When filled out all the app-names you can simply save the file and run it with following command. </br>
`python3 main.py`

## Warning

These files **DON'T** go first to your bin but are immidiatly removed from your computer. Use this script on own risk and always check the code yourself if it doesn't have any mallicious intends as this is good practice for any code you execute. Also I'm not responsible for any applications that stop functioning as a result of the script and you yourself are also responsible for modifying the script to your own needs.
