from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.TCollection import *
from OCC.Core.Message import *
from OCC.Core.Resource import *

#the following typedef cannot be wrapped as is
CDM_DocumentHasher = NewType('CDM_DocumentHasher', Any)
CDM_DocumentPointer = NewType('CDM_DocumentPointer', CDM_Document)
#the following typedef cannot be wrapped as is
CDM_MapIteratorOfMapOfDocument = NewType('CDM_MapIteratorOfMapOfDocument', Any)
#the following typedef cannot be wrapped as is
CDM_MapOfDocument = NewType('CDM_MapOfDocument', Any)
CDM_NamesDirectory = NewType('CDM_NamesDirectory', TColStd_DataMapOfStringInteger)

class CDM_ListOfDocument:
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

class CDM_ListOfReferences:
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

class CDM_CanCloseStatus(IntEnum):
    CDM_CCS_OK: int = ...
    CDM_CCS_NotOpen: int = ...
    CDM_CCS_UnstoredReferenced: int = ...
    CDM_CCS_ModifiedReferenced: int = ...
    CDM_CCS_ReferenceRejection: int = ...

CDM_CCS_OK = CDM_CanCloseStatus.CDM_CCS_OK
CDM_CCS_NotOpen = CDM_CanCloseStatus.CDM_CCS_NotOpen
CDM_CCS_UnstoredReferenced = CDM_CanCloseStatus.CDM_CCS_UnstoredReferenced
CDM_CCS_ModifiedReferenced = CDM_CanCloseStatus.CDM_CCS_ModifiedReferenced
CDM_CCS_ReferenceRejection = CDM_CanCloseStatus.CDM_CCS_ReferenceRejection

class CDM_Application(Standard_Transient):
    def BeginOfUpdate(self, aDocument: CDM_Document) -> None: ...
    def EndOfUpdate(self, aDocument: CDM_Document, theStatus: bool, ErrorString: TCollection_ExtendedString) -> None: ...
    def MessageDriver(self) -> Message_Messenger: ...
    def MetaDataLookUpTable(self) -> CDM_MetaDataLookUpTable: ...
    def Name(self) -> TCollection_ExtendedString: ...
    def Resources(self) -> Resource_Manager: ...
    def Version(self) -> TCollection_AsciiString: ...
    def Write(self, aString: Standard_ExtString) -> None: ...

