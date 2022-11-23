import os 

seq_dir="/home/lukec/Documents/MA5114/FastQC/STEAK-master/testdata/test_dataset"
fastqc_dir="/home/lukec/Documents/MA5114/FastQC/STEAK-master/fastqc_output"

file_list=os.listdir(seq_dir)
print(seq_dir)

for seq in file_list:
    command="fastqc "+seq_dir+"/"+seq
    print(command)
    os.system(command)

    command1="mv "+seq_dir+"/"+"*.html "+fastqc_dir
    print(command1)
    os.system(command1)

    #command2="mv "+seq_dir+"/"+"*.zip"+fastqc_dir
    #print(command2)
    #os.system(command2)

    print("#done")

    
    
