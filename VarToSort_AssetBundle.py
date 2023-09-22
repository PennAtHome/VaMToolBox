
import os  
import zipfile  
import sys

# 指定目录  
dir_path = '.'  
out_path = './UnZipTemp'

# designed by pennathome @ 2023
# Var 文件分类归档工具，你可以将此.py放置于 Var 所有目录，然后执行本程序 (请先安装 Phtyon)
# 你可以访问 https://github.com/PennAtHome/VaMToolBox 获取最新版本

if __name__ == "__main__":  
    # 从命令行参数中获取路径  
    dir_path = sys.argv[1] if len(sys.argv) > 1 else "." 

def callFileMoveTo(from_path, to_path):
    to_dir  =   os.path.dirname(to_path)
    if (not os.path.exists(from_path)):
        return False
    if (not os.path.exists(to_dir)):
        os.makedirs(to_dir)  
    if (not os.path.exists(to_path)):   # 目标文件不存在
        os.rename(from_path, to_path)   # 执行移动
        return True
    else:
        return False

def checkPathAndMoveTo(file_path, in_path, from_path, to_path):
    if (in_path in file_path):
        to_dir  =   os.path.dirname(to_path)
        if (callFileMoveTo(from_path, to_path)):
            print(f"移动成功" + file_path)
            callFileMoveTo(from_path.replace(".var", ".jpg"), to_path.replace(".var", ".jpg"))
        else:
            print(f"【移动目标存在同名文件！{to_path}】")
        return True
    return False
  
input("即将开始归档不同类型 Var 文件，按回车键开始")
# 遍历指定目录下的所有zip文件  
count_zip = 0
count_sorted = 0
count_sortin = 0
count_sortOut = 0

for zip_path in os.listdir(dir_path):  
    if zip_path.endswith('.var'): 
        count_zip += 1
        # 获取zip文件名
        zip_name = os.path.splitext(zip_path)[0]
        sou_path = os.path.join(dir_path, zip_path)
        # print(f"path:" + zip_path + " name:" + zip_name)
        # input("按回车键继续")
        # break
        
        try:
            with zipfile.ZipFile(os.path.join(dir_path, zip_path), 'r') as zip_file:    #  打开 Zip 文件
                outputed  = False
                file_list = zip_file.namelist()     #zip_ref.extractall(output_dir) 

            if (outputed == False): 
                to_path =   os.path.join(dir_path, "AssetBundles", zip_path)
                for file_name in file_list:
                    if (checkPathAndMoveTo(file_name, ".assetbundle", sou_path, to_path)):
                        outputed = True
                        break
            if (outputed == False): 
                to_path =   os.path.join(dir_path, "Scenes", zip_path)
                for file_name in file_list:  
                    if (checkPathAndMoveTo(file_name, "Saves/scene", sou_path, to_path)):
                        outputed = True
                        break
            if (outputed == False): 
                to_path =   os.path.join(dir_path, "Poses", zip_path)
                for file_name in file_list:  
                    if (checkPathAndMoveTo(file_name, "Saves/Person/Pose", sou_path, to_path) or
                        checkPathAndMoveTo(file_name, "Saves/Person/pose", sou_path, to_path) or
                        checkPathAndMoveTo(file_name, "Custom/Atom/Person/Pose", sou_path, to_path) or    # 动作
                        checkPathAndMoveTo(file_name, "Custom/Atom/Person/Morphs", sou_path, to_path)):   # 表情
                        outputed = True
                        break
            if (outputed == False): 
                to_path =   os.path.join(dir_path, "Cloths", zip_path)
                for file_name in file_list:  
                    if (checkPathAndMoveTo(file_name, "Custom/Clothing", sou_path, to_path)):
                        outputed = True
                        break
            if (outputed == False): 
                to_path =   os.path.join(dir_path, "Atoms", zip_path)
                for file_name in file_list:  
                    if (checkPathAndMoveTo(file_name, "Custom/Atom", sou_path, to_path)):
                        outputed = True
                        break
            if (outputed == False): 
                to_path =   os.path.join(dir_path, "Hairs", zip_path)
                for file_name in file_list:  
                    if (checkPathAndMoveTo(file_name, "Custom/Hair", sou_path, to_path)):
                        outputed = True
                        break
            if (outputed == False): 
                to_path =   os.path.join(dir_path, "Scripts", zip_path)
                for file_name in file_list:  
                    if (checkPathAndMoveTo(file_name, "Custom/Scripts", sou_path, to_path)):
                        outputed = True
                        break
            if (outputed == True):
                count_sorted += 1
                if (os.path.exists(zip_path)):  # 移除原文件
                    os.remove(zip_path)
                    count_sortin += 1
            else:
                count_zip += 1
        #     delete_folder(out_path)
        except:
           print(f"解压失败！" + zip_path)
input(f"归档结束，共var文件: {count_zip} | 归档 {count_sorted} / 重复 {count_sortin} | 未归档 {count_sortOut}，按回车键结束")
