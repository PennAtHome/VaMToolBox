@echo off
echo VaM ToolBox工具箱 by PennAtHome @ 2023
echo 这个工具快速生成预览图 与 对不同类型var进行分类排序
echo 你可以将这个文件放置在 Var 文件所有目录，然后执行本 bat 即可
echo .
pause

echo 即将生成预览图 [%1]
echo .

python VarToPreview.py %1

echo .
echo 预览图生成完毕，即将按类别进行分类归档（如果不需要分类，请关闭本窗口）
pause
echo .
python VarToSort.py %1
echo .
echo 全部执行完毕，按任意键结束
pause