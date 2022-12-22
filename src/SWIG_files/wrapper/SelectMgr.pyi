from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Graphic3d import *
from OCC.Core.gp import *
from OCC.Core.Select3D import *
from OCC.Core.SelectBasics import *
from OCC.Core.TColgp import *
from OCC.Core.PrsMgr import *
from OCC.Core.Aspect import *
from OCC.Core.Prs3d import *
from OCC.Core.TopLoc import *
from OCC.Core.V3d import *
from OCC.Core.TopAbs import *
from OCC.Core.BVH import *
from OCC.Core.Bnd import *

SelectBasics_EntityOwner = NewType('SelectBasics_EntityOwner', SelectMgr_EntityOwner)
#the following typedef cannot be wrapped as is
SelectMgr_IndexedDataMapOfOwnerCriterion = NewType('SelectMgr_IndexedDataMapOfOwnerCriterion', Any)
#the following typedef cannot be wrapped as is
SelectMgr_IndexedMapOfHSensitive = NewType('SelectMgr_IndexedMapOfHSensitive', Any)
#the following typedef cannot be wrapped as is
SelectMgr_IndexedMapOfOwner = NewType('SelectMgr_IndexedMapOfOwner', Any)
#the following typedef cannot be wrapped as is
SelectMgr_Mat4 = NewType('SelectMgr_Mat4', Any)
#the following typedef cannot be wrapped as is
SelectMgr_Vec3 = NewType('SelectMgr_Vec3', Any)
#the following typedef cannot be wrapped as is
SelectMgr_Vec4 = NewType('SelectMgr_Vec4', Any)

class SelectMgr_ListOfFilter:
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

class SelectMgr_SequenceOfOwner:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class SelectMgr_SequenceOfSelection:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class SelectMgr_FilterType(IntEnum):
    SelectMgr_FilterType_AND: int = ...
    SelectMgr_FilterType_OR: int = ...

SelectMgr_FilterType_AND = SelectMgr_FilterType.SelectMgr_FilterType_AND
SelectMgr_FilterType_OR = SelectMgr_FilterType.SelectMgr_FilterType_OR

class SelectMgr_TypeOfDepthTolerance(IntEnum):
    SelectMgr_TypeOfDepthTolerance_Uniform: int = ...
    SelectMgr_TypeOfDepthTolerance_UniformPixels: int = ...
    SelectMgr_TypeOfDepthTolerance_SensitivityFactor: int = ...

SelectMgr_TypeOfDepthTolerance_Uniform = SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_Uniform
SelectMgr_TypeOfDepthTolerance_UniformPixels = SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_UniformPixels
SelectMgr_TypeOfDepthTolerance_SensitivityFactor = SelectMgr_TypeOfDepthTolerance.SelectMgr_TypeOfDepthTolerance_SensitivityFactor

class SelectMgr_SelectionType(IntEnum):
    SelectMgr_SelectionType_Unknown: int = ...
    SelectMgr_SelectionType_Point: int = ...
    SelectMgr_SelectionType_Box: int = ...
    SelectMgr_SelectionType_Polyline: int = ...

SelectMgr_SelectionType_Unknown = SelectMgr_SelectionType.SelectMgr_SelectionType_Unknown
SelectMgr_SelectionType_Point = SelectMgr_SelectionType.SelectMgr_SelectionType_Point
SelectMgr_SelectionType_Box = SelectMgr_SelectionType.SelectMgr_SelectionType_Box
SelectMgr_SelectionType_Polyline = SelectMgr_SelectionType.SelectMgr_SelectionType_Polyline

class SelectMgr_TypeOfUpdate(IntEnum):
    SelectMgr_TOU_Full: int = ...
    SelectMgr_TOU_Partial: int = ...
    SelectMgr_TOU_None: int = ...

SelectMgr_TOU_Full = SelectMgr_TypeOfUpdate.SelectMgr_TOU_Full
SelectMgr_TOU_Partial = SelectMgr_TypeOfUpdate.SelectMgr_TOU_Partial
SelectMgr_TOU_None = SelectMgr_TypeOfUpdate.SelectMgr_TOU_None

class SelectMgr_TypeOfBVHUpdate(IntEnum):
    SelectMgr_TBU_Add: int = ...
    SelectMgr_TBU_Remove: int = ...
    SelectMgr_TBU_Renew: int = ...
    SelectMgr_TBU_Invalidate: int = ...
    SelectMgr_TBU_None: int = ...

