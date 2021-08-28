# -*- coding=UTF-8 -*-
# This typing file was generated by typing_from_help.py
"""
win32gui
"""

from typing import *

from ._pywin32 import *

class error(Exception):
    """
    error(*args, **kw)

    Common base class for all non-exit exceptions.
    """

    __weakref__: ...
    """
    list of weak references to the object (if defined)
    """
    def __init__(self, *args, **kw):
        """ """
        ...
    ...

def AbortPath(*args, **kwargs):
    """ """
    ...

def AlphaBlend(*args, **kwargs):
    """ """
    ...

def AngleArc(*args, **kwargs):
    """ """
    ...

def AnimateWindow(*args, **kwargs):
    """ """
    ...

def AppendMenu(*args, **kwargs):
    """ """
    ...

def Arc(*args, **kwargs):
    """ """
    ...

def ArcTo(*args, **kwargs):
    """ """
    ...

def BeginPaint(*args, **kwargs):
    """ """
    ...

def BeginPath(*args, **kwargs):
    """ """
    ...

def BitBlt(
    hdcDest: int,
    x: int,
    y: int,
    width: int,
    height: int,
    hdcSrc: int,
    nXSrc: int,
    nYSrc: int,
    dwRop: int,
) -> None:
    """ """
    ...

def BringWindowToTop(*args, **kwargs):
    """ """
    ...

def CallWindowProc(*args, **kwargs):
    """ """
    ...

def CheckMenuItem(*args, **kwargs):
    """ """
    ...

def CheckMenuRadioItem(*args, **kwargs):
    """ """
    ...

def ChildWindowFromPoint(*args, **kwargs):
    """ """
    ...

def ChildWindowFromPointEx(*args, **kwargs):
    """ """
    ...

def Chord(*args, **kwargs):
    """ """
    ...

def ClientToScreen(hWnd: int, Point: Tuple[int, int]) -> Tuple[int, int]:
    """Convert client coordinates to screen coords

    Args:
        hWnd (int): Handle to a window
        Point (Tuple[int, int]): Client coordinates to be converted

    Returns:
        Tuple[int, int]: screen coords
    """
    ...

def CloseFigure(*args, **kwargs):
    """ """
    ...

def CloseWindow(*args, **kwargs):
    """ """
    ...

def CombineRgn(*args, **kwargs):
    """ """
    ...

def CombineTransform(*args, **kwargs):
    """ """
    ...

def CommDlgExtendedError(*args, **kwargs):
    """ """
    ...

def CopyIcon(*args, **kwargs):
    """ """
    ...

def CreateAcceleratorTable(*args, **kwargs):
    """ """
    ...

def CreateBitmap(*args, **kwargs):
    """ """
    ...

def CreateBrushIndirect(*args, **kwargs):
    """ """
    ...

def CreateCaret(*args, **kwargs):
    """ """
    ...

def CreateCompatibleBitmap(*args, **kwargs):
    """ """
    ...

def CreateCompatibleDC(*args, **kwargs):
    """ """
    ...

def CreateDC(*args, **kwargs):
    """ """
    ...

def CreateDialogIndirect(*args, **kwargs):
    """ """
    ...

def CreateDialogIndirectParam(*args, **kwargs):
    """ """
    ...

def CreateEllipticRgnIndirect(*args, **kwargs):
    """ """
    ...

def CreateFontIndirect(*args, **kwargs):
    """ """
    ...

def CreateHatchBrush(*args, **kwargs):
    """ """
    ...

def CreateIconFromResource(*args, **kwargs):
    """ """
    ...

def CreateIconIndirect(*args, **kwargs):
    """ """
    ...

def CreateMenu(*args, **kwargs):
    """ """
    ...

def CreatePatternBrush(*args, **kwargs):
    """ """
    ...

def CreatePen(*args, **kwargs):
    """ """
    ...

def CreatePolygonRgn(*args, **kwargs):
    """ """
    ...

def CreatePopupMenu(*args, **kwargs):
    """ """
    ...

def CreateRectRgnIndirect(*args, **kwargs):
    """ """
    ...

def CreateRoundRectRgn(*args, **kwargs):
    """ """
    ...

def CreateSolidBrush(*args, **kwargs):
    """ """
    ...