class CDM_Document(Standard_Transient):
    def AddComment(self, aComment: TCollection_ExtendedString) -> None: ...
    def Application(self) -> CDM_Application: ...
    def CanClose(self) -> CDM_CanCloseStatus: ...
    def CanCloseReference(self, aDocument: CDM_Document, aReferenceIdentifier: int) -> bool: ...
    def Close(self) -> None: ...
    def CloseReference(self, aDocument: CDM_Document, aReferenceIdentifier: int) -> None: ...
    def Comment(self) -> Standard_ExtString: ...
    def Comments(self, aComments: TColStd_SequenceOfExtendedString) -> None: ...
    def CopyReference(self, aFromDocument: CDM_Document, aReferenceIdentifier: int) -> int: ...
    @overload
    def CreateReference(self, anOtherDocument: CDM_Document) -> int: ...
    @overload
    def CreateReference(self, aMetaData: CDM_MetaData, aReferenceIdentifier: int, anApplication: CDM_Application, aToDocumentVersion: int, UseStorageConfiguration: bool) -> None: ...
    @overload
    def CreateReference(self, aMetaData: CDM_MetaData, anApplication: CDM_Application, aDocumentVersion: int, UseStorageConfiguration: bool) -> int: ...
    def DeepReferences(self, aDocument: CDM_Document) -> bool: ...
    def Description(self) -> TCollection_ExtendedString: ...
    def Document(self, aReferenceIdentifier: int) -> CDM_Document: ...
    def Extensions(self, Extensions: TColStd_SequenceOfExtendedString) -> None: ...
    def FileExtension(self) -> TCollection_ExtendedString: ...
    def FindDescription(self) -> bool: ...
    def FindFileExtension(self) -> bool: ...
    def Folder(self) -> TCollection_ExtendedString: ...
    def FromReferencesNumber(self) -> int: ...
    def GetAlternativeDocument(self, aFormat: TCollection_ExtendedString, anAlternativeDocument: CDM_Document) -> bool: ...
    def HasRequestedFolder(self) -> bool: ...
    def HasRequestedPreviousVersion(self) -> bool: ...
    def IsInSession(self, aReferenceIdentifier: int) -> bool: ...
    def IsModified(self) -> bool: ...
    @overload
    def IsOpened(self) -> bool: ...
    @overload
    def IsOpened(self, aReferenceIdentifier: int) -> bool: ...
    @overload
    def IsReadOnly(self) -> bool: ...
    @overload
    def IsReadOnly(self, aReferenceIdentifier: int) -> bool: ...
    @overload
    def IsStored(self, aReferenceIdentifier: int) -> bool: ...
    @overload
    def IsStored(self) -> bool: ...
    def IsUpToDate(self, aReferenceIdentifier: int) -> bool: ...
    def LoadResources(self) -> None: ...
    def MetaData(self) -> CDM_MetaData: ...
    def Modifications(self) -> int: ...
    def Modify(self) -> None: ...
    def Name(self, aReferenceIdentifier: int) -> TCollection_ExtendedString: ...
    def Open(self, anApplication: CDM_Application) -> None: ...
    def Reference(self, aReferenceIdentifier: int) -> CDM_Reference: ...
    def ReferenceCounter(self) -> int: ...
    def RemoveAllReferences(self) -> None: ...
    def RemoveReference(self, aReferenceIdentifier: int) -> None: ...
    def RequestedComment(self) -> TCollection_ExtendedString: ...
    def RequestedFolder(self) -> TCollection_ExtendedString: ...
    def RequestedName(self) -> TCollection_ExtendedString: ...
    def RequestedPreviousVersion(self) -> TCollection_ExtendedString: ...
    def SetComment(self, aComment: TCollection_ExtendedString) -> None: ...
    def SetComments(self, aComments: TColStd_SequenceOfExtendedString) -> None: ...
    def SetIsReadOnly(self) -> None: ...
    def SetIsUpToDate(self, aReferenceIdentifier: int) -> None: ...
    def SetMetaData(self, aMetaData: CDM_MetaData) -> None: ...
    def SetModifications(self, Modifications: int) -> None: ...
    def SetReferenceCounter(self, aReferenceCounter: int) -> None: ...
    def SetRequestedComment(self, aComment: TCollection_ExtendedString) -> None: ...
    def SetRequestedFolder(self, aFolder: TCollection_ExtendedString) -> None: ...
    def SetRequestedName(self, aName: TCollection_ExtendedString) -> None: ...
    def SetRequestedPreviousVersion(self, aPreviousVersion: TCollection_ExtendedString) -> None: ...
    def ShallowReferences(self, aDocument: CDM_Document) -> bool: ...
    def StorageFormat(self) -> TCollection_ExtendedString: ...
    def StorageVersion(self) -> int: ...
    def ToReferencesNumber(self) -> int: ...
    def UnModify(self) -> None: ...
    def UnsetIsReadOnly(self) -> None: ...
    def UnsetIsStored(self) -> None: ...
    def UnsetRequestedPreviousVersion(self) -> None: ...
    @overload
    def Update(self, aToDocument: CDM_Document, aReferenceIdentifier: int, aModifContext: None) -> None: ...
    @overload
    def Update(self, ErrorString: TCollection_ExtendedString) -> bool: ...
    @overload
    def Update(self) -> None: ...
    def UpdateFromDocuments(self, aModifContext: None) -> None: ...

class CDM_MetaData(Standard_Transient):
    def Document(self) -> CDM_Document: ...
    def FileName(self) -> TCollection_ExtendedString: ...
    def Folder(self) -> TCollection_ExtendedString: ...
    def HasVersion(self) -> bool: ...
    def IsReadOnly(self) -> bool: ...
    def IsRetrieved(self) -> bool: ...
    @overload
    @staticmethod
    def LookUp(theLookUpTable: CDM_MetaDataLookUpTable, aFolder: TCollection_ExtendedString, aName: TCollection_ExtendedString, aPath: TCollection_ExtendedString, aFileName: TCollection_ExtendedString, ReadOnly: bool) -> CDM_MetaData: ...
    @overload
    @staticmethod
    def LookUp(theLookUpTable: CDM_MetaDataLookUpTable, aFolder: TCollection_ExtendedString, aName: TCollection_ExtendedString, aPath: TCollection_ExtendedString, aVersion: TCollection_ExtendedString, aFileName: TCollection_ExtendedString, ReadOnly: bool) -> CDM_MetaData: ...
    def Name(self) -> TCollection_ExtendedString: ...
    def Path(self) -> TCollection_ExtendedString: ...
    def SetIsReadOnly(self) -> None: ...
    def UnsetDocument(self) -> None: ...
    def UnsetIsReadOnly(self) -> None: ...
    def Version(self) -> TCollection_ExtendedString: ...

class CDM_Reference(Standard_Transient):
    def DocumentVersion(self) -> int: ...
    def FromDocument(self) -> CDM_Document: ...
    def IsReadOnly(self) -> bool: ...
    def ReferenceIdentifier(self) -> int: ...
    def ToDocument(self) -> CDM_Document: ...

class CDM_ReferenceIterator:
    def __init__(self, aDocument: CDM_Document) -> None: ...
    def Document(self) -> CDM_Document: ...
    def DocumentVersion(self) -> int: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def ReferenceIdentifier(self) -> int: ...

# harray1 classes
# harray2 classes
# hsequence classes

CDM_MetaData_LookUp = CDM_MetaData.LookUp
CDM_MetaData_LookUp = CDM_MetaData.LookUp
