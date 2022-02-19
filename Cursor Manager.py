import win32api
import time
import win32gui
import win32con
import ctypes

hold = win32gui.LoadImage(0, 32512, win32con.IMAGE_CURSOR, 
                          0, 0, win32con.LR_SHARED )
hsave = ctypes.windll.user32.CopyImage(hold, win32con.IMAGE_CURSOR, 
                                       0, 0, win32con.LR_COPYFROMRESOURCE)
hcursor = win32gui.LoadImage(0, 'cursors/1.cur', 
                             win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE);
ctypes.windll.user32.SetSystemCursor(hcursor, 32512)
time.sleep(5)

#restore the old cursor
ctypes.windll.user32.SetSystemCursor(hsave, 32512)
