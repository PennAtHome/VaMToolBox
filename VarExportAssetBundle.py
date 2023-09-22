
import os  
import zipfile  
import shutil
import sys

# designed by pennathome @ 2023
# Var AssetBundle 文件提取工具，你可以将此.py放置于 Var 所有目录，然后执行本程序 (请先安装 Phtyon)
# 你可以访问 https://github.com/PennAtHome/VaMToolBox 获取最新版本
  
def delete_folder(folder_path, deep=True):  
    if os.path.exists(folder_path):  
        shutil.rmtree(folder_path, ignore_errors=not deep)  
        print(f"Folder {folder_path} deleted successfully.")  
    else:  
        print(f"Folder {folder_path} does not exist.")

# 指定目录  
dir_path = '.'  
out_path = './UnZipAssetBundle'

if __name__ == "__main__":  
    # 从命令行参数中获取路径  
    dir_path = sys.argv[1] if len(sys.argv) > 1 else "." 
  
unknowList  =   ''
# 遍历指定目录下的所有zip文件  
for zip_path in os.listdir(dir_path):  
    if zip_path.endswith('.var'):  
        # 获取zip文件的上一层目录名  
        base_name = os.path.basename(os.path.dirname(zip_path))
        # 创建解压后的文件存放目录  
        output_dir = os.path.join(out_path, base_name)  
        zip_name = os.path.splitext(zip_path)[0]
        try:
            with zipfile.ZipFile(os.path.join(dir_path, zip_path), 'r') as zip_file:    #zip_ref:  
                file_list = zip_file.namelist()     #zip_ref.extractall(output_dir)  

                if not os.path.exists(output_dir):  
                    os.makedirs(output_dir)  

                outputed = False
                outputPath  =   ""
                for file_name in file_list:  
                    if '.assetbundle' in file_name: # == ".assetbundle"
                        outputPath  =   os.path.join(out_path, file_name)
                        if not os.path.exists(outputPath):    # 文件不存在，则解压
                            zip_file.extract(file_name, out_path)
                            print(f"解压 AssetBundle : " + file_name)
                            outputed = True
                        else:
                            print(f"已存在 AssetBundle : " + file_name)
                    elif '.scene' in file_name and 'Custom/Assets' in file_name:  # == '所需的文件名':  
                        # 使用 ZipFile.extractfile() 方法获取文件的文件对象  
                        outputPath  =   os.path.join(out_path, file_name)
                        if not os.path.exists(outputPath):    # 文件不存在，则解压
                            zip_file.extract(file_name, out_path)
                            print(f"解压 Assets.Scene : " + file_name)
                            outputed = True
                        else:
                            print(f"已存在 Assets.Scene : " + file_name)
                    elif 'Custom/Assets' in file_name:  # 不知名类型
                        print(f"未知类型：" + file_name)
                        unknowList = unknowList + "\n" + file_name
        except:
            print(f"解压失败！" + zip_path)

unknowPath  =   os.path.join(out_path, "unknow.log")
f = open(unknowPath, "w")
f.write(unknowList)
f.close()