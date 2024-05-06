import pandas as pd
# from pandas_profiling import ProfileReport
import argparse
import os
import sweetviz as sv

class ReadFile():
    def __init__(self, fname, base_dir=None, typ='csv'):
        self.fname = fname
        self.base_dir = base_dir
        self.typ = typ

    def read_file(self):
        if self.base_dir:
            file = os.path.join(self.base_dir, self.fname)
        else:
            file = self.fname
            print(file)

        # read different type of files
        isFile = os.path.isfile(file)
        if isFile:
            if self.typ==1:
                df = pd.read_csv(file)
                name = self.fname[:-4]
                print(df.head, name)
            elif self.typ==2:
                df = pd.read_excel(file)
                name = self.fname[:-5]
            elif self.typ==3:
                df = pd.read_json(file)
                name = self.fname[:-5]
            elif self.typ==4:
                df = pd.read_pickle(file)
                name = self.fname[:-4]
            elif self.typ==5:
                df = pd.read_hdf(file)
                name = self.fname[:-3]
            else:
                print("File type not supported.")

            if self.base_dir:
                self.des_file = os.path.join(self.base_dir, (name+"_report.html"))
            else:
                self.des_file = name + "_report.html"
            self.df = df
            return self.df, self.des_file

        else:
            print("This file is not present in the directory")

