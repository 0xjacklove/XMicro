# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""
IDA Plugin SDK API wrapper: registry
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_registry
else:
    import _ida_registry

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

SWIG_PYTHON_LEGACY_BOOL = _ida_registry.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


import sys
_BC695 = sys.modules["__main__"].IDAPYTHON_COMPAT_695_API

if _BC695:






    def bc695redef(func):
        ida_idaapi._BC695.replace_fun(func)
        return func


def reg_read_string(*args) -> "PyObject *":
    r"""
    reg_read_string(name, subkey=None, _def=None) -> PyObject *


    Read a string from the registry.
    
    @param name: value name (C++: const char *)
    @param subkey: key name (C++: const char *)
    @return: success
    """
    return _ida_registry.reg_read_string(*args)

def reg_data_type(*args) -> "regval_type_t":
    r"""
    reg_data_type(name, subkey=None) -> regval_type_t


    Get data type of a given value.
    
    @param name: value name (C++: const char *)
    @param subkey: key name (C++: const char *)
    @return: false if the [key+]value doesn't exist
    """
    return _ida_registry.reg_data_type(*args)

def reg_read_binary(*args) -> "PyObject *":
    r"""
    reg_read_binary(name, subkey=None) -> PyObject *


    Read binary data from the registry.
    
    @param name: value name (C++: const char *)
    @param subkey: key name (C++: const char *)
    @return: false if 'data' is not large enough to hold all data present.
             in this case 'data' is left untouched.
    """
    return _ida_registry.reg_read_binary(*args)

def reg_write_binary(*args) -> "PyObject *":
    r"""
    reg_write_binary(name, py_bytes, subkey=None) -> PyObject *


    Write binary data to the registry.
    
    @param name: value name (C++: const char *)
    @param subkey: key name (C++: const char *)
    """
    return _ida_registry.reg_write_binary(*args)

def reg_subkey_subkeys(*args) -> "PyObject *":
    r"""
    reg_subkey_subkeys(name) -> PyObject *


    Get all subkey names of given key.
    
    
    @param name (C++: const char *)
    """
    return _ida_registry.reg_subkey_subkeys(*args)

def reg_subkey_values(*args) -> "PyObject *":
    r"""
    reg_subkey_values(name) -> PyObject *


    Get all value names under given key.
    
    
    @param name (C++: const char *)
    """
    return _ida_registry.reg_subkey_values(*args)
ROOT_KEY_NAME = _ida_registry.ROOT_KEY_NAME
"""
Key used to store IDA settings in registry (Windows version).this name
is automatically prepended to all key names passed to functions in
this file.
"""

reg_unknown = _ida_registry.reg_unknown

reg_sz = _ida_registry.reg_sz

reg_binary = _ida_registry.reg_binary

reg_dword = _ida_registry.reg_dword


def reg_delete_subkey(*args) -> "bool":
    r"""
    reg_delete_subkey(name) -> bool


    Delete a key from the registry.
    
    
    @param name (C++: const char *)
    """
    return _ida_registry.reg_delete_subkey(*args)

def reg_delete_tree(*args) -> "bool":
    r"""
    reg_delete_tree(name) -> bool


    Delete a subtree from the registry.
    
    
    @param name (C++: const char *)
    """
    return _ida_registry.reg_delete_tree(*args)

def reg_delete(*args) -> "bool":
    r"""
    reg_delete(name, subkey=None) -> bool


    Delete a value from the registry.
    
    @param name: value name (C++: const char *)
    @param subkey: parent key (C++: const char *)
    @return: success
    """
    return _ida_registry.reg_delete(*args)

def reg_subkey_exists(*args) -> "bool":
    r"""
    reg_subkey_exists(name) -> bool


    Is there already a key with the given name?
    
    
    @param name (C++: const char *)
    """
    return _ida_registry.reg_subkey_exists(*args)

def reg_exists(*args) -> "bool":
    r"""
    reg_exists(name, subkey=None) -> bool


    Is there already a value with the given name?
    
    @param name: value name (C++: const char *)
    @param subkey: parent key (C++: const char *)
    """
    return _ida_registry.reg_exists(*args)

def reg_read_strlist(*args) -> "qstrvec_t *":
    r"""
    reg_read_strlist(subkey)


    Retrieve all string values associated with the given key. Also see
    'reg_update_strlist()' .
    
    @param subkey (C++: const char *)
    """
    return _ida_registry.reg_read_strlist(*args)

def reg_update_strlist(*args) -> "void":
    r"""
    reg_update_strlist(subkey, add, maxrecs, rem=None, ignorecase=False)


    Update list of strings associated with given key.
    
    @param subkey: key name (C++: const char *)
    @param add: string to be added to list, can be NULL (C++: const char
                *)
    @param maxrecs: limit list to this size (C++: size_t)
    @param rem: string to be removed from list, can be NULL (C++: const
                char *)
    @param ignorecase: ignore case for 'add' and 'rem' (C++: bool)
    """
    return _ida_registry.reg_update_strlist(*args)

def reg_write_string(*args) -> "void":
    r"""
    reg_write_string(name, utf8, subkey=None)


    Write a string to the registry.
    
    @param name: value name (C++: const char *)
    @param utf8: utf8-encoded string (C++: const char *)
    @param subkey: key name (C++: const char *)
    """
    return _ida_registry.reg_write_string(*args)

def reg_read_int(*args) -> "int":
    r"""
    reg_read_int(name, defval, subkey=None) -> int


    Read integer value from the registry.
    
    @param name: value name (C++: const char *)
    @param defval: default value (C++: int)
    @param subkey: key name (C++: const char *)
    @return: the value read from the registry, or 'defval' if the read
             failed
    """
    return _ida_registry.reg_read_int(*args)

def reg_write_int(*args) -> "void":
    r"""
    reg_write_int(name, value, subkey=None)


    Write integer value to the registry.
    
    @param name: value name (C++: const char *)
    @param value: value to write (C++: int)
    @param subkey: key name (C++: const char *)
    """
    return _ida_registry.reg_write_int(*args)

def reg_read_bool(*args) -> "bool":
    r"""
    reg_read_bool(name, defval, subkey=None) -> bool


    Read boolean value from the registry.
    
    @param name: value name (C++: const char *)
    @param defval: default value (C++: bool)
    @param subkey: key name (C++: const char *)
    @return: boolean read from registry, or 'defval' if the read failed
    """
    return _ida_registry.reg_read_bool(*args)

def reg_write_bool(*args) -> "void":
    r"""
    reg_write_bool(name, value, subkey=None)


    Write boolean value to the registry.
    
    @param name: value name (C++: const char *)
    @param value: boolean to write (nonzero = true) (C++: int)
    @param subkey: key name (C++: const char *)
    """
    return _ida_registry.reg_write_bool(*args)

def reg_update_filestrlist(*args) -> "void":
    r"""
    reg_update_filestrlist(subkey, add, maxrecs, rem=None)


    Update registry with a file list. Case sensitivity will vary depending
    on the target OS.'add' and 'rem' must be UTF-8, just like for regular
    string operations.
    
    @param subkey (C++: const char *)
    @param add (C++: const char *)
    @param maxrecs (C++: size_t)
    @param rem (C++: const char *)
    """
    return _ida_registry.reg_update_filestrlist(*args)

def reg_load(*args) -> "void":
    r"""
    reg_load()
    """
    return _ida_registry.reg_load(*args)

def reg_flush(*args) -> "void":
    r"""
    reg_flush()
    """
    return _ida_registry.reg_flush(*args)

