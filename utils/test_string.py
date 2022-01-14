from pathlib import PureWindowsPath

s1 = "E:/pyprj/SPConcreteTools/test_data_work/ex1/ex1.cdb"
s2 = str(PureWindowsPath(s1))
print(f'{s2=}')

s1 = "E:\pyprj\SPConcreteTools\test_data_work\ex1\ex1.cdb"
s3 = []
for c in s1:
    if c =='\\':
        s3.append('/')
    s3.append(c)

s4 = ''.join(s3)
print(f'{s4=}')    