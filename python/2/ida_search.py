# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: search
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_search
else:
    import _ida_search

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """
    Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass
    """
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """
    Meta class to enforce nondynamic attributes (no new attributes) for a class
    """
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

SWIG_PYTHON_LEGACY_BOOL = _ida_search.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func

SEARCH_UP = _ida_search.SEARCH_UP
"""
search towards lower addresses
"""

SEARCH_DOWN = _ida_search.SEARCH_DOWN
"""
search towards higher addresses
"""

SEARCH_NEXT = _ida_search.SEARCH_NEXT
"""
for other find_.. functions it is implicitly set

useful only for 'search()' and find_binary().
"""

SEARCH_CASE = _ida_search.SEARCH_CASE
"""
case-sensitive search (case-insensitive otherwise)
"""

SEARCH_REGEX = _ida_search.SEARCH_REGEX
"""
regular expressions in search string (only supported for txt search)
"""

SEARCH_NOBRK = _ida_search.SEARCH_NOBRK
"""
don't test for ctrl-break to interrupt the search
"""

SEARCH_NOSHOW = _ida_search.SEARCH_NOSHOW
"""
don't display the search progress/refresh screen
"""

SEARCH_IDENT = _ida_search.SEARCH_IDENT
"""
search for an identifier (text search). it means that the characters
before and after the match cannot be is_visible_char().
"""

SEARCH_BRK = _ida_search.SEARCH_BRK
"""
return 'BADADDR' if Ctrl-Break wass pressed during search
"""


def search_down(*args):
    r"""
    search_down(sflag) -> bool


    Is the 'SEARCH_DOWN' bit set?
    
    
    @param sflag (C++: int)
    """
    return _ida_search.search_down(*args)

def find_error(*args):
    r"""
    find_error(ea, sflag) -> ea_t


    Find next error or problem.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_error(*args)

def find_notype(*args):
    r"""
    find_notype(ea, sflag) -> ea_t


    Find next operand without any type info.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_notype(*args)

def find_unknown(*args):
    r"""
    find_unknown(ea, sflag) -> ea_t


    Find next unexplored address.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_unknown(*args)

def find_defined(*args):
    r"""
    find_defined(ea, sflag) -> ea_t


    Find next ea that is the start of an instruction or data.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_defined(*args)

def find_suspop(*args):
    r"""
    find_suspop(ea, sflag) -> ea_t


    Find next suspicious operand.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_suspop(*args)

def find_data(*args):
    r"""
    find_data(ea, sflag) -> ea_t


    Find next data address.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_data(*args)

def find_code(*args):
    r"""
    find_code(ea, sflag) -> ea_t


    Find next code address.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_code(*args)

def find_not_func(*args):
    r"""
    find_not_func(ea, sflag) -> ea_t


    Find next code address that does not belong to a function.
    
    
    @param ea (C++: ea_t)
    @param sflag (C++: int)
    """
    return _ida_search.find_not_func(*args)

def find_imm(*args):
    r"""
    find_imm(newEA, sflag, srchValue) -> ea_t


    Find next immediate operand with the given value.
    
    
    @param newEA (C++: ea_t)
    @param sflag (C++: int)
    @param srchValue (C++: uval_t)
    """
    return _ida_search.find_imm(*args)

def find_text(*args):
    r"""
    find_text(start_ea, y, x, ustr, sflag) -> ea_t


    See 'search()'
    
    
    @param start_ea (C++: ea_t)
    @param y (C++: int)
    @param x (C++: int)
    @param ustr (C++: const char *)
    @param sflag (C++: int)
    """
    return _ida_search.find_text(*args)

def find_binary(*args):
    r"""
    find_binary(arg1, arg2, arg3, arg4, arg5) -> ea_t
    """
    return _ida_search.find_binary(*args)

if _BC695:
    find_void=find_suspop



