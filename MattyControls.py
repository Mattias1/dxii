from tkinter import *
from tkinter.ttk import *


# The constants
H_LEFT        = 0
H_COPY_LEFT   = 1
H_CENTER      = 2
H_COPY_RIGHT  = 3
H_RIGHT       = 4
V_TOP         = 0
V_COPY_TOP    = 1
V_MIDDLE      = 2
V_COPY_BOTTOM = 3
V_BOTTOM      = 4


#
#   Frame functions
#
def frame_init(frame, master, frameInsideTab = False):
    """Initialize the frame, so that it's properties are properly set."""
    Frame.__init__(frame, master)
    master.update_idletasks() # This fires all events that update unnescessary things like width and height
    h = master.winfo_height()
    if frameInsideTab:
        h -= 20
    frame.place(width=master.winfo_width(), height=h)

def frame_x(frame):
    """Get the frame's x coordinate."""
    return 0

def frame_y(frame):
    """Get the frame's y coordinate."""
    return 0

def frame_width(frame):
    """Get the frame's width."""
    return int(frame.place_info().get('width'))

def frame_height(frame):
    """Get the frame's width."""
    return int(frame.place_info().get('height'))


#
#   The button class
#
class Btn(Button):
    """Matty's button class"""

    # Init method
    def __init__(self, parent, **kwargs):
        """Create a button given it's text and it's parent frame."""
        Button.__init__(self, parent, **kwargs)
        if self.place_info().get('width', '') == '':
            self.width = 90
        if self.place_info().get('height', '') == '':
            self.height = 26
        self.label = None

    # Some getters and setters
    x = property(lambda self: int(self.place_info()['x']), lambda self, val: self.place(x = val))
    y = property(lambda self: int(self.place_info()['y']), lambda self, val: self.place(y = val))
    width = property(lambda self: int(self.place_info()['width']), lambda self, val: self.place(width = val))
    height = property(lambda self: int(self.place_info()['height']), lambda self, val: self.place(height = val))
    text = property(lambda self: self["text"], lambda self, val: self.configure(text = val))
    command = property(lambda self: self["command"], lambda self, val: self.configure(command = val))

    # The positioning methods
    def locateInside(self, c, h=H_LEFT, v=V_TOP, d=10):
        """Locate the current control inside c at the horizontal placement h, the vertical placement v and with a margin of d"""
        x = 0
        y = 0

        if h == H_LEFT:        x = d
        if h == H_COPY_LEFT:   x = frame_x(c)
        if h == H_CENTER:      x = (frame_width(c) - self.width) / 2
        if h == H_COPY_RIGHT:  x = c.x + frame_width(c) - self.width
        if h == H_RIGHT:       x = frame_width(c) - self.width - d

        if v == V_TOP:         y = d
        if v == V_COPY_TOP:    y = frame_y(c)
        if v == V_MIDDLE:      y = (frame_height(c) - self.height) / 2
        if v == V_COPY_BOTTOM: y = frame_y(c) + c.height - self.height
        if v == V_BOTTOM:      y = frame_height(c) - self.height - d

        self.place(x=x, y=y)

    def locateFrom(self, c, h=H_LEFT, v=V_TOP, d=10):
        """Locate the current control relative to c at the horizontal placement h, the vertical placement v and with a margin of d"""
        x = 0
        y = 0

        if h == H_LEFT:        x = c.x - self.width - d
        if h == H_COPY_LEFT:   x = c.x
        if h == H_CENTER:      x = c.x + (c.width - self.width) / 2
        if h == H_COPY_RIGHT:  x = c.x + c.width - self.width
        if h == H_RIGHT:       x = c.x + c.width + d

        if v == V_TOP:         y = c.y - self.height - d
        if v == V_COPY_TOP:    y = c.y
        if v == V_MIDDLE:      y = c.y + (c.height - self.height) / 2
        if v == V_COPY_BOTTOM: y = c.y + c.height - self.height
        if v == V_BOTTOM:      y = c.y + c.height + d

        self.place(x=x, y=y)
        
    def addLabel(self, text, d=10, moveCtrl=True, labelWidth=0):
        """ Create a label and add it on front of the control we want to add it to (self)"""
        lbl = Lbl(self.master, text=text);

        # Set its width
        if (labelWidth > 0):
            lbl.width = labelWidth

        # Give it the right position
        if (moveCtrl):
            lbl.locateFrom(self, H_COPY_LEFT, V_MIDDLE, d);
            self.locateFrom(lbl, H_RIGHT, V_MIDDLE, d);
        else:
            lbl.locateFrom(self, H_LEFT, V_MIDDLE, d);

        # Return the label, for the sake of easyness
        self.label = lbl
        return lbl;


