#!/usr/bin/python

from syswitch import printsys
from syswitch import checksysv

def logo():
    logo = '''
   mm   ""#    ""#      mmm  #                    #     
   ##     #      #    m"   " # mm    mmm    mmm   #   m 
  #  #    #      #    #      #"  #  #"  #  #"  "  # m"  
  #mm#    #      #    #      #   #  #""""  #      #"#   
 #    #   "mm    "mm   "mmm" #   #  "#mm"  "#mm"  #  "m 
    '''
    print(logo)
    print("Author By Vlary!")
    print("Version 0.01b!")
    print("Welcom to AllCheck!")

if __name__ == "__main__":
    logo()
    printsys()
    checksysv()
