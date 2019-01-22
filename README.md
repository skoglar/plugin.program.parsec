# Parsec Launcher for LibreELEC

This is a small add-on for launching Parsec on Libreelec  
Although it should be easily modifiable for other linux distributions.    

It uses the [raspbian version](https://s3.amazonaws.com/parsec-build/package/parsec-rpi.deb) of parsec provided by the [Parsec Team](https://parsecgaming.com/downloads)  

## Installation and Usage
Download the latest [release](https://github.com/skoglar/plugin.program.parsec/releases/download/v1.0.0/plugin.program.parsec.zip) on libreelec using wget, or any other method you like  
```wget https://github.com/skoglar/plugin.program.parsec/releases/download/v1.0.0/plugin.program.parsec.zip```  
Then install it as any other zipped add-on and go to the addon settings
## First run
![Parsec Settings](https://i.imgur.com/6FIpWPA.png)  
  
When running for the first time it is absolutely necessary to set both `Email` and `Password` before running the addon.  
After that you'll need to know your `Server ID` and put it on the settings.  .  
The `Server Selection` parameter refers to an option given by parsec once it's logged into your account, which corresponds to a number on a list of servers.  

**This will only be used on the first login and can be ignored unless you need to connect to a specific server on the list**  
  
![Servers Menu](https://i.imgur.com/zUGpOzO.png)

## Second Run  
From the second run onwards it is only important to have a `Server ID` saved, since thats the only parameter the addon will be using.
Your server ID can be obtained via the parsec app or web on the **Manage** section  
  
![Manage Button](https://i.imgur.com/oIRQITd.png) -> 
![Server ID](https://i.imgur.com/7vTMRON.png)  
  
Once you get that number on the settings menu, you're all set!