#
#   The label class
#
class Lbl(Label):
    """Matty's label class"""

    # Init method
    def __init__(self, parent, **kwargs):
        """Create a label."""
        Label.__init__(self, parent, **kwargs)
        if self.place_info().get('width', '') == '':
            self.width = 100
        if self.place_info().get('height', '') == '':
            self.height = 20

    # Some getters and setters
    x = Btn.x
    y = Btn.y
    width = Btn.width
    height = Btn.height
    text = Btn.text

    # The positioning methods
    def locateInside(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateInside(self, c, h, v, d)

    def locateFrom(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateFrom(self, c, h, v, d)


#
#   The textbox (entry) class
#
class Tb(Entry):
    """Matty's textbox class"""

    # Init method
    def __init__(self, parent, **kwargs):
        """Create a textbox."""
        Entry.__init__(self, parent, **kwargs)
        if self.place_info().get('width', '') == '':
            self.width = 120
        if self.place_info().get('height', '') == '':
            self.height = 22
        self.label = None

    # Some getters and setters
    x = Btn.x
    y = Btn.y
    width = Btn.width
    height = Btn.height
    command = Btn.command
    value = property(lambda self: self.get(), lambda self, val: self.setValue(val))
    def setValue(self, val):
        self.delete(0, END)
        self.insert(0, val)

    # The positioning methods
    def locateInside(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateInside(self, c, h, v, d)

    def locateFrom(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateFrom(self, c, h, v, d)

    def addLabel(self, text, d=10, moveCtrl=True, labelWidth=0):
        Btn.addLabel(self, text, d, moveCtrl, labelWidth)


#
#   The multiline textbox (text) class
#
class TbM(Text):
    """Matty's textbox class"""

    # Init method
    def __init__(self, parent, **kwargs):
        """Create a textbox."""
        Text.__init__(self, parent, **kwargs)
        if self.place_info().get('width', '') == '':
            self.width = 200
        if self.place_info().get('height', '') == '':
            self.height = 84
        self.label = None
        # onChange stuff
        self.onChange = None
        self._resetModified()
        self.bind_all('<<Modified>>', self._onChange)

    # Some getters and setters
    x = Btn.x
    y = Btn.y
    width = Btn.width
    height = Btn.height
    command = Btn.command
    value = property(lambda self: self.get(1.0, END), lambda self, val: self.setValue(val))
    def setValue(self, val):
        self.delete(1.0, END)
        self.insert(1.0, val)

    # The positioning methods
    def locateInside(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateInside(self, c, h, v, d)

    def locateFrom(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateFrom(self, c, h, v, d)

    def addLabel(self, text, d=10, moveCtrl=True, labelWidth=0):
        Btn.addLabel(self, text, d, moveCtrl, labelWidth)

    # Stuff for the onchange event
    def _resetModified(self):
        self._resettingModified = True
        try:
            self.tk.call(self._w, 'edit', 'modified', 0)
        finally:
            self._resettingModified = False

    def _onChange(self, event=None):
        if self._resettingModified:
            return
        self._resetModified()
        if self.onChange != None:
            self.onChange(event)


#
#   The canvas class
#
class Cnvs(Canvas):
    """Matty's canvas class"""

    # Init method
    def __init__(self, parent, **kwargs):
        """Create a canvas."""
        Canvas.__init__(self, parent, **kwargs)
        if self.place_info().get('width', '') == '':
            self.width = 50
        if self.place_info().get('height', '') == '':
            self.height = 50

    # Some getters and setters
    x = Btn.x
    y = Btn.y
    width = Btn.width
    height = Btn.height
    command = Btn.command

    # The positioning methods
    def locateInside(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateInside(self, c, h, v, d)

    def locateFrom(self, c, h=H_LEFT, v=V_TOP, d=10):
        Btn.locateFrom(self, c, h, v, d)

