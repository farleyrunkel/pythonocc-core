from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *

# the following typedef cannot be wrapped as is
FEmTool_AssemblyTable = NewType("FEmTool_AssemblyTable", Any)

class FEmTool_ListOfVectors:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class FEmTool_SeqOfLinConstr:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> FEmTool_ListOfVectors: ...
    def Last(self) -> FEmTool_ListOfVectors: ...
    def Length(self) -> int: ...
    def Append(self, theItem: FEmTool_ListOfVectors) -> FEmTool_ListOfVectors: ...
    def Prepend(self, theItem: FEmTool_ListOfVectors) -> FEmTool_ListOfVectors: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> FEmTool_ListOfVectors: ...
    def SetValue(self, theIndex: int, theValue: FEmTool_ListOfVectors) -> None: ...

#classnotwrapped
class FEmTool_ElementsOfRefMatrix: ...

#classnotwrapped
class FEmTool_Curve: ...

#classnotwrapped
class FEmTool_ProfileMatrix: ...

#classnotwrapped
class FEmTool_ElementaryCriterion: ...

#classnotwrapped
class FEmTool_LinearTension: ...

#classnotwrapped
class FEmTool_LinearJerk: ...

#classnotwrapped
class FEmTool_LinearFlexion: ...

#classnotwrapped
class FEmTool_SparseMatrix: ...

#classnotwrapped
class FEmTool_Assembly: ...

# harray1 classes
# harray2 classes

class FEmTool_HAssemblyTable(FEmTool_AssemblyTable, Standard_Transient):
    @overload
    def __init__(self, theRowLow: int, theRowUpp: int, theColLow: int, theColUpp: int) -> None: ...
    @overload
    def __init__(self, theOther: FEmTool_AssemblyTable) -> None: ...
    def Array2(self) -> FEmTool_AssemblyTable: ...

# hsequence classes