SelectMgr_TBU_Add = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Add
SelectMgr_TBU_Remove = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Remove
SelectMgr_TBU_Renew = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Renew
SelectMgr_TBU_Invalidate = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_Invalidate
SelectMgr_TBU_None = SelectMgr_TypeOfBVHUpdate.SelectMgr_TBU_None

class SelectMgr_StateOfSelection(IntEnum):
    SelectMgr_SOS_Any: int = ...
    SelectMgr_SOS_Unknown: int = ...
    SelectMgr_SOS_Deactivated: int = ...
    SelectMgr_SOS_Activated: int = ...

SelectMgr_SOS_Any = SelectMgr_StateOfSelection.SelectMgr_SOS_Any
SelectMgr_SOS_Unknown = SelectMgr_StateOfSelection.SelectMgr_SOS_Unknown
SelectMgr_SOS_Deactivated = SelectMgr_StateOfSelection.SelectMgr_SOS_Deactivated
SelectMgr_SOS_Activated = SelectMgr_StateOfSelection.SelectMgr_SOS_Activated

class SelectMgr_PickingStrategy(IntEnum):
    SelectMgr_PickingStrategy_FirstAcceptable: int = ...
    SelectMgr_PickingStrategy_OnlyTopmost: int = ...

SelectMgr_PickingStrategy_FirstAcceptable = SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_FirstAcceptable
SelectMgr_PickingStrategy_OnlyTopmost = SelectMgr_PickingStrategy.SelectMgr_PickingStrategy_OnlyTopmost

class selectmgr:
    @staticmethod
    def ComputeSensitivePrs(theStructure: Graphic3d_Structure, theSel: SelectMgr_Selection, theLoc: gp_Trsf, theTrsfPers: Graphic3d_TransformPers) -> None: ...

class SelectMgr_BVHThreadPool(Standard_Transient):
    def __init__(self, theNbThreads: int) -> None: ...
    def AddEntity(self, theEntity: Select3D_SensitiveEntity) -> None: ...
    def StopThreads(self) -> None: ...
    def Threads(self) -> False: ...
    def WaitThreads(self) -> None: ...

