import os
import yaml
from launcher_globals import *



class LinkParser():

    def __init__(self):
        # Parser globals
        self.link_data = []
        self.download_list = []
        self.unzip_list = []


    def extractLinks(self, file_name):
        # Read the YAML file
        with open(file_name, 'r') as stream:
            data_loaded = yaml.load(stream)

        for file_data in data_loaded:
            link_line = (data_loaded[file_data])

            self.link_data.append(link_line)

            # Keep the UI active
            self.refreshUI()

    def parseLinks(self):
        for link_data in self.link_data:

            try:

                file_platform = (link_data['platform'])

                if file_platform == CURRENT_PLATFORM or file_platform == PLATFORM_ALL:

                    file_url = (link_data['url'])
                    file_path_declar = (link_data['path'])
                    file_name = (link_data['name'])
                    file_extension = (link_data['extension'])
                    # File archive can be true or false
                    file_archive = (link_data['archive'])
                    file_hash =  (link_data['hash'])

                    if file_path_declar == BASE_FILEPATH_D:
                        file_path = BASE_FILEPATH_S + file_name
                        file_dir = BASE_FILEPATH_S
                    elif file_path_declar == RESOURCE_FILEPATH_D:
                        file_path = RESOURCE_FILEPATH_S + file_name
                        file_dir = RESOURCE_FILEPATH_D
                    else:
                        file_path = BASE_FILEPATH_S + file_name
                        file_dir = BASE_FILEPATH_S

                    self.download_list.append(
                        [file_url, file_path, file_name, file_extension, file_archive, file_hash, file_dir])

                    if file_archive == True:
                        self.unzip_list.append(
                            [file_url, file_path, file_name, file_extension, file_archive, file_hash, file_dir])

            except:
                if TESTING_NF:
                    print (LINK_INVALID % link_data)
                self.setFailedLauncher()
                break

