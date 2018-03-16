import platform
import os

TESTING_NF = False
LOCAL_GAME_DOWNLOAD = False
LOCAL_GAME_SERVER = False


CURRENT_PLATFORM = platform.system()
PLATFORM_ALL = 'all'
CURRENT_PATH = os.getcwd()


if TESTING_NF:
    print ('Host operating system: ' + CURRENT_PLATFORM)

    RESOURCE_FILE = 'resources.yaml'
    RESOURCE_LINK = 'https://toonclash.tk/launcher/resources.yaml'

RESOURCE_NAME = 'resource-links'

BASE_FILEPATH_D = 'base'
RESOURCE_FILEPATH_D = 'resources'

if CURRENT_PLATFORM == 'Linux':
    BASE_FILEPATH_S = './'
    RESOURCE_FILEPATH_S = './resources/'
else:
    BASE_FILEPATH_S = '.\\'
    RESOURCE_FILEPATH_S = 'resources\\'

DOWNLOADING_FILE = 'Downloading: %s'
DOWNLOAD_COMPLETE_FILE = '%s has completed.'
FILE_UPTODATE = '%s is up to date.'
FILE_DOWNLOAD_FAILED = 'Could not download %s !'
LINK_INVALID = 'WARNING!!! Something went wrong while parsing: %s !'

UPDATED_STARTED = 'Update has begun! Please wait...'
FILE_CURRENT = 'File %s is already up to date.'
UPDATE_COMPLETE = 'The game is up to date!'
UPDATE_FAILED = 'Update has failed!'

ARCHIVE_EXTRACTING = 'Extracting: %s'
ARCHIVE_COMPLETE = 'Finished extracting %s'
ARCHIVE_FAILED = 'Could not extract %s'

MD5_FAILED = 'Failed retriving MD5 hash for %s !'

LAUNCHER_STATE_WAITING = 'Please login...'
LAUNCHER_STATE_UPDATING = 'Please wait...'
LAUNCHER_STATE_LAUNCHING = 'Have fun!'

LAUNCHER_STATUS_LOGIN = 'Welcome!'
LAUNCHER_STATUS_GIVE_INPUT = 'You must enter a username and password.'
LAUNCHER_STATUS_FAILURE = 'Something went wrong while updating.'

    GAME_SERVER = 'gs1.toonclash.tk'

if CURRENT_PLATFORM == 'Linux':
    PYTHON_PATH = '/usr/bin/python2'
else:
    PYTHON_PATH = '\panda3d\python\ppython.exe'

