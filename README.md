A quick fix to your over-large PyInstaller executables. 


How to use: 

Download the files in the directory you want the virtual environment to be installed. 

Open the directory in Command Prompt, and enter the following line: 
```
pyshrinker.bat nameofyourvenvfolder nameofyourscript.py
```

After that simply wait for it to finish, and then locate the dist folder in nameofyourvenvfolder, where your shrunk single-file executable is ready and waiting! 

Here's the before and after: 


![GU88X6ha4AIKof3](https://github.com/user-attachments/assets/236d3a2a-a49e-4769-b35e-8125e6fd5288)

![GU88Z8_a4AQ_Cvq](https://github.com/user-attachments/assets/c9fd33ae-7643-48a6-8e83-e090538cfab2)


Note: Current version only works with single scripts, a future update will be introduced which walks your folders for any and all inherited modules.