class SelectMgr_BaseIntersector(Standard_Transient):
    def Build(self) -> None: ...
    def Camera(self) -> Graphic3d_Camera: ...
    def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
    def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
    def GetFarPnt(self) -> gp_Pnt: ...
    def GetMousePosition(self) -> gp_Pnt2d: ...
    def GetNearPnt(self) -> gp_Pnt: ...
    def GetSelectionType(self) -> SelectMgr_SelectionType: ...
    def GetViewRayDirection(self) -> gp_Dir: ...
    def IsScalable(self) -> bool: ...
    @overload
    def OverlapsBox(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsBox(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: gp_Trsf, theIsFilled: bool, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: bool, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt) -> bool: ...
    def OverlapsPolygon(self, theArrayOfPnts: TColgp_Array1OfPnt, theSensType: Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    def OverlapsSegment(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsSphere(self, theCenter: gp_Pnt, theRadius: float, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsSphere(self, theCenter: gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePnt3: gp_Pnt, theSensType: Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    def RayCircleIntersection(self, theRadius: float, theLoc: gp_Pnt, theRayDir: gp_Dir, theIsFilled: bool) -> Tuple[bool, float]: ...
    def RayCylinderIntersection(self, theBottomRadius: float, theTopRadius: float, theHeight: float, theLoc: gp_Pnt, theRayDir: gp_Dir, theIsHollow: bool) -> Tuple[bool, float, float]: ...
    def RaySphereIntersection(self, theCenter: gp_Pnt, theRadius: float, theLoc: gp_Pnt, theRayDir: gp_Dir) -> Tuple[bool, float, float]: ...
    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: ...
    def SetCamera(self, theCamera: Graphic3d_Camera) -> None: ...
    def SetPixelTolerance(self, theTol: int) -> None: ...
    def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None: ...
    def SetWindowSize(self, theWidth: int, theHeight: int) -> None: ...
    def WindowSize(self) -> Tuple[int, int]: ...

class SelectMgr_EntityOwner(Standard_Transient):
    @overload
    def __init__(self, aPriority: Optional[int] = 0) -> None: ...
    @overload
    def __init__(self, aSO: SelectMgr_SelectableObject, aPriority: Optional[int] = 0) -> None: ...
    @overload
    def __init__(self, theOwner: SelectMgr_EntityOwner, aPriority: Optional[int] = 0) -> None: ...
    def Clear(self, thePrsMgr: PrsMgr_PresentationManager, theMode: Optional[int] = 0) -> None: ...
    def ComesFromDecomposition(self) -> bool: ...
    def HandleMouseClick(self, thePoint: Graphic3d_Vec2i, theButton: Aspect_VKeyMouse, theModifiers: Aspect_VKeyFlags, theIsDoubleClick: bool) -> bool: ...
    def HasLocation(self) -> bool: ...
    def HasSelectable(self) -> bool: ...
    def HilightWithColor(self, thePrsMgr: PrsMgr_PresentationManager, theStyle: Prs3d_Drawer, theMode: Optional[int] = 0) -> None: ...
    def IsAutoHilight(self) -> bool: ...
    def IsForcedHilight(self) -> bool: ...
    def IsHilighted(self, thePrsMgr: PrsMgr_PresentationManager, theMode: Optional[int] = 0) -> bool: ...
    def IsSameSelectable(self, theOther: SelectMgr_SelectableObject) -> bool: ...
    def IsSelected(self) -> bool: ...
    def Location(self) -> TopLoc_Location: ...
    def Priority(self) -> int: ...
    def Selectable(self) -> SelectMgr_SelectableObject: ...
    @overload
    def Set(self, theSelObj: SelectMgr_SelectableObject) -> None: ...
    @overload
    def Set(self, thePriority: int) -> None: ...
    def SetComesFromDecomposition(self, theIsFromDecomposition: bool) -> None: ...
    def SetLocation(self, theLocation: TopLoc_Location) -> None: ...
    def SetPriority(self, thePriority: int) -> None: ...
    def SetSelectable(self, theSelObj: SelectMgr_SelectableObject) -> None: ...
    def SetSelected(self, theIsSelected: bool) -> None: ...
    def SetZLayer(self, theLayerId: int) -> None: ...
    @overload
    def State(self) -> int: ...
    @overload
    def State(self, theStatus: int) -> None: ...
    def Unhilight(self, thePrsMgr: PrsMgr_PresentationManager, theMode: Optional[int] = 0) -> None: ...
    def UpdateHighlightTrsf(self, theViewer: V3d_Viewer, theManager: PrsMgr_PresentationManager, theDispMode: int) -> None: ...

class SelectMgr_Filter(Standard_Transient):
    def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
    def IsOk(self, anObj: SelectMgr_EntityOwner) -> bool: ...

class SelectMgr_SelectableObject(PrsMgr_PresentableObject):
    def AcceptShapeDecomposition(self) -> bool: ...
    def AddSelection(self, aSelection: SelectMgr_Selection, aMode: int) -> None: ...
    def ClearDynamicHighlight(self, theMgr: PrsMgr_PresentationManager) -> None: ...
    def ClearSelected(self) -> None: ...
    def ClearSelections(self, update: Optional[bool] = False) -> None: ...
    def ComputeSelection(self, theSelection: SelectMgr_Selection, theMode: int) -> None: ...
    def ErasePresentations(self, theToRemove: bool) -> None: ...
    def GetAssemblyOwner(self) -> SelectMgr_EntityOwner: ...
    def GetHilightPresentation(self, thePrsMgr: PrsMgr_PresentationManager) -> Prs3d_Presentation: ...
    def GetSelectPresentation(self, thePrsMgr: PrsMgr_PresentationManager) -> Prs3d_Presentation: ...
    def GlobalSelOwner(self) -> SelectMgr_EntityOwner: ...
    def GlobalSelectionMode(self) -> int: ...
    def HasSelection(self, theMode: int) -> bool: ...
    def HilightOwnerWithColor(self, thePM: PrsMgr_PresentationManager, theStyle: Prs3d_Drawer, theOwner: SelectMgr_EntityOwner) -> None: ...
    def HilightSelected(self, thePrsMgr: PrsMgr_PresentationManager, theSeq: SelectMgr_SequenceOfOwner) -> None: ...
    def IsAutoHilight(self) -> bool: ...
    @overload
    def RecomputePrimitives(self) -> None: ...
    @overload
    def RecomputePrimitives(self, theMode: int) -> None: ...
    def ResetTransformation(self) -> None: ...
    def Selection(self, theMode: int) -> SelectMgr_Selection: ...
    def Selections(self) -> SelectMgr_SequenceOfSelection: ...
    def SetAssemblyOwner(self, theOwner: SelectMgr_EntityOwner, theMode: Optional[int] = -1) -> None: ...
    def SetAutoHilight(self, theAutoHilight: bool) -> None: ...
    def SetZLayer(self, theLayerId: int) -> None: ...
    def UpdateSelection(self, theMode: Optional[int] = -1) -> None: ...
    def UpdateTransformation(self) -> None: ...
    def UpdateTransformations(self, aSelection: SelectMgr_Selection) -> None: ...

class SelectMgr_SelectableObjectSet:
    def __init__(self) -> None: ...
    def Append(self, theObject: SelectMgr_SelectableObject) -> bool: ...
    def ChangeSubset(self, theObject: SelectMgr_SelectableObject) -> None: ...
    def Contains(self, theObject: SelectMgr_SelectableObject) -> bool: ...
    @overload
    def IsEmpty(self) -> bool: ...
    def MarkDirty(self) -> None: ...
    def Remove(self, theObject: SelectMgr_SelectableObject) -> bool: ...
    def UpdateBVH(self, theCam: Graphic3d_Camera, theWinSize: Graphic3d_Vec2i) -> None: ...

class SelectMgr_SelectingVolumeManager(SelectBasics_SelectingVolumeManager):
    def __init__(self) -> None: ...
    def AllowOverlapDetection(self, theIsToAllow: bool) -> None: ...
    @overload
    def BuildSelectingVolume(self) -> None: ...
    @overload
    def BuildSelectingVolume(self, thePoint: gp_Pnt2d) -> None: ...
    @overload
    def BuildSelectingVolume(self, theMinPt: gp_Pnt2d, theMaxPt: gp_Pnt2d) -> None: ...
    @overload
    def BuildSelectingVolume(self, thePoints: TColgp_Array1OfPnt2d) -> None: ...
    def Camera(self) -> Graphic3d_Camera: ...
    def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
    def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
    def GetActiveSelectionType(self) -> int: ...
    def GetFarPickedPnt(self) -> gp_Pnt: ...
    def GetMousePosition(self) -> gp_Pnt2d: ...
    def GetNearPickedPnt(self) -> gp_Pnt: ...
    def GetVertices(self) -> gp_Pnt: ...
    def GetViewRayDirection(self) -> gp_Dir: ...
    def InitAxisSelectingVolume(self, theAxis: gp_Ax1) -> None: ...
    def InitBoxSelectingVolume(self, theMinPt: gp_Pnt2d, theMaxPt: gp_Pnt2d) -> None: ...
    def InitPointSelectingVolume(self, thePoint: gp_Pnt2d) -> None: ...
    def InitPolylineSelectingVolume(self, thePoints: TColgp_Array1OfPnt2d) -> None: ...
    def InitSelectingVolume(self, theVolume: SelectMgr_BaseIntersector) -> None: ...
    def IsOverlapAllowed(self) -> bool: ...
    def IsScalableActiveVolume(self) -> bool: ...
    def ObjectClipping(self) -> Graphic3d_SequenceOfHClipPlane: ...
    @overload
    def OverlapsBox(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsBox(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: gp_Trsf, theIsFilled: bool, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self, theBottomRad: float, theTrsf: gp_Trsf, theIsFilled: bool, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: bool, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: bool, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt) -> bool: ...
    def OverlapsPolygon(self, theArrayOfPts: TColgp_Array1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
    def OverlapsSegment(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsSphere(self, theCenter: gp_Pnt, theRadius: float, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsSphere(self, theCenter: gp_Pnt, theRadius: float, theInside: Optional[bool] = None) -> bool: ...
    def OverlapsTriangle(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePnt3: gp_Pnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder) -> SelectMgr_SelectingVolumeManager: ...
    def SetCamera(self, theCamera: Graphic3d_Camera) -> None: ...
    def SetPixelTolerance(self, theTolerance: int) -> None: ...
    def SetViewClipRanges(self, theRange: SelectMgr_ViewClipRange) -> None: ...
    @overload
    def SetViewClipping(self, theViewPlanes: Graphic3d_SequenceOfHClipPlane, theObjPlanes: Graphic3d_SequenceOfHClipPlane, theWorldSelMgr: SelectMgr_SelectingVolumeManager) -> None: ...
    @overload
    def SetViewClipping(self, theOther: SelectMgr_SelectingVolumeManager) -> None: ...
    def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None: ...
    def SetWindowSize(self, theWidth: int, theHeight: int) -> None: ...
    def ViewClipRanges(self) -> SelectMgr_ViewClipRange: ...
    def ViewClipping(self) -> Graphic3d_SequenceOfHClipPlane: ...
    def WindowSize(self) -> Tuple[int, int]: ...

class SelectMgr_Selection(Standard_Transient):
    def __init__(self, theModeIdx: Optional[int] = 0) -> None: ...
    def Add(self, theSensitive: Select3D_SensitiveEntity) -> None: ...
    def BVHUpdateStatus(self) -> SelectMgr_TypeOfBVHUpdate: ...
    def ChangeEntities(self) -> False: ...
    def Clear(self) -> None: ...
    def Destroy(self) -> None: ...
    def Entities(self) -> False: ...
    def GetSelectionState(self) -> SelectMgr_StateOfSelection: ...
    def IsEmpty(self) -> bool: ...
    def Mode(self) -> int: ...
    def Sensitivity(self) -> int: ...
    def SetSelectionState(self, theState: SelectMgr_StateOfSelection) -> None: ...
    def SetSensitivity(self, theNewSens: int) -> None: ...
    def UpdateBVHStatus(self, theStatus: SelectMgr_TypeOfBVHUpdate) -> None: ...
    @overload
    def UpdateStatus(self) -> SelectMgr_TypeOfUpdate: ...
    @overload
    def UpdateStatus(self, theStatus: SelectMgr_TypeOfUpdate) -> None: ...

class SelectMgr_SelectionImageFiller(Standard_Transient):
    def Fill(self, theCol: int, theRow: int, thePicked: int) -> None: ...
    def Flush(self) -> None: ...

class SelectMgr_SelectionManager(Standard_Transient):
    def __init__(self, theSelector: SelectMgr_ViewerSelector) -> None: ...
    def Activate(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int] = 0) -> None: ...
    def ClearSelectionStructures(self, theObj: SelectMgr_SelectableObject, theMode: Optional[int] = -1) -> None: ...
    def Contains(self, theObject: SelectMgr_SelectableObject) -> bool: ...
    def Deactivate(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int] = -1) -> None: ...
    def IsActivated(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int] = -1) -> bool: ...
    def Load(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int] = -1) -> None: ...
    def RecomputeSelection(self, theObject: SelectMgr_SelectableObject, theIsForce: Optional[bool] = False, theMode: Optional[int] = -1) -> None: ...
    def Remove(self, theObject: SelectMgr_SelectableObject) -> None: ...
    def RestoreSelectionStructures(self, theObj: SelectMgr_SelectableObject, theMode: Optional[int] = -1) -> None: ...
    def Selector(self) -> SelectMgr_ViewerSelector: ...
    def SetSelectionSensitivity(self, theObject: SelectMgr_SelectableObject, theMode: int, theNewSens: int) -> None: ...
    @overload
    def SetUpdateMode(self, theObject: SelectMgr_SelectableObject, theType: SelectMgr_TypeOfUpdate) -> None: ...
    @overload
    def SetUpdateMode(self, theObject: SelectMgr_SelectableObject, theMode: int, theType: SelectMgr_TypeOfUpdate) -> None: ...
    def Update(self, theObject: SelectMgr_SelectableObject, theIsForce: Optional[bool] = True) -> None: ...
    def UpdateSelection(self, theObj: SelectMgr_SelectableObject) -> None: ...

class SelectMgr_SensitiveEntity(Standard_Transient):
    def __init__(self, theEntity: Select3D_SensitiveEntity) -> None: ...
    def BaseSensitive(self) -> Select3D_SensitiveEntity: ...
    def Clear(self) -> None: ...
    def IsActiveForSelection(self) -> bool: ...
    def ResetSelectionActiveStatus(self) -> None: ...
    def SetActiveForSelection(self) -> None: ...

class SelectMgr_SortCriterion:
    def __init__(self) -> None: ...
    def IsCloserDepth(self, theOther: SelectMgr_SortCriterion) -> bool: ...
    def IsHigherPriority(self, theOther: SelectMgr_SortCriterion) -> bool: ...

class SelectMgr_ViewClipRange:
    def __init__(self) -> None: ...
    def AddClipSubRange(self, theRange: Bnd_Range) -> None: ...
    def AddClippingPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane, thePickRay: gp_Ax1) -> None: ...
    def ChangeUnclipRange(self) -> Bnd_Range: ...
    def GetNearestDepth(self, theRange: Bnd_Range) -> Tuple[bool, float]: ...
    def IsClipped(self, theDepth: float) -> bool: ...
    def SetVoid(self) -> None: ...

class SelectMgr_AxisIntersector(SelectMgr_BaseIntersector):
    def __init__(self) -> None: ...
    def Build(self) -> None: ...
    def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
    def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
    def GetFarPnt(self) -> gp_Pnt: ...
    def GetNearPnt(self) -> gp_Pnt: ...
    def GetViewRayDirection(self) -> gp_Dir: ...
    def Init(self, theAxis: gp_Ax1) -> None: ...
    def IsScalable(self) -> bool: ...
    @overload
    def OverlapsBox(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsBox(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, theInside: bool) -> bool: ...
    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: gp_Trsf, theIsFilled: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCircle(self, theRadius: float, theTrsf: gp_Trsf, theIsFilled: bool, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: bool, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsCylinder(self, theBottomRad: float, theTopRad: float, theHeight: float, theTrsf: gp_Trsf, theIsHollow: bool, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt) -> bool: ...
    def OverlapsPolygon(self, theArrayOfPnts: TColgp_Array1OfPnt, theSensType: Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    def OverlapsSegment(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    @overload
    def OverlapsSphere(self, theCenter: gp_Pnt, theRadius: float, theInside: Optional[bool] = None) -> bool: ...
    @overload
    def OverlapsSphere(self, theCenter: gp_Pnt, theRadius: float, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    def OverlapsTriangle(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePnt3: gp_Pnt, theSensType: Select3D_TypeOfSensitivity, theClipRange: SelectMgr_ViewClipRange, thePickResult: SelectBasics_PickResult) -> bool: ...
    def ScaleAndTransform(self, theScaleFactor: int, theTrsf: gp_GTrsf, theBuilder: SelectMgr_FrustumBuilder) -> SelectMgr_BaseIntersector: ...
    def SetCamera(self, theCamera: Graphic3d_Camera) -> None: ...

class SelectMgr_CompositionFilter(SelectMgr_Filter):
    def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
    def Add(self, afilter: SelectMgr_Filter) -> None: ...
    def Clear(self) -> None: ...
    def IsEmpty(self) -> bool: ...
    def IsIn(self, aFilter: SelectMgr_Filter) -> bool: ...
    def Remove(self, aFilter: SelectMgr_Filter) -> None: ...
    def StoredFilters(self) -> SelectMgr_ListOfFilter: ...

class SelectMgr_AndFilter(SelectMgr_CompositionFilter):
    def __init__(self) -> None: ...
    def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...

class SelectMgr_AndOrFilter(SelectMgr_CompositionFilter):
    def __init__(self, theFilterType: SelectMgr_FilterType) -> None: ...
    def FilterType(self) -> SelectMgr_FilterType: ...
    def IsOk(self, theObj: SelectMgr_EntityOwner) -> bool: ...
    def SetDisabledObjects(self, theObjects: Graphic3d_NMapOfTransient) -> None: ...
    def SetFilterType(self, theFilterType: SelectMgr_FilterType) -> None: ...

class SelectMgr_OrFilter(SelectMgr_CompositionFilter):
    def __init__(self) -> None: ...
    def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...

#classnotwrapped
class SelectMgr_Frustum: ...

#classnotwrapped
class SelectMgr_FrustumBuilder: ...

#classnotwrapped
class SelectMgr_BaseFrustum: ...

#classnotwrapped
class SelectMgr_TriangularFrustum: ...

#classnotwrapped
class SelectMgr_RectangularFrustum: ...

#classnotwrapped
class SelectMgr_TriangularFrustumSet: ...

#classnotwrapped
class SelectMgr_ToleranceMap: ...

#classnotwrapped
class SelectMgr_ViewerSelector: ...

#classnotwrapped
class SelectMgr_SensitiveEntitySet: ...

# harray1 classes
# harray2 classes
# hsequence classes

selectmgr_ComputeSensitivePrs = selectmgr.ComputeSensitivePrs