def CreateWindow(*args, **kwargs):
    """ """
    ...

def CreateWindowEx(*args, **kwargs):
    """ """
    ...

def DefWindowProc(*args, **kwargs):
    """ """
    ...

def DeleteDC(*args, **kwargs):
    """ """
    ...

def DeleteMenu(*args, **kwargs):
    """ """
    ...

def DeleteObject(handle: int) -> None:
    """
    Deletes a logical pen, brush, font, bitmap, region, or palette,
    freeing all system resources associated with the object.
    After the object is deleted, the specified handle is no longer valid.

    Args:
        handle (int): handle to the object to delete.
    """
    ...

def DestroyAcceleratorTable(*args, **kwargs):
    """ """
    ...

def DestroyCaret(*args, **kwargs):
    """ """
    ...

def DestroyIcon(*args, **kwargs):
    """ """
    ...

def DestroyMenu(*args, **kwargs):
    """ """
    ...

def DestroyWindow(*args, **kwargs):
    """ """
    ...

def DialogBox(*args, **kwargs):
    """ """
    ...

def DialogBoxIndirect(*args, **kwargs):
    """ """
    ...

def DialogBoxIndirectParam(*args, **kwargs):
    """ """
    ...

def DialogBoxParam(*args, **kwargs):
    """ """
    ...

def DispatchMessage(*args, **kwargs):
    """ """
    ...

def DragAcceptFiles(*args, **kwargs):
    """ """
    ...

def DragDetect(*args, **kwargs):
    """ """
    ...

def DrawAnimatedRects(*args, **kwargs):
    """ """
    ...

def DrawEdge(*args, **kwargs):
    """ """
    ...

def DrawFocusRect(*args, **kwargs):
    """ """
    ...

def DrawIcon(*args, **kwargs):
    """ """
    ...

def DrawIconEx(*args, **kwargs):
    """ """
    ...

def DrawMenuBar(*args, **kwargs):
    """ """
    ...

def DrawText(*args, **kwargs):
    """ """
    ...

def DrawTextW(*args, **kwargs):
    """ """
    ...

def Edit_GetLine(*args, **kwargs):
    """ """
    ...

def Ellipse(*args, **kwargs):
    """ """
    ...

def EnableMenuItem(*args, **kwargs):
    """ """
    ...

def EnableWindow(*args, **kwargs):
    """ """
    ...

def EndDialog(*args, **kwargs):
    """ """
    ...

def EndPaint(*args, **kwargs):
    """ """
    ...

def EndPath(*args, **kwargs):
    """ """
    ...

def EnumChildWindows(*args, **kwargs):
    """ """
    ...

def EnumFontFamilies(*args, **kwargs):
    """ """
    ...

def EnumPropsEx(*args, **kwargs):
    """ """
    ...

def EnumThreadWindows(
    dwThreadId: int, callback: Callable[[int, T], None], extra: T
) -> None:
    """ """
    ...

def EnumWindows(*args, **kwargs):
    """ """
    ...

def EqualRgn(*args, **kwargs):
    """ """
    ...

def ExtCreatePen(*args, **kwargs):
    """ """
    ...

def ExtFloodFill(*args, **kwargs):
    """ """
    ...

def ExtTextOut(*args, **kwargs):
    """ """
    ...

def ExtractIcon(*args, **kwargs):
    """ """
    ...

def ExtractIconEx(*args, **kwargs):
    """ """
    ...

def FillPath(*args, **kwargs):
    """ """
    ...

def FillRect(*args, **kwargs):
    """ """
    ...

def FillRgn(*args, **kwargs):
    """ """
    ...

def FindWindow(ClassName: Text = None, WindowName: Text = None) -> int:
    """Retrieves a handle to the top-level window whose class name and window name match the specified strings.

    Args:
        ClassName (Text, optional): Name or atom of window class to find. Defaults to None.
        WindowName (Text, optional): Title of window to find. Defaults to None.

    Returns:
        int: PyHANDLE
    """
    ...

def FindWindowEx(*args, **kwargs):
    """ """
    ...

def FlashWindow(*args, **kwargs):
    """ """
    ...

def FlashWindowEx(*args, **kwargs):
    """ """
    ...

def FlattenPath(*args, **kwargs):
    """ """
    ...

