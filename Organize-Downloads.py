import os
import collections

#Find download folders
#Use this only if your default download folder is at your "C" disk

#downloads_path = os.path.join(
#    os.path.expanduser('~'),'Downloads'
#)

#Use this if you want to specify your downloads folder
downloads_path = os.path.normpath('E:\\Users\\Antonis Rouseas\\Downloads')

#Create "Auto-Sorted" folder
save_path = os.path.join(downloads_path, "Auto-Sorted")
if not os.path.exists(save_path):
    os.mkdir(save_path)

# Type of file to folder
file_ext = collections.defaultdict()
for filename in os.listdir(downloads_path):
    check = os.path.join(downloads_path, filename)
    if not filename == "Organize-Downloads.lnk":
        if not os.path.isdir(check):
            file_type = filename.split('.')[-1]
            file_ext.setdefault(file_type, []).append(filename)

#Transfer files to their folder
for folder_name, folder_items in file_ext.items():
    folder_path = os.path.join(save_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for item in folder_items:
        source = os.path.join(downloads_path, item)
        dest = os.path.join(folder_path, item)
        #Check if a file is a duplicate, if it is rename it and move it
        if not os.path.isfile(dest):
            print(f'Moving {source} to {dest} and {item}')
            os.rename(source, dest)
        else:
            base, extension = os.path.splitext(item)
            ii = 1
            while True:
                new_name = os.path.join(folder_path,  base + " - Copy (" + str(ii) + ")" + extension)
                if not os.path.exists(new_name):
                    os.rename(source, new_name)
                    print(f'Moved and renamed {source} as {new_name}')
                    break
                ii += 1