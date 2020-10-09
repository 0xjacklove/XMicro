# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: diskio
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_diskio
else:
    import _ida_diskio

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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

SWIG_PYTHON_LEGACY_BOOL = _ida_diskio.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func


def idadir(*args) -> "char const *":
    r"""
    idadir(subdir) -> char const *


    Get IDA directory (if subdir==NULL) or the specified subdirectory (see
    'IDA subdirectories' )
    
    @param subdir (C++: const char *)
    """
    return _ida_diskio.idadir(*args)

def getsysfile(*args) -> "char const *":
    r"""
    getsysfile(filename, subdir) -> str


    Search for IDA system file. This function searches for a file in:each
    directory specified by IDAUSR%ida directory [+ subdir] and returns the
    first match.
    
    @param filename (C++: const char *)
    @param subdir (C++: const char *)
    @return: NULL if not found, otherwise a pointer to full file name.
    """
    return _ida_diskio.getsysfile(*args)
CFG_SUBDIR = _ida_diskio.CFG_SUBDIR

IDC_SUBDIR = _ida_diskio.IDC_SUBDIR

IDS_SUBDIR = _ida_diskio.IDS_SUBDIR

IDP_SUBDIR = _ida_diskio.IDP_SUBDIR

LDR_SUBDIR = _ida_diskio.LDR_SUBDIR

SIG_SUBDIR = _ida_diskio.SIG_SUBDIR

TIL_SUBDIR = _ida_diskio.TIL_SUBDIR

PLG_SUBDIR = _ida_diskio.PLG_SUBDIR

THM_SUBDIR = _ida_diskio.THM_SUBDIR


def get_user_idadir(*args) -> "char const *":
    r"""
    get_user_idadir() -> char const *


    Get user ida related directory.
    
    - if $IDAUSR is defined:
        - the first element in $IDAUSR
    - else
        - default user directory ($HOME/.idapro or %APPDATA%Hex-Rays/IDA Pro)
    """
    return _ida_diskio.get_user_idadir(*args)

def get_ida_subdirs(*args) -> "qstrvec_t *":
    r"""
    get_ida_subdirs(subdir, flags=0) -> int


    Get list of directories in which to find a specific IDA resource (see
    'IDA subdirectories' ). The order of the resulting list is as follows:
    
    - [$IDAUSR/subdir (0..N entries)]
    - $IDADIR/subdir
    
    @param subdir: name of the resource to list (C++: const char *)
    @param flags: Subdirectory modification flags  bits (C++: int)
    @return: number of directories appended to 'dirs'
    """
    return _ida_diskio.get_ida_subdirs(*args)
IDA_SUBDIR_IDP = _ida_diskio.IDA_SUBDIR_IDP
"""
append the processor name as a subdirectory
"""

IDA_SUBDIR_IDADIR_FIRST = _ida_diskio.IDA_SUBDIR_IDADIR_FIRST
"""
$IDADIR/subdir will be first, not last
"""

IDA_SUBDIR_ONLY_EXISTING = _ida_diskio.IDA_SUBDIR_ONLY_EXISTING
"""
only existing directories will be present
"""


def get_special_folder(*args) -> "size_t":
    r"""
    get_special_folder(csidl) -> str


    Get a folder location by CSIDL (see 'Common CSIDLs' ). Path should be
    of at least MAX_PATH size
    
    @param csidl (C++: int)
    """
    return _ida_diskio.get_special_folder(*args)
CSIDL_APPDATA = _ida_diskio.CSIDL_APPDATA

CSIDL_LOCAL_APPDATA = _ida_diskio.CSIDL_LOCAL_APPDATA

CSIDL_PROGRAM_FILES = _ida_diskio.CSIDL_PROGRAM_FILES

CSIDL_PROGRAM_FILES_COMMON = _ida_diskio.CSIDL_PROGRAM_FILES_COMMON

CSIDL_PROGRAM_FILESX86 = _ida_diskio.CSIDL_PROGRAM_FILESX86


def fopenWT(*args) -> "FILE *":
    r"""
    fopenWT(file) -> FILE *


    Open a new file for write in text mode, deny write. If a file exists,
    it will be removed.
    
    @param file (C++: const char *)
    @return: NULL if failure
    """
    return _ida_diskio.fopenWT(*args)

def fopenWB(*args) -> "FILE *":
    r"""
    fopenWB(file) -> FILE *


    Open a new file for write in binary mode, deny read/write. If a file
    exists, it will be removed.
    
    @param file (C++: const char *)
    @return: NULL if failure
    """
    return _ida_diskio.fopenWB(*args)

def fopenRT(*args) -> "FILE *":
    r"""
    fopenRT(file) -> FILE *


    Open a file for read in text mode, deny none.
    
    @param file (C++: const char *)
    @return: NULL if failure
    """
    return _ida_diskio.fopenRT(*args)

