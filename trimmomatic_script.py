
# script can use the conda installation of Trimmomatic if you don't include "java -jar..."


import os
seq_dir = '/home/lukec/Documents/MA5114/FastQC/STEAK-master/testdata/test_dataset'
trim_out = '/home/lukec/Documents/MA5114/FastQC/STEAK-master/testdata/trimmed_out'
standard1 =' SE -phred33 ' 
standard2 = ' ILLUMINACLIP:/home/lukec/Documents/MA5114/FastQC/trimmomatic-0.39/adapters/TruSeq3-SE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'


file_list = os.listdir(seq_dir)
print('# got list of files in: ' + seq_dir)

os.mkdir(trim_out)
print('# created subdir: ' + trim_out)
                                                      

for seq in file_list:
   command_trim = "java -jar /home/lukec/Documents/MA5114/FastQC/trimmomatic-0.39/trimmomatic-0.39.jar" + standard1+ seq_dir + '/' + seq +' ' + trim_out + '/' + seq +'.trimmed' + standard2
   print(command_trim)
   os.system(command_trim)

#this is configured for my file system, you'll need to change the directories at seq_dir and trim_out
#also need to reference where you have installed trimmomatic


