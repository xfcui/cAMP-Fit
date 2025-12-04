import shutil
import os

def copy_folder_contents(src_folder, dst_folder):
    """
    复制源文件夹所有内容到目标文件夹
    
    Args:
        src_folder (str): 源文件夹路径
        dst_folder (str): 目标文件夹路径
    """
    try:
        # 确保目标文件夹存在
        os.makedirs(dst_folder, exist_ok=True)
        
        # 遍历源文件夹中的所有内容
        for item in os.listdir(src_folder):
            src_path = os.path.join(src_folder, item)
            dst_path = os.path.join(dst_folder, item)
            
            if os.path.isdir(src_path):
                # 如果是文件夹，递归复制
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            else:
                # 如果是文件，直接复制
                shutil.copy2(src_path, dst_path)
                
        #print(f"成功将 {src_folder} 的内容复制到 {dst_folder}")
        
    except Exception as e:
        print(f"复制过程中出错: {e}")

def get_pdb(src_folder, dst_folder):
    for item in os.listdir(src_folder):
            src_path = os.path.join(dst_folder, item)
            return src_path,item

def maketleap(pdbpath,tleapfolder):
    tleap = tleapfolder+'/tleap.in'
    with open(tleap,'w')as f:
        print(f"""source oldff/leaprc.ff99SB # 加载ff99SB力场
source leaprc.gaff # 加载 GAFF 力场
loadamberparams {tleapfolder}/cmp.frcmod # 加载分子力场参数
loadoff {tleapfolder}/cmp.lib # 加载分子库文件
cngc = loadpdb {pdbpath} # 加载分子 PDB 文件
saveamberparm cngc {tleapfolder}/cngc.prmtop {tleapfolder}/cngc.inpcrd # 保存拓扑和坐标文件
savepdb cngc {tleapfolder}/cngc.pdb # 保存溶剂化后的 PDB 文件
quit""",file=f)

def amber(md_path):
    p1 = f"tleap -f {md_path}/tleap.in > {md_path}/leap.log"
    p2 = f"sander -O -i {md_path}/min.in -o {md_path}/cngc_min.out -p {md_path}/cngc.prmtop -c {md_path}/cngc.inpcrd -r {md_path}/cngc_min.crd"
    p3 = f"ambpdb -p {md_path}/cngc.prmtop -c {md_path}/cngc_min.crd > {md_path}/cngc_min_result.pdb"
    print("🔹 [1/3] Running tleap to generate topology and coordinate files (prmtop / inpcrd)...")
    os.system(p1)
    print("🔹 [2/3] Running sander for energy minimization, please wait...")
    os.system(p2)
    print("🔹 [3/3] Converting minimized coordinates to PDB format...")
    os.system(p3)

def md():
    print('[3/4] Performing energy minimization using AMBER...')
    copy_folder_contents('../data/03_mincrashpdb', '../data/04_mdresult')
    copy_folder_contents('../data/mddefult', '../data/04_mdresult')
    pdb_path,pdb_name=get_pdb('../data/03_mincrashpdb', '../data/04_mdresult')
    maketleap(pdb_path,'../data/04_mdresult')
    amber('../data/04_mdresult')
    shutil.copy2('../data/04_mdresult/cngc_min_result.pdb','../result/'+pdb_name)

md()