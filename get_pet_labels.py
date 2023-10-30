#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ajit Kumar
# DATE CREATED:    18 OCT 2023                           
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from adjust_results4_isadog import adjust_results4_isadog
from classify_images import classify_images


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic={}
    file_ls=listdir(image_dir)
    
    for file in file_ls:
        if results_dic.get(file)!= None or file[0]=='.':
            continue
        else:
            current_label=""
            words=file.split('_')
            for word in words:
              if(word.isalpha()):
                current_label+=' '+word
            results_dic[file] =[current_label.strip().lower()]
    return results_dic


# code for debugging purpose

# ans=get_pet_labels('./uploaded_images/')
# print(ans)

# classify_images('./uploaded_images/',ans, 'alexnet')
# adjust_results4_isadog(ans ,'./dognames.txt')
# print('/n/n', ans)


