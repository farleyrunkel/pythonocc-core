from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.Prs3d import *
from OCC.Core.TCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.Graphic3d import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TColgp import *
from OCC.Core.HLRAlgo import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TColStd import *
from OCC.Core.Poly import *
from OCC.Core.TopLoc import *
from OCC.Core.BRep import *
from OCC.Core.GeomAbs import *
from OCC.Core.Bnd import *
from OCC.Core.TopTools import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor2d import *

StdPrs_BndBox = NewType('StdPrs_BndBox', Prs3d_BndBox)
#the following typedef cannot be wrapped as is
StdPrs_Point = NewType('StdPrs_Point', Any)
#the following typedef cannot be wrapped as is
StdPrs_Vertex = NewType('StdPrs_Vertex', Any)

class StdPrs_Volume(IntEnum):
    StdPrs_Volume_Autodetection: int = ...
    StdPrs_Volume_Closed: int = ...
    StdPrs_Volume_Opened: int = ...

StdPrs_Volume_Autodetection = StdPrs_Volume.StdPrs_Volume_Autodetection
StdPrs_Volume_Closed = StdPrs_Volume.StdPrs_Volume_Closed
StdPrs_Volume_Opened = StdPrs_Volume.StdPrs_Volume_Opened

class StdPrs_BRepFont(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theFontPath: NCollection_String, theSize: float, theFaceId: Optional[int] = 0) -> None: ...
    @overload
    def AdvanceX(self, theUCharNext: Standard_Utf32Char) -> float: ...
    @overload
    def AdvanceX(self, theUChar: Standard_Utf32Char, theUCharNext: Standard_Utf32Char) -> float: ...
    @overload
    def AdvanceY(self, theUCharNext: Standard_Utf32Char) -> float: ...
    @overload
    def AdvanceY(self, theUChar: Standard_Utf32Char, theUCharNext: Standard_Utf32Char) -> float: ...
    def Ascender(self) -> float: ...
    def Descender(self) -> float: ...
    def FTFont(self) -> False: ...
    @overload
    def Init(self, theFontPath: NCollection_String, theSize: float, theFaceId: int) -> bool: ...
    def LineSpacing(self) -> float: ...
    def Mutex(self) -> Standard_Mutex: ...
    def PointSize(self) -> float: ...
    def Release(self) -> None: ...
    def RenderGlyph(self, theChar: Standard_Utf32Char) -> TopoDS_Shape: ...
    def Scale(self) -> float: ...
    def SetCompositeCurveMode(self, theToConcatenate: bool) -> None: ...
    def SetWidthScaling(self, theScaleFactor: float) -> None: ...

class StdPrs_BRepTextBuilder:
    @overload
    def Perform(self, theFont: StdPrs_BRepFont, theString: NCollection_String, thePenLoc: Optional[gp_Ax3] = gp_Ax3(), theHAlign: Optional[Graphic3d_HorizontalTextAlignment] = Graphic3d_HTA_LEFT, theVAlign: Optional[Graphic3d_VerticalTextAlignment] = Graphic3d_VTA_BOTTOM) -> TopoDS_Shape: ...

class StdPrs_Curve(Prs3d_Root):
    @overload
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer, drawCurve: Optional[bool] = True) -> None: ...
    @overload
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, U1: float, U2: float, aDrawer: Prs3d_Drawer, drawCurve: Optional[bool] = True) -> None: ...
    @overload
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer, Points: TColgp_SequenceOfPnt, drawCurve: Optional[bool] = True) -> None: ...
    @overload
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, U1: float, U2: float, Points: TColgp_SequenceOfPnt, aNbPoints: Optional[int] = 30, drawCurve: Optional[bool] = True) -> None: ...
    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> bool: ...
    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDeflection: float, aLimit: float, aNbPoints: int) -> bool: ...
    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, U1: float, U2: float, aDrawer: Prs3d_Drawer) -> bool: ...
    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, U1: float, U2: float, aDeflection: float, aNbPoints: int) -> bool: ...

class StdPrs_HLRShapeI(Standard_Transient):
    def ComputeHLR(self, thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theProjector: Graphic3d_Camera) -> None: ...

