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


# Output path
outpath = "/home/010/s/ss/ssy220000/CA_P2/out2/"

# Gem5 directory
Gem5dir = "/home/010/s/ss/ssy220000/CA_P2/gem5/"

# m5out2 path
m5out2_path = "/home/010/s/ss/ssy220000/CA_P2/m5out2/"

# Benchmark path
Bench401 = "/home/010/s/ss/ssy220000/CA_P2/Bench/401.bzip2/src/benchmark"
Bench429 = "/home/010/s/ss/ssy220000/CA_P2/Bench/429.mcf/src/benchmark"

# arguement path
arg401 = "/home/010/s/ss/ssy220000/CA_P2/Bench/401.bzip2/data/input.program"
arg429 = "/home/010/s/ss/ssy220000/CA_P2/Bench/429.mcf/data/input.program"


if __name__ == "__main__":
    for cache_size in range(0, 128, 8):
        print("###########################################################")
        print("########### simulating l1d cache " + str(cache_size) + " ##########")
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "l1d_size_" + str(cache_size) + "_401bzip2"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size="
            + str(cache_size)
            + "kB "
            + "--l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(0, 128, 8):
        print("###########################################################")
        print("########### simulating l1d cache " + str(cache_size) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "l1d_size_" + str(cache_size) + "_429mcf"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size="
            + str(cache_size)
            + "kB "
            + "--l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(0, 128, 8):
        print("###########################################################")
        print("########### simulating l1i cache " + str(cache_size) + " ##########")
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "l1i_size_" + str(cache_size) + "_401bzip2"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size="
            + str(cache_size)
            + "kB "
            + "--l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(0, 128, 8):
        print("###########################################################")
        print("########### simulating l1i cache " + str(cache_size) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "l1i_size_" + str(cache_size) + "_429mcf"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size="
            + str(cache_size)
            + "kB "
            + "--l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(1, 8):
        print("###########################################################")
        print("########### simulating l2 cache " + str(cache_size) + " ##########")
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "l2_size_" + str(cache_size) + "_401bzip2"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size="
            + str(cache_size)
            + "MB "
            + " --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(1, 8):
        print("###########################################################")
        print("########### simulating l2 cache " + str(cache_size) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "l2_size_" + str(cache_size) + "_429mcf"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size="
            + str(cache_size)
            + "MB "
            + " --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(8, 512, 8):
        print("###########################################################")
        print(
            "########### simulating cache line " + str(cache_size) + " ###############"
        )
        print("###############  bench 401.bzip2    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "cacheline_" + str(cache_size) + "_401bzip2"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench401)
            + " -o "
            + str(arg401)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size="
            + str(cache_size)
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])

    for cache_size in range(8, 512, 8):
        print("###########################################################")
        print("########### simulating cache line " + str(cache_size) + " ##########")
        print("###############  bench 429.mcf    ##########################")
        print("###########################################################")
        os.chdir(outpath)
        outpath2 = outpath + "cacheline_" + str(cache_size) + "_429mcf"
        os.mkdir(outpath2)
        os.chdir(Gem5dir)
        os.system(
            "./build/X86/gem5.opt -d ../m5out2 ./configs/example/se.py -I 500000000 -c "
            + str(Bench429)
            + " -o "
            + str(arg429)
            + " --cpu-type=timing --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size="
            + str(cache_size)
        )
        os.chdir(m5out2_path)
        subprocess.run(["cp", "stats.txt", outpath2])
