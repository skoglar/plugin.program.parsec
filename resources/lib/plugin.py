import logging
import xbmcaddon
import xbmcgui
import os
import stat
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcplugin import addDirectoryItem, endOfDirectory

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()

#Get the server id from the settings
server_selection = ADDON.getSetting('server_selection')
credentials = [ ADDON.getSetting('email'),
                ADDON.getSetting('password'),
                "y",
                server_selection ]
settings = [ "y",
              server_selection ]
def check_permisions(root_path):
    res_path = os.path.join(root_path, "resources")
    elevate_perms = os.stat(res_path+"/elevate.sh")
    runparsec_perms = os.stat(res_path+"/run_parsec.sh")
    firstrun_perms = os.stat(res_path+"/first_run.sh")

    os.chmod(res_path+"/elevate.sh", elevate_perms.st_mode | stat.S_IEXEC)
    os.chmod(res_path+"/run_parsec.sh", runparsec_perms.st_mode | stat.S_IEXEC)
    os.chmod(res_path+"/first_run.sh", runparsec_perms.st_mode | stat.S_IEXEC)

    data_path = os.path.join(res_path, "data")
    parsec_perms = os.stat(data_path+"/parsec")
    os.chmod(data_path+"/parsec", parsec_perms.st_mode | stat.S_IEXEC)

def credentials_set(root_path):
    data_path = os.path.join(root_path, "resources", "data")
    creds_exist = os.path.isfile(data_path+'/creds')
    if creds_exist:
        return True
    else:
        creds_file = open(data_path+"/creds","w+")
        for line in credentials:
            if line.isdigit():
                creds_file.write(line)
            else:
                creds_file.write(line+'\n')
        creds_file.close()
        return False

def save_settings(root_path):
    data_path = os.path.join(root_path, "resources", "data")
    settings_file = open(data_path+"/settings")
    for option in settings:
        if option.isdigit():
            settings_file.write(option)
        else:
            settings_file.write(option+'\n')


#Launch parsec through a script
def launch_parsec(root_path):
    if server_selection == "0": 
        xbmcgui.Dialog().ok("Parsec", "You need to set a server first!")
    else:
    	#Set paths:
    	#Resource path
        res_path = os.path.join(root_path, "resources")
        #Binary path
        parsec_path = os.path.join(root_path, "resources", "data", "parsec")
        #Data path
        data_path = os.path.join(root_path, "resources", "data")
        #Settings Path
        settings_path = os.path.join(root_path, "resources, data", "settings")
        #Script with arguments
        script_call = res_path+"/elevate.sh"+" "\
        			  	+parsec_path+" "\
        			  	+settings_path
        script_first_call = res_path+"/elevate.sh"+" "\
                        +data_path
        #Launch!
        check_permisions(root_path)
        if credentials_set(root_path):
            creds_file = open(data_path+"/creds","w+")
            creds_file.write('nothing to see here')
            xbmcgui.Dialog().ok("Parsec", "All set, launching!")
            os.system("sh "+script_call)
        else:
            xbmcgui.Dialog().ok("Parsec", "Getting ready for our first launch!")
            os.system("sh "+script_first_call+" first_run")
