#####################################################################################################################################################
#####################################################################################################################################################
#########################   Author: Shishir Sunil Yalburgi                                                           ################################
#########################   NET ID: SSY220000                                                                        ################################
#########################   Version: 2.0.1                                                                           ################################
#########################   Email ID: ssy220000@utdallas.edu                                                         ################################
#########################   This python script automates CE6304 Project 2                                            ################################
#####################################################################################################################################################
#####################################################################################################################################################


import os
import subprocess


# out1put path
out1path = "/home/010/s/ss/ssy220000/CA_P2/out1/"

# Gem5 directory
Gem5dir = "/home/010/s/ss/ssy220000/CA_P2/gem5/"

# m5out1 path
m5out1_path = "/home/010/s/ss/ssy220000/CA_P2/m5out1/"

# Benchmark path
Bench401 = "/home/010/s/ss/ssy220000/CA_P2/Bench/401.bzip2/src/benchmark"
Bench429 = "/home/010/s/ss/ssy220000/CA_P2/Bench/429.mcf/src/benchmark"

# arguement path
arg401 = "/home/010/s/ss/ssy220000/CA_P2/Bench/401.bzip2/data/input.program"
arg429 = "/home/010/s/ss/ssy220000/CA_P2/Bench/429.mcf/data/input.program"


if __name__ == "__main__":
    for assoc in range(1, 8, 1):
        print("###########################################################")
        print("########### simulating L1D assoc " + str(assoc) + " ##########")
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(out1path)
        out1path2 = out1path + "L1d_assoc_" + str(assoc) + "_401bzip2"
        os.mkdir(out1path2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out1 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc="
            + str(assoc)
            + " --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out1_path)
        subprocess.run(["cp", "stats.txt", out1path2])

    for assoc in range(1, 8, 1):
        print("###########################################################")
        print("########### simulating L1D assoc " + str(assoc) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(out1path)
        out1path2 = out1path + "L1d_assoc_" + str(assoc) + "_429mcf"
        os.mkdir(out1path2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out1 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc="
            + str(assoc)
            + " --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out1_path)
        subprocess.run(["cp", "stats.txt", out1path2])

    for assoc in range(0, 88, 2):
        print("###########################################################")
        print("########### simulating L1I assoc " + str(assoc) + " ##########")
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(out1path)
        out1path2 = out1path + "L1i_assoc_" + str(assoc) + "_401bzip2"
        os.mkdir(out1path2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out1 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc="
            + str(assoc)
            + " --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out1_path)
        subprocess.run(["cp", "stats.txt", out1path2])

    for assoc in range(0, 88, 2):
        print("###########################################################")
        print("########### simulating L1I assoc " + str(assoc) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(out1path)
        out1path2 = out1path + "L1i_assoc_" + str(assoc) + "_429mcf"
        os.mkdir(out1path2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out1 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc="
            + str(assoc)
            + " --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out1_path)
        subprocess.run(["cp", "stats.txt", out1path2])

    for assoc in range(0, 16384, 256):
        print("###########################################################")
        print("########### simulating L2 assoc " + str(assoc) + " ##########")
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(out1path)
        out1path2 = out1path + "L2_assoc_" + str(assoc) + "_401bzip2"
        os.mkdir(out1path2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out1 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc="
            + str(assoc)
            + " --cacheline_size=64"
        )
        os.chdir(m5out1_path)
        subprocess.run(["cp", "stats.txt", out1path2])

    for assoc in range(0, 16384, 258):
        print("###########################################################")
        print("########### simulating L2 assoc " + str(assoc) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(out1path)
        out1path2 = out1path + "L2_assoc_" + str(assoc) + "_429mcf"
        os.mkdir(out1path2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out1 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc="
            + str(assoc)
            + " --cacheline_size=64"
        )
        os.chdir(m5out1_path)
        subprocess.run(["cp", "stats.txt", out1path2])
