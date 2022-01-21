# +============================================================================+
# | Company:   SOFiSTiK AG                                                     |
# | Version:   SOFiSTIK 2020                                                   |
# +============================================================================+

import os             # for the environment variable necessary
import platform       # checks the python platform
from ctypes import *  # read the functions from the cdb
from sofistik_daten import *
from elements import *

from pathlib import PureWindowsPath

# 64bit DLLs
os.add_dll_directory(r"C:\Program Files\SOFiSTiK\2020\SOFiSTiK 2020\interfaces\64bit")
os.add_dll_directory(r"C:\Program Files\SOFiSTiK\2020\SOFiSTiK 2020")

# Get the DLL functions
lib = 'sof_cdb_w-70.dll'

myDLL = cdll.LoadLibrary(lib)
py_sof_cdb_get = cdll.LoadLibrary(lib).sof_cdb_get
py_sof_cdb_put = cdll.LoadLibrary(lib).sof_cdb_put
py_sof_cdb_del = cdll.LoadLibrary(lib).sof_cdb_del

py_sof_cdb_get.restype = c_int

py_sof_cdb_kenq = cdll.LoadLibrary(lib).sof_cdb_kenq_ex
py_sof_cdb_kexist = cdll.LoadLibrary(lib).sof_cdb_kexist


# Connect to CDB
Index = c_int()
cdbIndex = 99

# Set the CDB Path
def SetBase(s):
    fileName = PureWindowsPath(s)
    return str(fileName)

fileName = SetBase('E:/pyprj/SPConcreteTools/test_data_work/ex1/ex1.cdb')

# important: Unicode call!
Index.value = myDLL.sof_cdb_init(fileName.encode('utf-8'), cdbIndex)

cdbStat = c_int()  # get the CDB status
cdbStat.value = myDLL.sof_cdb_status(Index.value)

# Print the Status of the CDB
print ("CDB Status:", cdbStat.value)


###########################################################
# READ FROM CDB
"""
do while ie == 0, see cdbase.chm, Returnvalue.
    = 0 -> No error
    = 1 -> Item is longer than Data
    = 2 -> End of file reached
    = 3 -> Key does not exist
"""

#read and save list of structural areas
structural_areas = []
key1 = 32
key2 = 0
func = cgln_matc

if py_sof_cdb_kexist(key1, key2) == 2: # the key exists and contains data
    ie = c_int(0)
    RecLen = c_int(sizeof(func))
    while ie.value == 0:
        ie.value = py_sof_cdb_get(Index, key1, key2, byref(func), byref(RecLen), 1)
        structural_areas.append(func.m_nr)

print(f'{structural_areas=}')

# for a in structural_areas:

#     key1 = 32
#     key2 = a
#     func = cgar

#     if py_sof_cdb_kexist(key1, key2) == 2: # the key exists and contains data
#         ie = c_int(0)
#         RecLen = c_int(sizeof(func))
#         while ie.value == 0:
#             ie.value = py_sof_cdb_get(Index, key1, key2, byref(func), byref(RecLen), 1)
#             # print(f'{func.m_id=}')
#             # if func.m_id==0:
#             #     print(f'group {func.m_nog=}')
#             #     print(f'thickness {func.m_td[0]=} m')
#         # if func.m_id==10:
#         #     print(f'{func.m_box[1][1]=}')
def SarsRead(int_id):
    key1 = 39
    key2 = 0
    func = csar

    print(f'{py_sof_cdb_kexist(key1, key2)=}')
    if py_sof_cdb_kexist(key1, key2) == 2: # the key exists and contains data
        
        ie = c_int(0)
        RecLen = c_int(sizeof(func))
        while ie.value < 2:
        # while ie.value == 0:
            ie.value = py_sof_cdb_get(Index, key1, key2, byref(func), byref(RecLen), 1)
            # print(f'{ie.value=}')
            if func.m_id == 200 and func.m_ids==1001:
                print(f'group {func.m_nog=}')
                print(f'material {func.m_nom=}')
                print(f'group {func.m_nog=}')
                print(f'thickness {func.m_td[0]=}')
                print(f'thickness {func.m_td[2]=}')



SarsRead(1004)
# class Node():
#     def __init__(self,nr,kfix=127,xyz=(0,0,0),pz=0):
#         self.nr = nr
#         self.kfix = kfix
#         self.xyz = xyz
#     Pz = 0

# #read and save nodes with supports
# k1 = 20
# k2 = 0
# func = cnode
# nodes = []

# if py_sof_cdb_kexist(k1, k2) == 2: # the key exists and contains data
#     ie = c_int(0)
#     RecLen = c_int(sizeof(func))
#     while ie.value == 0:
#         ie.value = py_sof_cdb_get(Index, k1, k2, byref(func), byref(RecLen), 1)
#         if func.m_nr > 0:
#             if func.m_kfix !=127:
#                 xyz = (func.m_xyz[0],func.m_xyz[1],func.m_xyz[2])
#                 nodes.append(Node(func.m_nr,func.m_kfix,xyz))
#         RecLen = c_int(sizeof(func))

# def Clean_Nodes(nodes):
#     nr = []
#     clean_nodes = []
#     for n in nodes:
#         if n.nr not in nr:        
#             nr.append(n.nr)
#             clean_nodes.append(n)
#     return(nr,clean_nodes)

# (node_numbers,nodes) = Clean_Nodes(nodes)
# # print(f'I have nodes {node_numbers}')
# # for n in nodes:
# #     print(n.nr,n.kfix,n.xyz)


# #read support forces
# k1 = 24
# k2 = 1
# func = cn_disp

# if py_sof_cdb_kexist(k1, k2) == 2: # the key exists and contains data
#     ie = c_int(0)
#     RecLen = c_int(sizeof(func))
#     while ie.value == 0:
#         ie.value = py_sof_cdb_get(Index, k1, k2, byref(func), byref(RecLen), 1)
#         if func.m_nr in node_numbers:
#             for n in nodes:
#                 if func.m_nr == n.nr:
#                     n.Pz = func.m_pz
#         RecLen = c_int(sizeof(func))

# print('Add support forces')
# for n in nodes:
#     print(n.nr,n.kfix,n.xyz,n.Pz)









# Close the CDB, 0 - will close all the files
myDLL.sof_cdb_close(0)

# Print again the status of the CDB, if status = 0 -> CDB Closed successfully
cdbStat.value = myDLL.sof_cdb_status(Index.value)
if cdbStat.value == 0:
    print ("CDB closed successfully, status = 0")