def FrameRect(*args, **kwargs):
    """ """
    ...

def FrameRgn(*args, **kwargs):
    """ """
    ...

def GetActiveWindow(*args, **kwargs):
    """ """
    ...

def GetArcDirection(*args, **kwargs):
    """ """
    ...

def GetBkColor(*args, **kwargs):
    """ """
    ...

def GetBkMode(*args, **kwargs):
    """ """
    ...

def GetCapture(*args, **kwargs):
    """ """
    ...

def GetCaretPos(*args, **kwargs):
    """ """
    ...

def GetClassLong(*args, **kwargs):
    """ """
    ...

def GetClassName(hwnd: int) -> Text:
    """ """
    ...

def GetClientRect(hwnd: int) -> PyRECT:
    """Returns the rectangle of the client area of a window, in client coordinates

    Args:
        hwnd (int): The handle to the window

    Returns:
        PyRECT: (0, 0, width, height)
    """
    ...

def GetCurrentObject(*args, **kwargs):
    """ """
    ...

def GetCurrentPositionEx(*args, **kwargs):
    """ """
    ...

def GetCursor(*args, **kwargs):
    """ """
    ...

def GetCursorInfo(*args, **kwargs):
    """ """
    ...

def GetCursorPos() -> Tuple[int, int]:
    """Returns the position of the cursor, in screen co-ordinates."""
    ...

def GetDC(*args, **kwargs):
    """ """
    ...

def GetDesktopWindow(*args, **kwargs):
    """ """
    ...

def GetDlgCtrlID(*args, **kwargs):
    """ """
    ...

def GetDlgItem(*args, **kwargs):
    """ """
    ...

def GetDlgItemInt(*args, **kwargs):
    """ """
    ...

def GetDlgItemText(*args, **kwargs):
    """ """
    ...

def GetDoubleClickTime(*args, **kwargs):
    """ """
    ...

def GetFocus(*args, **kwargs):
    """ """
    ...

def GetForegroundWindow() -> int:
    """ """
    ...

def GetGraphicsMode(*args, **kwargs):
    """ """
    ...

def GetIconInfo(*args, **kwargs):
    """ """
    ...

def GetLayeredWindowAttributes(*args, **kwargs):
    """ """
    ...

def GetLayout(*args, **kwargs):
    """ """
    ...

def GetMapMode(*args, **kwargs):
    """ """
    ...

def GetMenu(*args, **kwargs):
    """ """
    ...

def GetMenuDefaultItem(*args, **kwargs):
    """ """
    ...

def GetMenuInfo(*args, **kwargs):
    """ """
    ...

def GetMenuItemCount(*args, **kwargs):
    """ """
    ...

def GetMenuItemID(*args, **kwargs):
    """ """
    ...

def GetMenuItemInfo(*args, **kwargs):
    """ """
    ...

def GetMenuItemRect(*args, **kwargs):
    """ """
    ...

def GetMenuState(*args, **kwargs):
    """ """
    ...

def GetMessage(*args, **kwargs):
    """ """
    ...

def GetMiterLimit(*args, **kwargs):
    """ """
    ...

def GetModuleHandle(*args, **kwargs):
    """ """
    ...

def GetNextDlgGroupItem(*args, **kwargs):
    """ """
    ...

def GetNextDlgTabItem(*args, **kwargs):
    """ """
    ...

def GetObject(*args, **kwargs):
    """ """
    ...

def GetObjectType(*args, **kwargs):
    """ """
    ...

def GetOpenFileName(*args, **kwargs):
    """ """
    ...

def GetOpenFileNameW(*args, **kwargs):
    """ """
    ...

def GetParent(*args, **kwargs):
    """ """
    ...

def GetPath(*args, **kwargs):
    """ """
    ...

def GetPixel(*args, **kwargs):
    """ """
    ...

def GetPolyFillMode(*args, **kwargs):
    """ """
    ...

def GetROP2(*args, **kwargs):
    """ """
    ...

def GetRgnBox(*args, **kwargs):
    """ """
    ...

def GetSaveFileNameW(*args, **kwargs):
    """ """
    ...

def GetScrollInfo(*args, **kwargs):
    """ """
    ...

def GetStockObject(*args, **kwargs):
    """ """
    ...

