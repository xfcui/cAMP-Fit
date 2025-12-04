# import os

# p1='cngc30.pdb'
# p2='5k8s.pdb'

# com='./TMalign '+p1+' '+p2+' -o ./tmout/TM_sup'
# os.system(com)

import os
import shutil
#from tqdm import tqdm

def get_files_in_directory(directory):
    # 获取目录中的所有文件和文件夹
    files = os.listdir(directory)
    
    # 只保留文件（排除文件夹）
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    return files

def rename_and_copy_file(source_file, destination_folder, new_name):
    # 检查源文件是否存在
    if not os.path.isfile(source_file):
        print(f"文件 {source_file} 不存在!")
        return

    # 获取文件扩展名
    file_extension = os.path.splitext(source_file)[1]

    # 创建目标文件夹（如果目标文件夹不存在）
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        #print(f"目标文件夹 {destination_folder} 已创建。")

    # 创建新的文件路径
    new_file_name = new_name + file_extension
    destination_path = os.path.join(destination_folder, new_file_name)

    # 复制文件并重命名
    shutil.copy(source_file, destination_path)

def getcmp(p):
    TMp='../data/00_tmalignout/TM_sup.pdb'
    outl=[]
    with open(TMp, 'r') as file:
        for line in file:
            x=line.split()
            if x[0]=='HETATM':
                outl.append(line)
                #print(len(x),line)
    outp=p+'/cmp.pdb'
    with open(outp, 'w') as filex:
        for item in outl:
            filex.write(item)

def docking(cngc_path,p,tnam):
    #print('*')
    TMp='../data/00_tmalignout/TM_sup.pdb'
    p0=cngc_path
    outl=[]
    with open(TMp, 'r') as file:
        for line in file:
            x=line.split()
            if x[0]=='HETATM':
                outl.append(line)
    #print(tnam,len(outl))
    if len(outl)==0:
        return
   
    with open(p0, 'r') as file:
        for line in file:
            outl.append(line)
    
    # lx=len(outl)
    # with open(TMp, 'r') as file:
    #     for line in file:
    #         x=line.split()
    #         if x[0]=='HETATM':
    #             outl.append(line)
    # if lx==len(outl):
    #     return
    pnam='/cngc-'+tnam+'.pdb'
    outp=p+pnam
    with open(outp, 'w') as filex:
        for item in outl:
            filex.write(item)
    resp='../data/02_tmalignresult_all'+pnam
    with open(resp, 'w') as filex:
        for item in outl:
            filex.write(item)

def align(cngc_path,template_path):
    print('[1/4] Docking cngc30 and cmp based on the template...')
    files = get_files_in_directory(template_path)
    for i in files:
        p2=cngc_path
        p1=template_path+'/'+i
        com='./TMalign '+p1+' '+p2+' -o ../data/00_tmalignout/TM_sup > TMout.txt'
        os.system(com)
        TMp='../data/00_tmalignout/TM_sup.pdb'
        tnam=i[:5]
    
        outp='../data/01_tmalignresult/'+tnam+''
        rename_and_copy_file(TMp, outp, tnam)
        getcmp(outp)
        docking(cngc_path,outp,tnam)

align('../data/cngc30.pdb','../data/p-cmp')