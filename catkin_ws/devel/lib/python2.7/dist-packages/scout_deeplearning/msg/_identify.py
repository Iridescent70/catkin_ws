# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from scout_deeplearning/identify.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class identify(genpy.Message):
  _md5sum = "f6053d8d260d6714b1da39ebe6fbf86b"
  _type = "scout_deeplearning/identify"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string results
int8 classes
int32 area
float32[4] position
float32 acc
int32 image_number
"""
  __slots__ = ['results','classes','area','position','acc','image_number']
  _slot_types = ['string','int8','int32','float32[4]','float32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       results,classes,area,position,acc,image_number

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(identify, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.results is None:
        self.results = ''
      if self.classes is None:
        self.classes = 0
      if self.area is None:
        self.area = 0
      if self.position is None:
        self.position = [0.] * 4
      if self.acc is None:
        self.acc = 0.
      if self.image_number is None:
        self.image_number = 0
    else:
      self.results = ''
      self.classes = 0
      self.area = 0
      self.position = [0.] * 4
      self.acc = 0.
      self.image_number = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.results
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_bi().pack(_x.classes, _x.area))
      buff.write(_get_struct_4f().pack(*self.position))
      _x = self
      buff.write(_get_struct_fi().pack(_x.acc, _x.image_number))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.results = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.results = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.classes, _x.area,) = _get_struct_bi().unpack(str[start:end])
      start = end
      end += 16
      self.position = _get_struct_4f().unpack(str[start:end])
      _x = self
      start = end
      end += 8
      (_x.acc, _x.image_number,) = _get_struct_fi().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.results
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_bi().pack(_x.classes, _x.area))
      buff.write(self.position.tostring())
      _x = self
      buff.write(_get_struct_fi().pack(_x.acc, _x.image_number))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.results = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.results = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.classes, _x.area,) = _get_struct_bi().unpack(str[start:end])
      start = end
      end += 16
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      _x = self
      start = end
      end += 8
      (_x.acc, _x.image_number,) = _get_struct_fi().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_bi = None
def _get_struct_bi():
    global _struct_bi
    if _struct_bi is None:
        _struct_bi = struct.Struct("<bi")
    return _struct_bi
_struct_fi = None
def _get_struct_fi():
    global _struct_fi
    if _struct_fi is None:
        _struct_fi = struct.Struct("<fi")
    return _struct_fi