def GetStretchBltMode(*args, **kwargs):
    """ """
    ...

def GetSubMenu(*args, **kwargs):
    """ """
    ...

def GetSysColor(*args, **kwargs):
    """ """
    ...

def GetSysColorBrush(*args, **kwargs):
    """ """
    ...

def GetSystemMenu(*args, **kwargs):
    """ """
    ...

def GetTextAlign(*args, **kwargs):
    """ """
    ...

def GetTextCharacterExtra(*args, **kwargs):
    """ """
    ...

def GetTextColor(*args, **kwargs):
    """ """
    ...

def GetTextExtentPoint32(*args, **kwargs):
    """ """
    ...

def GetTextFace(*args, **kwargs):
    """ """
    ...

def GetTextMetrics(*args, **kwargs):
    """ """
    ...

def GetUpdateRgn(*args, **kwargs):
    """ """
    ...

def GetViewportExtEx(*args, **kwargs):
    """ """
    ...

def GetViewportOrgEx(*args, **kwargs):
    """ """
    ...

def GetWindow(*args, **kwargs):
    """ """
    ...

def GetWindowDC(hwnd: int) -> int:
    """
    Gets the windows current DC handle.
    """
    ...

def GetWindowExtEx(*args, **kwargs):
    """ """
    ...

def GetWindowLong(*args, **kwargs):
    """ """
    ...

def GetWindowOrgEx(*args, **kwargs):
    """ """
    ...

def GetWindowPlacement(*args, **kwargs):
    """ """
    ...

def GetWindowRect(hwnd: int) -> Tuple[int, int, int, int]:
    """
    Returns the screen coordinates of the windows (left, top, right, bottom)
    """
    ...

def GetWindowRgn(*args, **kwargs):
    """ """
    ...

def GetWindowText(*args, **kwargs):
    """ """
    ...

def GetWindowTextLength(*args, **kwargs):
    """ """
    ...

def GetWorldTransform(*args, **kwargs):
    """ """
    ...

def GradientFill(*args, **kwargs):
    """ """
    ...

def HIWORD(*args, **kwargs):
    """ """
    ...

def HideCaret(*args, **kwargs):
    """ """
    ...

def ImageList_Add(*args, **kwargs):
    """ """
    ...

def ImageList_Create(*args, **kwargs):
    """ """
    ...

def ImageList_Destroy(*args, **kwargs):
    """ """
    ...

def ImageList_Draw(*args, **kwargs):
    """ """
    ...

def ImageList_DrawEx(*args, **kwargs):
    """ """
    ...

def ImageList_GetIcon(*args, **kwargs):
    """ """
    ...

def ImageList_GetImageCount(*args, **kwargs):
    """ """
    ...

def ImageList_LoadBitmap(*args, **kwargs):
    """ """
    ...

def ImageList_LoadImage(*args, **kwargs):
    """ """
    ...

def ImageList_Remove(*args, **kwargs):
    """ """
    ...

def ImageList_Replace(*args, **kwargs):
    """ """
    ...

def ImageList_ReplaceIcon(*args, **kwargs):
    """ """
    ...

def ImageList_SetBkColor(*args, **kwargs):
    """ """
    ...

def ImageList_SetOverlayImage(*args, **kwargs):
    """ """
    ...

def InitCommonControls(*args, **kwargs):
    """ """
    ...

def InitCommonControlsEx(*args, **kwargs):
    """ """
    ...

def InsertMenu(*args, **kwargs):
    """ """
    ...

def InsertMenuItem(*args, **kwargs):
    """ """
    ...

def InvalidateRect(hWnd: int, Rect: Optional[PyRECT], Erase: bool) -> None:
    """Invalidates a rectangular area of a window and adds it to the window's update region

    Args:
        hWnd (int): Handle to the window
        Rect (Optional[PyRECT]): Client coordinates defining area to be redrawn. Use None for entire client area.
        Erase (bool): Indicates if background should be erased.
    """
    ...

def InvalidateRgn(*args, **kwargs):
    """ """
    ...

def InvertRect(*args, **kwargs):
    """ """
    ...

def InvertRgn(*args, **kwargs):
    """ """
    ...

def IsChild(*args, **kwargs):
    """ """
    ...

def IsIconic(*args, **kwargs):
    """ """
    ...

