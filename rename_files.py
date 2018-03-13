import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir('/Users/ndeyisatoujobe/Desktop/udacity/Programming_Foundations_with_Python/file_rename/prank')
    #print (file_list)
    saved_path = os.getcwd()
    #print("Current Working Directory is "+saved_path)
    os.chdir('/Users/ndeyisatoujobe/Desktop/udacity/Programming_Foundations_with_Python/file_rename/prank')
    # (2) for each file, rename filename
    for file_name in file_list:
        print('Old Name - ' + file_name)
        os.rename(file_name, file_name.translate(None,'0123456789'))
        print('New Name - ' + file_name.translate(None,'0123456789'))
    os.chdir (saved_path)          
rename_files()
