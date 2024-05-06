# importing libraries
import argparse
import os
import time 
from eda_small import Eda
from read_file import ReadFile
start_time = time.time()

#to print the banner
def main():
    if os.name == 'nt':
        os.system('cls')
    banner = """\u001b[36m

       _           _        ______ _____            _______          _ 
      | |         | |      |  ____|  __ \   /\     |__   __|        | |
   ___| |__   ___ | | ___  | |__  | |  | | /  \       | | ___   ___ | |
  / __| '_ \ / _ \| |/ _ \ |  __| | |  | |/ /\ \      | |/ _ \ / _ \| |
 | (__| | | | (_) | |  __/ | |____| |__| / ____ \     | | (_) | (_) | |
  \___|_| |_|\___/|_|\___| |______|_____/_/    \_\    |_|\___/ \___/|_|
                                                                                                              

\u001b[32m coded with <3 by Vishwa end to end CLI based tool for a daily data scientist\u001b[0m
                            \u001b[32m version 1.0\u001b[0m
                        \u001b[32m Please support US  \u001b[0m
    """

    #user selection options to drive user in the defined dataframe by the organization
    print(banner + ("Tip: You can use chole tool via arguments as well check the help(python chole.py -h) menu for more information"))
    print (" Input    Description")
    print ("=======  ===========================================================================================")
    print ("  [1]    Project Setup")
    print ("  [2]    Data Collection")
    print ("  [3]    Quick EDA for smaller dataset")
    print ("  [4]    EDA for lager datasets")
    print ("  [5]    Data Pre-processing")
    print ("  [6]    Data Imputation")
    print ("  [7]    Feature Engineering")
    print ("  [8]    Model Development")
    print ("  [9]    Read manual")
    print ("  [0]    Exit Chole :( \n")

## Parser for help 
    # parser = argparse.ArgumentParser(description='Chole a parameter discovery suite')
    # parser.add_argument('-A' ,'--aws' , help = 'To collect data from AWS s3 [ex : --bucket name or storage name]' , required=True)
    # parser.add_argument('-G' ,'--gcp' , help = 'To collect data from GCP [ex : --bucket name or storage name ]' , default=True, required=True)
    # parser.add_argument('-M','--microsoft' ,  help = 'For nested parameters [ex : --bucket name or storage name]' , required=True)
    # parser.add_argument('-S','--snowflake', help= 'extensions to exclude [ex --bucket name or storage name]' , required=True)
    # parser.add_argument('-R','--redshift', help= 'extensions to exclude [ex --bucket name or storage name]' , required=True)
    # parser.add_argument('-o','--output' , help = 'Output file name [by default it is \'.txt\' please mention other formatt you would need]' , default=True)
    # parser.add_argument('-p','--placeholder' , help = 'The string to add as a placeholder after the parameter name.', default = "FUZZ")
    # parser.add_argument('-q', '--quiet', help='Do not print the results to the screen', action='store_true')
    # parser.add_argument('-r', '--retries', help='Specify number of retries for 4xx and 5xx errors', default=3)
    # args = parser.parse_args()
    df = None
    # function to define project setup
    def step1():
        pass
    # function for data collection
    def step2():
        fname = input("Enter file name: ")
        base_dir = input("Enter base directory else 0: ")
        if base_dir == "0":
            base_dir = None
        print (" Input    File Type")
        print ("=======  ================================")
        print ("  [1]    csv")
        print ("  [2]    xls")
        print ("  [3]    json")
        print ("  [4]    pkl")
        print ("  [5]    h5")
        typ = int(input("Enter file type: "))
        readfile = ReadFile(fname=fname, base_dir=base_dir, typ=typ)
        df, des = readfile.read_file()
        return df, des
    # function to define eda
    def step3(df, des):
        eda = Eda(df, des)
        lib_no = int(input("Enter Library No: "))
        eda.prep_report(lib_no=lib_no)

    # take user input of the step number
    step = int(input("Enter step no: "))
    # 1 = project setup
    if step == 1:
        pass
    # 2 = data collection
    elif step == 2:
        df, des = step2()
        print(des, df.head())
        # if the user wants to move to eda from data collection
        next = int(input("Want to do EDA? yes-1 or no-0: "))
        # if yes, calling step 3, eda
        if next:
            step3(df, des)
    # 3 = eda
    elif step == 3:
        # calling step 2 to read the dataframe
        df, des = step2()
        step3(df, des)

    else:
        print("Please enter a valid step number.")

# https://stackoverflow.com/questions/36166225/using-the-same-option-multiple-times-in-pythons-argparse
if __name__ == "__main__":
    main()