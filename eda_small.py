import pandas as pd
# from pandas_profiling import ProfileReport
import argparse
import os
import sweetviz as sv

class Eda():
    def __init__(self, df, dir):
        self.df = df
        self.dir = dir
        print("This is eda stage.")
        print (" Input    Library No")
        print ("=======  ================================")
        print ("  [1]    Visualization-1") # Pandas Profiling")
        print ("  [2]    Visualization-2") # SweetViz")
        # print ("  [3]    AutoViz")
        # print ("  [4]    Dtale")

        # lib = int(input("Enter library no: "))

    def prep_report(self, lib_no=1):
        self.lib_no = lib_no
        if self.lib_no == 1:
            # profile = ProfileReport(self.df)
            # profile.to_file(output_file=self.dir)
            pass
        elif self.lib_no == 2:
            #analyzing the dataset
            advert_report = sv.analyze(self.df)
            #display the report
            advert_report.show_html(self.dir)

