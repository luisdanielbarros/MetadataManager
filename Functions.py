from pyexiv2 import Image
import os, stat
from datetime import datetime
from shutil import copyfile, copy, copy2
import mimetypes
import hashlib
import Variables, Classes
from PIL import Image as PILImage

#Check if url points to an image
def is_url_image(url):    
    return (url.endswith(".jpg") or url.endswith(".jpeg") or url.endswith(".png"))

#Add metadata
def add_metadata(dst, hashcode):
    if (is_url_image(dst) == False):
        return
    img = Image(dst)
    img.modify_xmp({'Xmp.dc.stamp': hashcode})
    img.modify_xmp({'Xmp.dc.creator': Variables.creator_name})
    img.modify_xmp({'Xmp.dc.description': Variables.files_description})
    img.modify_xmp({'Xmp.dc.source': Variables.files_source})
    img.close()

#Watermark image
def watermark_image(image_url, watermark_url):
    image_to_watermark = PILImage.open(image_url)
    watermark_image = PILImage.open(watermark_url)
    image_to_watermark.paste(watermark_image, (0, 0), watermark_image)
    image_to_watermark.save(image_url,"PNG")

#Copy & paste your files, metadata is added after copying each file into existence
def copytree(src, dst, hashcode, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                os.makedirs(d)
            copytree(s, d, hashcode, symlinks, ignore)
        else:
            copy2(s, d)
            add_metadata(d, hashcode)

#Copy & paste your images, metadata is added after copying each file into existence
def copyimages(raw_images_directory, export_url, hashcode, symlinks=False, ignore=None):
        count = 0;
        #For each comic
        for directory in raw_images_directory:
            #For each directory
            for directory_item in os.listdir(directory.source_url):
                subdirectory = os.path.join(directory.source_url, directory_item)
                print(subdirectory)
                if os.path.isdir(subdirectory):
                    #For each image
                    for subdirectory_item in os.listdir(subdirectory):
                        print(count)
                        count += 1
                        s = os.path.join(subdirectory, subdirectory_item)
                        d = os.path.join(export_url, str(count)+".png")
                        if os.path.isdir(s):
                            print('Warning: copyimages function found a directory! This function completely ignores directions and the items inside them. You may want to use copytree instead.')
                        else:
                            copy2(s, d)
                            add_metadata(d, hashcode)
                            watermark_image(d, Variables.watermark)

#Create a base exportation directory
def create_exportation_directory():
    timestamp = str(datetime.timestamp(datetime.now()))
    export_url = Variables.default_export+" "+timestamp
    if not os.path.exists(export_url):
        os.makedirs(export_url)
    return export_url

#Create an exportation subdirectory
def create_exportation_subdirectory(export_url, folder_name):
    subdirectory = export_url+"\\"+folder_name
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
    return subdirectory;

#Create an hash code and store it in a directory
def hash_store(seed, directory):
    hash_code = hashlib.md5(seed.encode('utf-8')).hexdigest()
    f = open(directory+"\hash.txt", "a")
    f.write(seed+"\n")
    f.write(hash_code+"\n")
    f.close()
    return hash_code