def fopenRB(*args) -> "FILE *":
    r"""
    fopenRB(file) -> FILE *


    Open a file for read in binary mode, deny none.
    
    @param file (C++: const char *)
    @return: NULL if failure
    """
    return _ida_diskio.fopenRB(*args)

def fopenM(*args) -> "FILE *":
    r"""
    fopenM(file) -> FILE *


    Open a file for read/write in binary mode, deny write.
    
    @param file (C++: const char *)
    @return: NULL if failure
    """
    return _ida_diskio.fopenM(*args)

def fopenA(*args) -> "FILE *":
    r"""
    fopenA(file) -> FILE *


    Open a file for append in text mode, deny none.
    
    @param file (C++: const char *)
    @return: NULL if failure
    """
    return _ida_diskio.fopenA(*args)
LINPUT_NONE = _ida_diskio.LINPUT_NONE

LINPUT_LOCAL = _ida_diskio.LINPUT_LOCAL

LINPUT_RFILE = _ida_diskio.LINPUT_RFILE

LINPUT_PROCMEM = _ida_diskio.LINPUT_PROCMEM

LINPUT_GENERIC = _ida_diskio.LINPUT_GENERIC


def qlgetz(*args) -> "size_t":
    r"""
    qlgetz(li, fpos) -> str


    Read a zero-terminated string from the input. If fpos == -1 then no
    seek will be performed.
    
    @param li (C++: linput_t *)
    @param fpos (C++: int64)
    """
    return _ida_diskio.qlgetz(*args)

def open_linput(*args) -> "linput_t *":
    r"""
    open_linput(file, remote) -> linput_t *


    Open loader input.
    
    
    @param file (C++: const char *)
    @param remote (C++: bool)
    """
    return _ida_diskio.open_linput(*args)
class generic_linput_t(object):
    r"""
    Proxy of C++ generic_linput_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    filesize = property(_ida_diskio.generic_linput_t_filesize_get, _ida_diskio.generic_linput_t_filesize_set)
    blocksize = property(_ida_diskio.generic_linput_t_blocksize_get, _ida_diskio.generic_linput_t_blocksize_set)

    def read(self, *args) -> "ssize_t":
        r"""
        read(self, off, buffer, nbytes) -> ssize_t
        """
        return _ida_diskio.generic_linput_t_read(self, *args)
    __swig_destroy__ = _ida_diskio.delete_generic_linput_t

# Register generic_linput_t in _ida_diskio:
_ida_diskio.generic_linput_t_swigregister(generic_linput_t)


def create_generic_linput(*args) -> "linput_t *":
    r"""
    create_generic_linput(gl) -> linput_t *


    Create a generic linput
    
    @param gl: linput description. this object will be destroyed by
               close_linput()  using "delete gl;" (C++: generic_linput_t
               *)
    """
    return _ida_diskio.create_generic_linput(*args)

def create_memory_linput(*args) -> "linput_t *":
    r"""
    create_memory_linput(start, size) -> linput_t *


    Create a linput for process memory. This linput will use
    read_dbg_memory() to read data.
    
    @param start: starting address of the input (C++: ea_t)
    @param size: size of the memory area to represent as linput if
                 unknown, may be passed as 0 (C++: asize_t)
    """
    return _ida_diskio.create_memory_linput(*args)

def get_linput_type(*args) -> "linput_type_t":
    r"""
    get_linput_type(li) -> linput_type_t


    Get linput type.
    
    
    @param li (C++: linput_t *)
    """
    return _ida_diskio.get_linput_type(*args)

def eclose(*args) -> "void":
    r"""
    eclose(fp)
    """
    return _ida_diskio.eclose(*args)

def enumerate_files(*args) -> "PyObject *":
    r"""
    enumerate_files(path, fname, callback) -> PyObject *


    Enumerate files in the specified directory while the callback returns 0.
    @param path: directory to enumerate files in
    @param fname: mask of file names to enumerate
    @param callback: a callable object that takes the filename as
                     its first argument and it returns 0 to continue
                     enumeration or non-zero to stop enumeration.
    @return:
        None in case of script errors
        tuple(code, fname) : If the callback returns non-zero
    """
    return _ida_diskio.enumerate_files(*args)

def create_bytearray_linput(*args) -> "linput_t *":
    r"""
    create_bytearray_linput(s) -> linput_t *


    Trivial memory linput.
    """
    return _ida_diskio.create_bytearray_linput(*args)

def close_linput(*args) -> "void":
    r"""
    close_linput(li)


    Close loader input.
    
    
    @param li (C++: linput_t *)
    """
    return _ida_diskio.close_linput(*args)

#<pycode(py_diskio)>
#</pycode(py_diskio)>


if _BC695:
    create_generic_linput64=create_generic_linput
    generic_linput64_t=generic_linput_t



