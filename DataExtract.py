import os
import subprocess
from pathlib import Path
from os.path import exists


# Output path
root= "D:\\UTD_Laptop\\Course_work\\Computer_Architecture\\P2\\out\\"

def ExtractData():
    for subdir,dirs,files in os.walk(root):
        for file in files:
            temppath = os.path.join(subdir,file)
            foldername = temppath.split("\\")[7]            
            testname = foldername.split("_")[0]  
            print(temppath)          
            if testname == 'cacheline':               
               testvalue = foldername.split("_")[1]
               benchtype = foldername.split("_")[2]
            else:
               testvalue = foldername.split("_")[2]
               testtype  = foldername.split("_")[1]
               benchtype = foldername.split("_")[3]  
               
            
            with open(temppath,'r') as f:
                 lines = f.readlines()
                 print ("Extracting " +testname + "  " + testvalue + "  " + benchtype  )
                 
                 
                 for line in lines:                      
                      if "system.cpu.dcache.overall_misses" in line:                           
                           Dnummisses = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Dcache over all miss : " + Dnummisses.split()[1] + "\n")
                      if "system.cpu.dcache.overall_miss_rate" in line:
                           Dmissrate = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Dcache miss rate : " + Dmissrate.split()[1] + "\n")
                      if "system.cpu.icache.overall_misses" in line:
                           Inummisses = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Icache miss rate : " + Inummisses.split()[1] + "\n")
                      if "system.cpu.icache.overall_miss_rate" in line:
                           Imissrate = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Icache miss rate :" + Imissrate.split()[1] + "\n")
                      if "system.l2.overall_misses::total" in line:
                           Lnummisses = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Icache miss rate :" + Lnummisses.split()[1] + "\n")
                      if "system.l2.overall_miss_rate::total:" in line:
                           Lmissrate = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Icache miss rate :" + Lmissrate.split()[1] + "\n")
                           
                      if "system.cpu.dcache.overallMisses::total" in line:                           
                           Dnummisses = line
                           if testname == 'cacheline':
                               outfile.write (testname + "  " + testvalue + "  " + benchtype )
                           else:
                                outfile.write (testname + "  " + testtype +"  "+ testvalue + "  " + benchtype)
                           outfile.write (" Dcache_over_all_miss : " + Dnummisses.split()[1] + " ")
                      
                      if "system.cpu.icache.overallMisses::total" in line:
                           Inummisses = line                           
                           outfile.write (" Icache_Overall_miss: " + Inummisses.split()[1] + " ")
                      
                      if "system.l2.overallMisses::total " in line:
                           Lnummisses = line                          
                           outfile.write (" L2cache_Overall_miss :" + Lnummisses.split()[1] + "\n")
               

if __name__ == "__main__":
   outfile = open("outfile.txt","w+")
   ExtractData() 
   outfile.close()