def IsWindow(hWnd: int) -> bool:
    """ """
    ...

def IsWindowEnabled(*args, **kwargs):
    """ """
    ...

def IsWindowVisible(*args, **kwargs):
    """ """
    ...

def LOGFONT(*args, **kwargs):
    """ """
    ...

def LOWORD(*args, **kwargs):
    """ """
    ...

def LineTo(*args, **kwargs):
    """ """
    ...

def ListView_SortItems(*args, **kwargs):
    """ """
    ...

def ListView_SortItemsEx(*args, **kwargs):
    """ """
    ...

def LoadCursor(*args, **kwargs):
    """ """
    ...

def LoadIcon(*args, **kwargs):
    """ """
    ...

def LoadImage(*args, **kwargs):
    """ """
    ...

def LoadMenu(*args, **kwargs):
    """ """
    ...

def MaskBlt(*args, **kwargs):
    """ """
    ...

def MessageBeep(*args, **kwargs):
    """ """
    ...

def MessageBox(parent: int, text: Text, caption: Text, flags: int) -> int:
    """ """
    ...

def ModifyMenu(*args, **kwargs):
    """ """
    ...

def ModifyWorldTransform(*args, **kwargs):
    """ """
    ...

def MoveToEx(*args, **kwargs):
    """ """
    ...

def MoveWindow(*args, **kwargs):
    """ """
    ...

def OffsetRgn(*args, **kwargs):
    """ """
    ...

def PaintDesktop(*args, **kwargs):
    """ """
    ...

def PaintRgn(*args, **kwargs):
    """ """
    ...

def PatBlt(*args, **kwargs):
    """ """
    ...

def PathToRegion(*args, **kwargs):
    """ """
    ...

def PeekMessage(*args, **kwargs):
    """ """
    ...

def Pie(*args, **kwargs):
    """ """
    ...

def PlgBlt(*args, **kwargs):
    """ """
    ...

def PolyBezier(*args, **kwargs):
    """ """
    ...

def PolyBezierTo(*args, **kwargs):
    """ """
    ...

def Polygon(*args, **kwargs):
    """ """
    ...

def Polyline(*args, **kwargs):
    """ """
    ...

def PolylineTo(*args, **kwargs):
    """ """
    ...

def PostMessage(hwnd: int, message: int, wparam: int, lparam: int) -> None:
    """ """
    ...

def PostQuitMessage(*args, **kwargs):
    """ """
    ...

def PostThreadMessage(*args, **kwargs):
    """ """
    ...

def PtInRect(*args, **kwargs):
    """ """
    ...

def PtInRegion(*args, **kwargs):
    """ """
    ...

def PumpMessages(*args, **kwargs):
    """ """
    ...

def PumpWaitingMessages(*args, **kwargs):
    """ """
    ...

def PyGetArraySignedLong(*args, **kwargs):
    """ """
    ...

def PyGetBufferAddressAndLen(*args, **kwargs):
    """ """
    ...

def PyGetMemory(*args, **kwargs):
    """ """
    ...

def PyGetString(*args, **kwargs):
    """ """
    ...

def PyMakeBuffer(*args, **kwargs):
    """ """
    ...

def PySetMemory(*args, **kwargs):
    """ """
    ...

def PySetString(*args, **kwargs):
    """ """
    ...

def RectInRegion(*args, **kwargs):
    """ """
    ...

def Rectangle(*args, **kwargs):
    """ """
    ...

def RedrawWindow(*args, **kwargs):
    """ """
    ...

def RegisterClass(*args, **kwargs):
    """ """
    ...

def RegisterDeviceNotification(*args, **kwargs):
    """ """
    ...

def RegisterHotKey(*args, **kwargs):
    """ """
    ...

def RegisterWindowMessage(*args, **kwargs):
    """ """
    ...

def ReleaseCapture(*args, **kwargs):
    """ """
    ...

def ReleaseDC(hWnd: int, hDC: int) -> int:
    """Releases a device context.

    Args:
        hWnd (int): handle to window
        hDC (int): handle to device context
    """
    ...

def RemoveMenu(*args, **kwargs):
    """ """
    ...

def ReplyMessage(*args, **kwargs):
    """ """
    ...

def RestoreDC(*args, **kwargs):
    """ """
    ...

