@echo off
echo VaM ToolBox������ by PennAtHome @ 2023
echo ������߿�������Ԥ��ͼ �� �Բ�ͬ����var���з�������
echo ����Խ�����ļ������� Var �ļ�����Ŀ¼��Ȼ��ִ�б� bat ����
echo .
pause

echo ��������Ԥ��ͼ [%1]
echo .

python VarToPreview.py %1

echo .
echo Ԥ��ͼ������ϣ������������з���鵵���������Ҫ���࣬��رձ����ڣ�
pause
echo .
python VarToSort.py %1
echo .
echo ȫ��ִ����ϣ������������
pause