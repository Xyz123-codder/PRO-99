import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = "/PATH_TO_DELETE"

    days=30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for root_floder, floders , files in os.wait(path):
            
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_floder)
                deleted_folders_count += 1 #incrementing count
                break
            else:

                for folder in folders:
                    folder_path = os.path.join(root_floder, folder)

                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_file(file_path)
                        deleted_files_count += 1 # incrementing count
                for file in files:
                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count +=1 # incrementing count

            else:

                if seconds >= get_file_or_folder_age(path):
                    remove_file(path)
                    deleted_files_count += 1 #incrementing count

            else:
                 
                print(f'"{path}" is not found')
                deleted_files_count += 1 # incrementing count

            print(f"Total folders deletes: {deleted_folders_count}")
            print(f"Total files deleted: {deleted_files_count}")

def remove_folder(path):

    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delet the " +path)
    else:
        print("Unable to delet the " +path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ =='__main__':
    main()