def RoundRect(*args, **kwargs):
    """ """
    ...

def SaveDC(*args, **kwargs):
    """ """
    ...

def ScreenToClient(*args, **kwargs):
    """ """
    ...

def ScrollWindowEx(*args, **kwargs):
    """ """
    ...

def SelectObject(*args, **kwargs):
    """ """
    ...

def SendMessage(
    hwnd: int,
    message: int,
    wparam: Union[int, Text] = None,
    lparam: Union[int, Text] = None,
) -> int:
    """Sends a message to the window.

    Args:
        hwnd (int): The handle to the Window
        message (int): The ID of the message to post
        wparam (Union[int, Text], optional): Type depends on the message. Defaults to None.
        lparam (Union[int, Text], optional): Type depends on the message. Defaults to None.

    Returns:
        int
    """
    ...

def SendMessageTimeout(*args, **kwargs):
    """ """
    ...

def SetActiveWindow(*args, **kwargs):
    """ """
    ...

def SetArcDirection(*args, **kwargs):
    """ """
    ...

def SetBkColor(*args, **kwargs):
    """ """
    ...

def SetBkMode(*args, **kwargs):
    """ """
    ...

def SetCapture(*args, **kwargs):
    """ """
    ...

def SetCaretPos(*args, **kwargs):
    """ """
    ...

def SetCursor(*args, **kwargs):
    """ """
    ...

def SetDlgItemInt(*args, **kwargs):
    """ """
    ...

def SetDlgItemText(*args, **kwargs):
    """ """
    ...

def SetDoubleClickTime(*args, **kwargs):
    """ """
    ...

def SetFocus(*args, **kwargs):
    """ """
    ...

def SetForegroundWindow(hwnd: int) -> int:
    """

    Args:
        hwnd (int): The handle to the window

    Returns:
        int: hwnd
    """
    ...

def SetGraphicsMode(*args, **kwargs):
    """ """
    ...

def SetLayeredWindowAttributes(*args, **kwargs):
    """ """
    ...

def SetLayout(*args, **kwargs):
    """ """
    ...

def SetMapMode(*args, **kwargs):
    """ """
    ...

def SetMenu(*args, **kwargs):
    """ """
    ...

def SetMenuDefaultItem(*args, **kwargs):
    """ """
    ...

def SetMenuInfo(*args, **kwargs):
    """ """
    ...

def SetMenuItemBitmaps(*args, **kwargs):
    """ """
    ...

def SetMenuItemInfo(*args, **kwargs):
    """ """
    ...

def SetMiterLimit(*args, **kwargs):
    """ """
    ...

def SetParent(*args, **kwargs):
    """ """
    ...

def SetPixel(*args, **kwargs):
    """ """
    ...

def SetPixelV(*args, **kwargs):
    """ """
    ...

def SetPolyFillMode(*args, **kwargs):
    """ """
    ...

def SetROP2(*args, **kwargs):
    """ """
    ...

def SetRectRgn(*args, **kwargs):
    """ """
    ...

def SetScrollInfo(*args, **kwargs):
    """ """
    ...

def SetStretchBltMode(*args, **kwargs):
    """ """
    ...

def SetTextAlign(*args, **kwargs):
    """ """
    ...

def SetTextCharacterExtra(*args, **kwargs):
    """ """
    ...

def SetTextColor(*args, **kwargs):
    """ """
    ...

def SetViewportExtEx(*args, **kwargs):
    """ """
    ...

def SetViewportOrgEx(*args, **kwargs):
    """ """
    ...

def SetWindowExtEx(*args, **kwargs):
    """ """
    ...

def SetWindowLong(*args, **kwargs):
    """ """
    ...

def SetWindowOrgEx(*args, **kwargs):
    """ """
    ...

def SetWindowPlacement(*args, **kwargs):
    """ """
    ...

def SetWindowPos(
    hWnd: int, InsertAfter: int, X: int, Y: int, cx: int, cy: int, Flags: int
) -> None:
    """ """
    ...

def SetWindowRgn(*args, **kwargs):
    """ """
    ...

def SetWindowText(*args, **kwargs):
    """ """
    ...

def SetWorldTransform(*args, **kwargs):
    """ """
    ...

def Shell_NotifyIcon(*args, **kwargs):
    """ """
    ...