class StdPrs_HLRToolShape:
    def __init__(self, TheShape: TopoDS_Shape, TheProjector: HLRAlgo_Projector) -> None: ...
    def Hidden(self, TheEdge: BRepAdaptor_Curve) -> Tuple[float, float]: ...
    def InitHidden(self, EdgeNumber: int) -> None: ...
    def InitVisible(self, EdgeNumber: int) -> None: ...
    def MoreHidden(self) -> bool: ...
    def MoreVisible(self) -> bool: ...
    def NbEdges(self) -> int: ...
    def NextHidden(self) -> None: ...
    def NextVisible(self) -> None: ...
    def Visible(self, TheEdge: BRepAdaptor_Curve) -> Tuple[float, float]: ...

class StdPrs_Isolines(Prs3d_Root):
    @overload
    @staticmethod
    def Add(thePresentation: Prs3d_Presentation, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float) -> None: ...
    @overload
    @staticmethod
    def Add(theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float, theUPolylines: Prs3d_NListOfSequenceOfPnt, theVPolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
    @overload
    @staticmethod
    def AddOnSurface(thePresentation: Prs3d_Presentation, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float) -> None: ...
    @overload
    @staticmethod
    def AddOnSurface(theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float, theUPolylines: Prs3d_NListOfSequenceOfPnt, theVPolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
    @overload
    @staticmethod
    def AddOnSurface(thePresentation: Prs3d_Presentation, theSurface: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer, theDeflection: float, theUIsoParams: TColStd_SequenceOfReal, theVIsoParams: TColStd_SequenceOfReal) -> None: ...
    @overload
    @staticmethod
    def AddOnTriangulation(thePresentation: Prs3d_Presentation, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer) -> None: ...
    @overload
    @staticmethod
    def AddOnTriangulation(theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theUPolylines: Prs3d_NListOfSequenceOfPnt, theVPolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
    @overload
    @staticmethod
    def AddOnTriangulation(thePresentation: Prs3d_Presentation, theTriangulation: Poly_Triangulation, theSurface: Geom_Surface, theLocation: TopLoc_Location, theDrawer: Prs3d_Drawer, theUIsoParams: TColStd_SequenceOfReal, theVIsoParams: TColStd_SequenceOfReal) -> None: ...
    @staticmethod
    def UVIsoParameters(theFace: TopoDS_Face, theNbIsoU: int, theNbIsoV: int, theUVLimit: float, theUIsoParams: TColStd_SequenceOfReal, theVIsoParams: TColStd_SequenceOfReal) -> Tuple[float, float, float, float]: ...

class StdPrs_Plane(Prs3d_Root):
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aPlane: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aPlane: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_PoleCurve(Prs3d_Root):
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> bool: ...
    @staticmethod
    def Pick(X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> int: ...

class StdPrs_ShadedShape(Prs3d_Root):
    @overload
    @staticmethod
    def Add(thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theVolume: Optional[StdPrs_Volume] = StdPrs_Volume_Autodetection) -> None: ...
    @overload
    @staticmethod
    def Add(thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theHasTexels: bool, theUVOrigin: gp_Pnt2d, theUVRepeat: gp_Pnt2d, theUVScale: gp_Pnt2d, theVolume: Optional[StdPrs_Volume] = StdPrs_Volume_Autodetection) -> None: ...
    @staticmethod
    def AddWireframeForFacesWithoutTriangles(thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def AddWireframeForFreeElements(thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def ExploreSolids(theShape: TopoDS_Shape, theBuilder: BRep_Builder, theClosed: TopoDS_Compound, theOpened: TopoDS_Compound, theIgnore1DSubShape: bool) -> None: ...
    @staticmethod
    def FillFaceBoundaries(theShape: TopoDS_Shape, theUpperContinuity: Optional[GeomAbs_Shape] = GeomAbs_CN) -> Graphic3d_ArrayOfSegments: ...
    @overload
    @staticmethod
    def FillTriangles(theShape: TopoDS_Shape) -> Graphic3d_ArrayOfTriangles: ...
    @overload
    @staticmethod
    def FillTriangles(theShape: TopoDS_Shape, theHasTexels: bool, theUVOrigin: gp_Pnt2d, theUVRepeat: gp_Pnt2d, theUVScale: gp_Pnt2d) -> Graphic3d_ArrayOfTriangles: ...

class StdPrs_ShadedSurface(Prs3d_Root):
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_ShapeTool:
    def __init__(self, theShape: TopoDS_Shape, theAllVertices: Optional[bool] = False) -> None: ...
    def CurrentTriangulation(self, l: TopLoc_Location) -> Poly_Triangulation: ...
    def CurveBound(self) -> Bnd_Box: ...
    def FaceBound(self) -> Bnd_Box: ...
    def FacesOfEdge(self) -> TopTools_HSequenceOfShape: ...
    def GetCurve(self) -> TopoDS_Edge: ...
    def GetFace(self) -> TopoDS_Face: ...
    def GetVertex(self) -> TopoDS_Vertex: ...
    def HasCurve(self) -> bool: ...
    def HasSurface(self) -> bool: ...
    def InitCurve(self) -> None: ...
    def InitFace(self) -> None: ...
    def InitVertex(self) -> None: ...
    @overload
    def IsPlanarFace(self) -> bool: ...
    @overload
    @staticmethod
    def IsPlanarFace(theFace: TopoDS_Face) -> bool: ...
    def MoreCurve(self) -> bool: ...
    def MoreFace(self) -> bool: ...
    def MoreVertex(self) -> bool: ...
    def Neighbours(self) -> int: ...
    def NextCurve(self) -> None: ...
    def NextFace(self) -> None: ...
    def NextVertex(self) -> None: ...
    def Polygon3D(self, l: TopLoc_Location) -> Poly_Polygon3D: ...
    def PolygonOnTriangulation(self, Indices: Poly_PolygonOnTriangulation, T: Poly_Triangulation, l: TopLoc_Location) -> None: ...

class StdPrs_ToolPoint:
    @staticmethod
    def Coord(aPoint: Geom_Point) -> Tuple[float, float, float]: ...

class StdPrs_ToolRFace:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aSurface: BRepAdaptor_Surface) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Init(self) -> None: ...
    def IsInvalidGeometry(self) -> bool: ...
    def IsOriented(self) -> bool: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Orientation(self) -> TopAbs_Orientation: ...
    def Value(self) -> Adaptor2d_Curve2d: ...

class StdPrs_ToolTriangulatedShape:
    @staticmethod
    def ClearOnOwnDeflectionChange(theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theToResetCoeff: bool) -> None: ...
    @overload
    @staticmethod
    def ComputeNormals(theFace: TopoDS_Face, theTris: Poly_Triangulation) -> None: ...
    @overload
    @staticmethod
    def ComputeNormals(theFace: TopoDS_Face, theTris: Poly_Triangulation, thePolyConnect: Poly_Connect) -> None: ...
    @staticmethod
    def GetDeflection(theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> float: ...
    @staticmethod
    def IsClosed(theShape: TopoDS_Shape) -> bool: ...
    @staticmethod
    def IsTessellated(theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> bool: ...
    @staticmethod
    def IsTriangulated(theShape: TopoDS_Shape) -> bool: ...
    @staticmethod
    def Normal(theFace: TopoDS_Face, thePolyConnect: Poly_Connect, theNormals: TColgp_Array1OfDir) -> None: ...
    @staticmethod
    def Tessellate(theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_ToolVertex:
    @staticmethod
    def Coord(aPoint: TopoDS_Vertex) -> Tuple[float, float, float]: ...

class StdPrs_WFDeflectionRestrictedFace(Prs3d_Root):
    @overload
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer) -> None: ...
    @overload
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_Surface, DrawUIso: bool, DrawVIso: bool, Deflection: float, NBUiso: int, NBViso: int, aDrawer: Prs3d_Drawer, Curves: Prs3d_NListOfSequenceOfPnt) -> None: ...
    @staticmethod
    def AddUIso(aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def AddVIso(aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer) -> None: ...
    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer) -> bool: ...
    @overload
    @staticmethod
    def Match(X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer, DrawUIso: bool, DrawVIso: bool, aDeflection: float, NBUiso: int, NBViso: int) -> bool: ...
    @staticmethod
    def MatchUIso(X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer) -> bool: ...
    @staticmethod
    def MatchVIso(X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_Surface, aDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_WFDeflectionSurface(Prs3d_Root):
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_WFPoleSurface(Prs3d_Root):
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_WFRestrictedFace(Prs3d_Root):
    @overload
    @staticmethod
    def Add(thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_Surface, theDrawUIso: bool, theDrawVIso: bool, theNbUIso: int, theNbVIso: int, theDrawer: Prs3d_Drawer, theCurves: Prs3d_NListOfSequenceOfPnt) -> None: ...
    @overload
    @staticmethod
    def Add(thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def AddUIso(thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer) -> None: ...
    @staticmethod
    def AddVIso(thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer) -> None: ...
    @overload
    @staticmethod
    def Match(theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_Surface, theDrawUIso: bool, theDrawVIso: bool, theDeflection: float, theNbUIso: int, theNbVIso: int, theDrawer: Prs3d_Drawer) -> bool: ...
    @overload
    @staticmethod
    def Match(theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer) -> bool: ...
    @staticmethod
    def MatchUIso(theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer) -> bool: ...
    @staticmethod
    def MatchVIso(theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_Surface, theDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_WFShape(Prs3d_Root):
    @staticmethod
    def Add(thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theIsParallel: Optional[bool] = False) -> None: ...
    @staticmethod
    def AddAllEdges(theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> Graphic3d_ArrayOfPrimitives: ...
    @overload
    @staticmethod
    def AddEdgesOnTriangulation(theShape: TopoDS_Shape, theToExcludeGeometric: Optional[bool] = True) -> Graphic3d_ArrayOfPrimitives: ...
    @overload
    @staticmethod
    def AddEdgesOnTriangulation(theSegments: TColgp_SequenceOfPnt, theShape: TopoDS_Shape, theToExcludeGeometric: Optional[bool] = True) -> None: ...
    @staticmethod
    def AddVertexes(theShape: TopoDS_Shape, theVertexMode: Prs3d_VertexDrawMode) -> Graphic3d_ArrayOfPoints: ...

class StdPrs_WFSurface(Prs3d_Root):
    @staticmethod
    def Add(aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_HLRPolyShape(StdPrs_HLRShapeI):
    def ComputeHLR(self, thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theProjector: Graphic3d_Camera) -> None: ...

class StdPrs_HLRShape(StdPrs_HLRShapeI):
    def ComputeHLR(self, thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theProjector: Graphic3d_Camera) -> None: ...

#classnotwrapped
class StdPrs_DeflectionCurve: ...

# harray1 classes
# harray2 classes
# hsequence classes

StdPrs_BRepFont_FindAndCreate = StdPrs_BRepFont.FindAndCreate
StdPrs_Curve_Add = StdPrs_Curve.Add
StdPrs_Curve_Add = StdPrs_Curve.Add
StdPrs_Curve_Add = StdPrs_Curve.Add
StdPrs_Curve_Add = StdPrs_Curve.Add
StdPrs_Curve_Match = StdPrs_Curve.Match
StdPrs_Curve_Match = StdPrs_Curve.Match
StdPrs_Curve_Match = StdPrs_Curve.Match
StdPrs_Curve_Match = StdPrs_Curve.Match
StdPrs_Isolines_Add = StdPrs_Isolines.Add
StdPrs_Isolines_Add = StdPrs_Isolines.Add
StdPrs_Isolines_AddOnSurface = StdPrs_Isolines.AddOnSurface
StdPrs_Isolines_AddOnSurface = StdPrs_Isolines.AddOnSurface
StdPrs_Isolines_AddOnSurface = StdPrs_Isolines.AddOnSurface
StdPrs_Isolines_AddOnTriangulation = StdPrs_Isolines.AddOnTriangulation
StdPrs_Isolines_AddOnTriangulation = StdPrs_Isolines.AddOnTriangulation
StdPrs_Isolines_AddOnTriangulation = StdPrs_Isolines.AddOnTriangulation
StdPrs_Isolines_UVIsoParameters = StdPrs_Isolines.UVIsoParameters
StdPrs_Plane_Add = StdPrs_Plane.Add
StdPrs_Plane_Match = StdPrs_Plane.Match
StdPrs_PoleCurve_Add = StdPrs_PoleCurve.Add
StdPrs_PoleCurve_Match = StdPrs_PoleCurve.Match
StdPrs_PoleCurve_Pick = StdPrs_PoleCurve.Pick
StdPrs_ShadedShape_Add = StdPrs_ShadedShape.Add
StdPrs_ShadedShape_Add = StdPrs_ShadedShape.Add
StdPrs_ShadedShape_AddWireframeForFacesWithoutTriangles = StdPrs_ShadedShape.AddWireframeForFacesWithoutTriangles
StdPrs_ShadedShape_AddWireframeForFreeElements = StdPrs_ShadedShape.AddWireframeForFreeElements
StdPrs_ShadedShape_ExploreSolids = StdPrs_ShadedShape.ExploreSolids
StdPrs_ShadedShape_FillFaceBoundaries = StdPrs_ShadedShape.FillFaceBoundaries
StdPrs_ShadedShape_FillTriangles = StdPrs_ShadedShape.FillTriangles
StdPrs_ShadedShape_FillTriangles = StdPrs_ShadedShape.FillTriangles
StdPrs_ShadedSurface_Add = StdPrs_ShadedSurface.Add
StdPrs_ShapeTool_IsPlanarFace = StdPrs_ShapeTool.IsPlanarFace
StdPrs_ToolPoint_Coord = StdPrs_ToolPoint.Coord
StdPrs_ToolTriangulatedShape_ClearOnOwnDeflectionChange = StdPrs_ToolTriangulatedShape.ClearOnOwnDeflectionChange
StdPrs_ToolTriangulatedShape_ComputeNormals = StdPrs_ToolTriangulatedShape.ComputeNormals
StdPrs_ToolTriangulatedShape_ComputeNormals = StdPrs_ToolTriangulatedShape.ComputeNormals
StdPrs_ToolTriangulatedShape_GetDeflection = StdPrs_ToolTriangulatedShape.GetDeflection
StdPrs_ToolTriangulatedShape_IsClosed = StdPrs_ToolTriangulatedShape.IsClosed
StdPrs_ToolTriangulatedShape_IsTessellated = StdPrs_ToolTriangulatedShape.IsTessellated
StdPrs_ToolTriangulatedShape_IsTriangulated = StdPrs_ToolTriangulatedShape.IsTriangulated
StdPrs_ToolTriangulatedShape_Normal = StdPrs_ToolTriangulatedShape.Normal
StdPrs_ToolTriangulatedShape_Tessellate = StdPrs_ToolTriangulatedShape.Tessellate
StdPrs_ToolVertex_Coord = StdPrs_ToolVertex.Coord
StdPrs_WFDeflectionRestrictedFace_Add = StdPrs_WFDeflectionRestrictedFace.Add
StdPrs_WFDeflectionRestrictedFace_Add = StdPrs_WFDeflectionRestrictedFace.Add
StdPrs_WFDeflectionRestrictedFace_AddUIso = StdPrs_WFDeflectionRestrictedFace.AddUIso
StdPrs_WFDeflectionRestrictedFace_AddVIso = StdPrs_WFDeflectionRestrictedFace.AddVIso
StdPrs_WFDeflectionRestrictedFace_Match = StdPrs_WFDeflectionRestrictedFace.Match
StdPrs_WFDeflectionRestrictedFace_Match = StdPrs_WFDeflectionRestrictedFace.Match
StdPrs_WFDeflectionRestrictedFace_MatchUIso = StdPrs_WFDeflectionRestrictedFace.MatchUIso
StdPrs_WFDeflectionRestrictedFace_MatchVIso = StdPrs_WFDeflectionRestrictedFace.MatchVIso
StdPrs_WFDeflectionSurface_Add = StdPrs_WFDeflectionSurface.Add
StdPrs_WFPoleSurface_Add = StdPrs_WFPoleSurface.Add
StdPrs_WFRestrictedFace_Add = StdPrs_WFRestrictedFace.Add
StdPrs_WFRestrictedFace_Add = StdPrs_WFRestrictedFace.Add
StdPrs_WFRestrictedFace_AddUIso = StdPrs_WFRestrictedFace.AddUIso
StdPrs_WFRestrictedFace_AddVIso = StdPrs_WFRestrictedFace.AddVIso
StdPrs_WFRestrictedFace_Match = StdPrs_WFRestrictedFace.Match
StdPrs_WFRestrictedFace_Match = StdPrs_WFRestrictedFace.Match
StdPrs_WFRestrictedFace_MatchUIso = StdPrs_WFRestrictedFace.MatchUIso
StdPrs_WFRestrictedFace_MatchVIso = StdPrs_WFRestrictedFace.MatchVIso
StdPrs_WFShape_Add = StdPrs_WFShape.Add
StdPrs_WFShape_AddAllEdges = StdPrs_WFShape.AddAllEdges
StdPrs_WFShape_AddEdgesOnTriangulation = StdPrs_WFShape.AddEdgesOnTriangulation
StdPrs_WFShape_AddEdgesOnTriangulation = StdPrs_WFShape.AddEdgesOnTriangulation
StdPrs_WFShape_AddVertexes = StdPrs_WFShape.AddVertexes
StdPrs_WFSurface_Add = StdPrs_WFSurface.Add
