import os, stat
import Variables, Classes, Functions

#Export Free Comic
def export_free_comic(raw_images_directory):
    print('Executing export_free_comic...')
    export_url = Functions.create_exportation_directory()
    export_subdirectory_url = Functions.create_exportation_subdirectory(export_url, 'Comic')
    hash_code = Functions.hash_store(Variables.creator_name, export_subdirectory_url)
    Functions.copyimages(raw_images_directory, export_subdirectory_url, hash_code)
    print('executed export_free_comic successfully')

#Export Monthly Rewards
def export_monthly_rewards(users, directories):
    print('Executing export_monthly_rewards...')
    export_url = Functions.create_exportation_directory()
    for user in users:
        user_directory = Functions.create_exportation_subdirectory(export_url, user.username)
        hash_code = Functions.hash_store(Variables.creator_name, user_directory)
        for directory in directories:
            content_directory = Functions.create_exportation_subdirectory(user_directory, directory.folder_name)
            Functions.copytree(directory.source_url, content_directory, hash_code)
    print('executed export_monthly_rewards successfully')