def ShowCaret(*args, **kwargs):
    """ """
    ...

def ShowWindow(hWnd: int, cmdShow: int) -> None:
    """Shows or hides a window and changes its state

    Parameters
        hWnd : int
            The handle to the window

        cmdShow : int
            Combination of win32con.SW_* flags
    """
    ...

def StretchBlt(*args, **kwargs):
    """ """
    ...

def StrokeAndFillPath(*args, **kwargs):
    """ """
    ...

def StrokePath(*args, **kwargs):
    """ """
    ...

def SystemParametersInfo(*args, **kwargs):
    """ """
    ...

def TrackPopupMenu(*args, **kwargs):
    """ """
    ...

def TranslateAccelerator(*args, **kwargs):
    """ """
    ...

def TranslateMessage(*args, **kwargs):
    """ """
    ...

def TransparentBlt(*args, **kwargs):
    """ """
    ...

def UnregisterClass(*args, **kwargs):
    """ """
    ...

def UnregisterDeviceNotification(*args, **kwargs):
    """ """
    ...

def UpdateLayeredWindow(*args, **kwargs):
    """ """
    ...

def UpdateWindow(*args, **kwargs):
    """ """
    ...

def ValidateRect(*args, **kwargs):
    """ """
    ...

def ValidateRgn(*args, **kwargs):
    """ """
    ...

def WNDCLASS(*args, **kwargs):
    """ """
    ...

def WaitMessage(*args, **kwargs):
    """ """
    ...

def WidenPath(*args, **kwargs):
    """ """
    ...

def WindowFromDC(*args, **kwargs):
    """ """
    ...

def WindowFromPoint(*args, **kwargs):
    """ """
    ...

def _TrackMouseEvent(*args, **kwargs):
    """ """
    ...

def lpstr(*args, **kwargs):
    """ """
    ...

CLR_NONE: int = -1

ILC_COLOR: int = 0

ILC_COLOR16: int = 16

ILC_COLOR24: int = 24

ILC_COLOR32: int = 32

ILC_COLOR4: int = 4

ILC_COLOR8: int = 8

ILC_COLORDDB: int = 254

ILC_MASK: int = 1

ILD_BLEND: int = 4

ILD_BLEND25: int = 2

ILD_BLEND50: int = 4

ILD_FOCUS: int = 2

ILD_MASK: int = 16

ILD_NORMAL: int = 0

ILD_SELECTED: int = 4

ILD_TRANSPARENT: int = 1

IMAGE_BITMAP: int = 0

IMAGE_CURSOR: int = 2

IMAGE_ICON: int = 1

LR_CREATEDIBSECTION: int = 8192

LR_DEFAULTCOLOR: int = 0

LR_DEFAULTSIZE: int = 64

LR_LOADFROMFILE: int = 16

LR_LOADMAP3DCOLORS: int = 4096

LR_LOADTRANSPARENT: int = 32

LR_MONOCHROME: int = 1

LR_SHARED: int = 32768

LR_VGACOLOR: int = 128

NIF_ICON: int = 2

NIF_INFO: int = 16

NIF_MESSAGE: int = 1

NIF_STATE: int = 8

NIF_TIP: int = 4

NIIF_ERROR: int = 3

NIIF_ICON_MASK: int = 15

NIIF_INFO: int = 1

NIIF_NONE: int = 0

NIIF_NOSOUND: int = 16

NIIF_WARNING: int = 2

NIM_ADD: int = 0

NIM_DELETE: int = 2

NIM_MODIFY: int = 1

NIM_SETVERSION: int = 4

TPM_BOTTOMALIGN: int = 32

TPM_CENTERALIGN: int = 4

TPM_LEFTALIGN: int = 0

TPM_LEFTBUTTON: int = 0

TPM_NONOTIFY: int = 128

TPM_RETURNCMD: int = 256

TPM_RIGHTALIGN: int = 8

TPM_RIGHTBUTTON: int = 2

TPM_TOPALIGN: int = 0

TPM_VCENTERALIGN: int = 16

UNICODE: bool
"""
True
"""

__all__: ...
"""
['AbortPath', 'AlphaBlend', 'AngleArc', 'AnimateWindow', 'Ap...
"""

dllhandle: int = 1613234176