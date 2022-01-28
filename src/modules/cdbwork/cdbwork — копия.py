# +============================================================================+
# | Company:   SOFiSTiK AG                                                     |
# | Version:   SOFiSTIK 2020                                                   |
# +============================================================================+

import os             # for the environment variable necessary
import platform       # checks the python platform
from ctypes import *  # read the functions from the cdb
from sofistik_daten import *
from ..classes import *

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
        structural_areas.append(Area(func.m_nr))

#read cdb and update existing Area class parameters

def SarsRead(area):
    key1 = 39
    key2 = 0
    func = csar

    print(f'{py_sof_cdb_kexist(key1, key2)=}')
    if py_sof_cdb_kexist(key1, key2) == 2: # the key exists and contains data
        ie = c_int(0)
        RecLen = c_int(sizeof(func))
        while ie.value < 2:
            ie.value = py_sof_cdb_get(Index, key1, key2, byref(func), byref(RecLen), 1)
            if func.m_id == 200 and func.m_ids==area.id:
                area.group = func.m_nog
                print(f'group {func.m_nog=}')
                area.material = func.m_nom
                print(f'material {func.m_nom=}')
                area.thickness = round(func.m_td[0],3)
                print(f'thickness {func.m_td[0]=}')

    #read cdb and update area quad elements list
    key1 = 32
    key2 = area.id
    func = cgar_elnr

    if py_sof_cdb_kexist(key1, key2) == 2: # the key exists and contains data  
        fe = []
        ie = c_int(0)
        RecLen = c_int(sizeof(func))
        while ie.value < 2:
            ie.value = py_sof_cdb_get(Index, key1, key2, byref(func), byref(RecLen), 1)
            if func.m_id == 121:
                fe.append(func.m_nr[0])
                fe.append(func.m_nr[1])
                area.elements = fe
                print(f'elements {fe}')
                break
    


a = structural_areas[4]
SarsRead(a)

print(f'{a.id=}')
print(f'{a.group=}')
print(f'{a.thickness=}')
print(f'{a.elements=}')

#read cdb and create list of loadcases




#read cdb and create quad finite elements for selected groups/structural areas
#elements contains forces from selected load cases





# Close the CDB, 0 - will close all the files
myDLL.sof_cdb_close(0)

# Print again the status of the CDB, if status = 0 -> CDB Closed successfully
cdbStat.value = myDLL.sof_cdb_status(Index.value)
if cdbStat.value == 0:
    print ("CDB closed successfully, status = 0")