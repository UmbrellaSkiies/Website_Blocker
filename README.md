# Website_Blocker
This app blocks websites using a website's URL.

### New Features
  - Import/Export: Enable the ability to import and export the list of blocked websites, allowing users to save their settings or transfer them to another device.
  - GUI Enhancements: Improved the user interface by adding icons.
  - Notifications: Implemented alerts to inform users when a website is blocked or unblocked.

### Upcoming Features
  - Website blocker that can block the website for certain time range.

<img src="https://github.com/sagnikghoshcr7/images/blob/master/Website%20Blocker%20gif.gif" height="50px" width="405px"></h1>

### Prerequisite:
  - Python 3.x
  
### Get the code from the repository

```
git clone https://github.com/sagnikghoshcr7/Website-Blocker.git
```

### How To Use:
  - First copy all the files to a folder
  - Open sitelist.txt
  - Enter all the websites you want to block
  
  ### Example:
  sitelist.txt
 
   >www.facebook.com 
   
   >www.twitter.com 
   
   >www.google.com
  
  ### For Mac or Linux
  - Open Terminal(Linux or Mac) on the blocker folder and Type
  
```
 $ sudo python3 blocker.py
```
  
  ### For Windows
  - Right click on 'run.bat' 
  - Click Run as Administrator  
  - Then Enter the Time range for which block websites in the format of
  '13 30 15 25' for blocking From 13:30 PM till 15:25 PM
  
  ### Troublshoot
  #### To Reset Blocker and Unblock all websites
  run the program and do not enter any time range

    >Website Blocker 1.0
    >INFO: Python 3 is required for blocker to run


    >Enter time duration. Eg. '13 25 15 30' for from 1:25 PM to 3:30 PM
    >
    >
    >
    >
    
  
  This will unblock any website which is being blocked by blocker
