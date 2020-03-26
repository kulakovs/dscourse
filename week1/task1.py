import sys
import os
import re


def split_file(file_in, file_out):
    f_in = open(file_in)
    f_out = open(file_out, 'w')
    lines = f_in.read()
    result = re.findall('\d+|[a-zA-Zа-яА-Я-]+|[^\w\s+]', lines)
    f_out.write(' '.join(result))
    f_in.close()
    f_out.close()


if len(sys.argv)>1:
    in_dir = sys.argv[1]
else:
    print('Empty directory.')

out_dir = 'out_folder_1'

filelist = list(os.listdir(in_dir))

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for in_f in filelist:
  split_file(in_dir+'/'+in_f,out_dir+'/'+in_f)
