import os
from Bio import PDB
import numpy as np
import shutil

def get_files_in_directory(directory):
    # 获取目录中的所有文件和文件夹
    files = os.listdir(directory)
    
    # 只保留文件（排除文件夹）
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    return files

def extract_atom_info(pdb_file):
    # 解析 PDB 文件
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', pdb_file)
    
    atom_info = []

    # 遍历结构中的每个模型，每个链和每个残基中的每个原子
    for model in structure:
        for chain in model:
            for residue in chain:
                # 获取残基类型（例如：ALA，GLY）
                residue_type = residue.get_resname()

                # 获取残基编号
                residue_id = residue.get_id()[1]  # 获取编号（如果存在插入码，则只获取编号部分）

                for atom in residue:
                    # 获取原子名称
                    atom_name = atom.get_name()
                    
                    # 获取原子的元素符号（例如：C，N，O）
                    atom_element = atom.element
                    
                    # 获取原子坐标
                    atom_coord = atom.get_coord()

                    # 将信息存储在列表中
                    atom_info.append({
                        'residue_type': residue_type,
                        'residue_id': residue_id,
                        'atom_name': atom_name,
                        'atom_element': atom_element,
                        'atom_coord': atom_coord
                    })
    
    return atom_info

def print_atom_info(atom_info):
    o1=[]
    o2=[]
    o3=[]
    o4=[]
    for info in atom_info:
        o1.append(info['residue_type']) 
        #atom_name = info['atom_name']
        o2.append(info['atom_element'])
        o3.append(info['atom_coord'])
        o4.append(info['residue_id'])
        #print(f"Residue: {residue_type}, Atom: {atom_name}, Element: {atom_element}, Coordinates: {atom_coord}")
    return o1,o2,o3,o4

def checkcrash(aligned_cngc_path):
    print('[4/4] Results have been saved to the result folder.')
    dicr={'H':0.32,'C':0.77,'N':0.75,'O':0.73,'S':1.02,'FE':0.76,'P':1.10}
    files = get_files_in_directory(aligned_cngc_path)
    num=0
    mincrash=10010
    minname=''
    for o in files:
        pdb_file = aligned_cngc_path+'/'+o  # 请替换为你的 PDB 文件路径
        atom_info = extract_atom_info(pdb_file)
        res,ele,coord,rid=print_atom_info(atom_info)
    # for j in ele:
    #     if j not in dicr:
    #         print(j)

        pe=[]
        pc=[]
        le=[]
        lc=[]
        for i in range(len(res)):
            if res[i]=='CMP':
                le.append(ele[i])
                lc.append(coord[i])
            else:
                if rid[i]>500:
                    pe.append(ele[i])
                    pc.append(coord[i])
    #print(len(pe),len(le))
        crash=0
        for i in range(len(le)):
            for j in range(len(pe)):
                dis=np.linalg.norm(lc[i] - pc[j]) - (dicr[le[i]]+dicr[pe[j]])
                if dis<0:
                    crash=crash+1
        num=num+1
        #print(o,num,len(files),len(le),crash)
        

checkcrash('../result')