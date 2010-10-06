#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class IOException(Exception):
  """
  Generic I/O error
  
  Attributes:
   - msg: Error message.
   - stack: Textual representation of the call stack.
   - clazz: The Java class of the Exception (may be a subclass)
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'msg', None, None, ), # 1
    (2, TType.STRING, 'stack', None, None, ), # 2
    (3, TType.STRING, 'clazz', None, None, ), # 3
  )

  def __init__(self, msg=None, stack=None, clazz=None,):
    self.msg = msg
    self.stack = stack
    self.clazz = clazz

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.msg = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.stack = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.clazz = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IOException')
    if self.msg != None:
      oprot.writeFieldBegin('msg', TType.STRING, 1)
      oprot.writeString(self.msg)
      oprot.writeFieldEnd()
    if self.stack != None:
      oprot.writeFieldBegin('stack', TType.STRING, 2)
      oprot.writeString(self.stack)
      oprot.writeFieldEnd()
    if self.clazz != None:
      oprot.writeFieldBegin('clazz', TType.STRING, 3)
      oprot.writeString(self.clazz)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class VersionInfo(object):
  """
  Information about the compilation version of this server
  
  Attributes:
   - version
   - revision
   - compileDate
   - compilingUser
   - url
   - buildVersion
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'version', None, None, ), # 1
    (2, TType.STRING, 'revision', None, None, ), # 2
    None, # 3
    (4, TType.STRING, 'compileDate', None, None, ), # 4
    (5, TType.STRING, 'compilingUser', None, None, ), # 5
    (6, TType.STRING, 'url', None, None, ), # 6
    (7, TType.STRING, 'buildVersion', None, None, ), # 7
  )

  def __init__(self, version=None, revision=None, compileDate=None, compilingUser=None, url=None, buildVersion=None,):
    self.version = version
    self.revision = revision
    self.compileDate = compileDate
    self.compilingUser = compilingUser
    self.url = url
    self.buildVersion = buildVersion

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.version = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.revision = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.compileDate = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.compilingUser = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.url = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.buildVersion = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('VersionInfo')
    if self.version != None:
      oprot.writeFieldBegin('version', TType.STRING, 1)
      oprot.writeString(self.version)
      oprot.writeFieldEnd()
    if self.revision != None:
      oprot.writeFieldBegin('revision', TType.STRING, 2)
      oprot.writeString(self.revision)
      oprot.writeFieldEnd()
    if self.compileDate != None:
      oprot.writeFieldBegin('compileDate', TType.STRING, 4)
      oprot.writeString(self.compileDate)
      oprot.writeFieldEnd()
    if self.compilingUser != None:
      oprot.writeFieldBegin('compilingUser', TType.STRING, 5)
      oprot.writeString(self.compilingUser)
      oprot.writeFieldEnd()
    if self.url != None:
      oprot.writeFieldBegin('url', TType.STRING, 6)
      oprot.writeString(self.url)
      oprot.writeFieldEnd()
    if self.buildVersion != None:
      oprot.writeFieldBegin('buildVersion', TType.STRING, 7)
      oprot.writeString(self.buildVersion)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class StackTraceElement(object):
  """
  A single stack frame in a stack dump
  
  Attributes:
   - className
   - fileName
   - lineNumber
   - methodName
   - isNativeMethod
   - stringRepresentation
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'className', None, None, ), # 1
    (2, TType.STRING, 'fileName', None, None, ), # 2
    (3, TType.I32, 'lineNumber', None, None, ), # 3
    (4, TType.STRING, 'methodName', None, None, ), # 4
    (5, TType.BOOL, 'isNativeMethod', None, None, ), # 5
    (6, TType.STRING, 'stringRepresentation', None, None, ), # 6
  )

  def __init__(self, className=None, fileName=None, lineNumber=None, methodName=None, isNativeMethod=None, stringRepresentation=None,):
    self.className = className
    self.fileName = fileName
    self.lineNumber = lineNumber
    self.methodName = methodName
    self.isNativeMethod = isNativeMethod
    self.stringRepresentation = stringRepresentation

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.className = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.fileName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.lineNumber = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.methodName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.isNativeMethod = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.stringRepresentation = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('StackTraceElement')
    if self.className != None:
      oprot.writeFieldBegin('className', TType.STRING, 1)
      oprot.writeString(self.className)
      oprot.writeFieldEnd()
    if self.fileName != None:
      oprot.writeFieldBegin('fileName', TType.STRING, 2)
      oprot.writeString(self.fileName)
      oprot.writeFieldEnd()
    if self.lineNumber != None:
      oprot.writeFieldBegin('lineNumber', TType.I32, 3)
      oprot.writeI32(self.lineNumber)
      oprot.writeFieldEnd()
    if self.methodName != None:
      oprot.writeFieldBegin('methodName', TType.STRING, 4)
      oprot.writeString(self.methodName)
      oprot.writeFieldEnd()
    if self.isNativeMethod != None:
      oprot.writeFieldBegin('isNativeMethod', TType.BOOL, 5)
      oprot.writeBool(self.isNativeMethod)
      oprot.writeFieldEnd()
    if self.stringRepresentation != None:
      oprot.writeFieldBegin('stringRepresentation', TType.STRING, 6)
      oprot.writeString(self.stringRepresentation)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ThreadStackTrace(object):
  """
  Info about a thread with its corresponding stack trace
  
  Attributes:
   - threadName
   - threadStringRepresentation
   - isDaemon
   - stackTrace
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'threadName', None, None, ), # 1
    (2, TType.STRING, 'threadStringRepresentation', None, None, ), # 2
    (3, TType.BOOL, 'isDaemon', None, None, ), # 3
    (4, TType.LIST, 'stackTrace', (TType.STRUCT,(StackTraceElement, StackTraceElement.thrift_spec)), None, ), # 4
  )

  def __init__(self, threadName=None, threadStringRepresentation=None, isDaemon=None, stackTrace=None,):
    self.threadName = threadName
    self.threadStringRepresentation = threadStringRepresentation
    self.isDaemon = isDaemon
    self.stackTrace = stackTrace

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.threadName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.threadStringRepresentation = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.isDaemon = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.stackTrace = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = StackTraceElement()
            _elem5.read(iprot)
            self.stackTrace.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ThreadStackTrace')
    if self.threadName != None:
      oprot.writeFieldBegin('threadName', TType.STRING, 1)
      oprot.writeString(self.threadName)
      oprot.writeFieldEnd()
    if self.threadStringRepresentation != None:
      oprot.writeFieldBegin('threadStringRepresentation', TType.STRING, 2)
      oprot.writeString(self.threadStringRepresentation)
      oprot.writeFieldEnd()
    if self.isDaemon != None:
      oprot.writeFieldBegin('isDaemon', TType.BOOL, 3)
      oprot.writeBool(self.isDaemon)
      oprot.writeFieldEnd()
    if self.stackTrace != None:
      oprot.writeFieldBegin('stackTrace', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.stackTrace))
      for iter6 in self.stackTrace:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RuntimeInfo(object):
  """
  Memory available via java.lang.Runtime
  
  Attributes:
   - totalMemory
   - freeMemory
   - maxMemory
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'totalMemory', None, None, ), # 1
    (2, TType.I64, 'freeMemory', None, None, ), # 2
    (3, TType.I64, 'maxMemory', None, None, ), # 3
  )

  def __init__(self, totalMemory=None, freeMemory=None, maxMemory=None,):
    self.totalMemory = totalMemory
    self.freeMemory = freeMemory
    self.maxMemory = maxMemory

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.totalMemory = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.freeMemory = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.maxMemory = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RuntimeInfo')
    if self.totalMemory != None:
      oprot.writeFieldBegin('totalMemory', TType.I64, 1)
      oprot.writeI64(self.totalMemory)
      oprot.writeFieldEnd()
    if self.freeMemory != None:
      oprot.writeFieldBegin('freeMemory', TType.I64, 2)
      oprot.writeI64(self.freeMemory)
      oprot.writeFieldEnd()
    if self.maxMemory != None:
      oprot.writeFieldBegin('maxMemory', TType.I64, 3)
      oprot.writeI64(self.maxMemory)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RequestContext(object):
  """
  Context options for every request.
  
  Attributes:
   - confOptions: This map turns into a Configuration object in the server and
  is currently used to construct a UserGroupInformation to
  authenticate this request.
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'confOptions', (TType.STRING,None,TType.STRING,None), None, ), # 1
  )

  def __init__(self, confOptions=None,):
    self.confOptions = confOptions

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.confOptions = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin() 
          for _i11 in xrange(_size7):
            _key12 = iprot.readString();
            _val13 = iprot.readString();
            self.confOptions[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RequestContext')
    if self.confOptions != None:
      oprot.writeFieldBegin('confOptions', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.confOptions))
      for kiter14,viter15 in self.confOptions.items():
        oprot.writeString(kiter14)
        oprot.writeString(viter15)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MetricsRecord(object):
  """
  Attributes:
   - tags
   - metrics
  """

  thrift_spec = (
    None, # 0
    None, # 1
    (2, TType.MAP, 'tags', (TType.STRING,None,TType.STRING,None), None, ), # 2
    (3, TType.MAP, 'metrics', (TType.STRING,None,TType.I64,None), None, ), # 3
  )

  def __init__(self, tags=None, metrics=None,):
    self.tags = tags
    self.metrics = metrics

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 2:
        if ftype == TType.MAP:
          self.tags = {}
          (_ktype17, _vtype18, _size16 ) = iprot.readMapBegin() 
          for _i20 in xrange(_size16):
            _key21 = iprot.readString();
            _val22 = iprot.readString();
            self.tags[_key21] = _val22
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.metrics = {}
          (_ktype24, _vtype25, _size23 ) = iprot.readMapBegin() 
          for _i27 in xrange(_size23):
            _key28 = iprot.readString();
            _val29 = iprot.readI64();
            self.metrics[_key28] = _val29
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MetricsRecord')
    if self.tags != None:
      oprot.writeFieldBegin('tags', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.tags))
      for kiter30,viter31 in self.tags.items():
        oprot.writeString(kiter30)
        oprot.writeString(viter31)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.metrics != None:
      oprot.writeFieldBegin('metrics', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.I64, len(self.metrics))
      for kiter32,viter33 in self.metrics.items():
        oprot.writeString(kiter32)
        oprot.writeI64(viter33)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MetricsContext(object):
  """
  Attributes:
   - name
   - isMonitoring
   - period
   - records
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.BOOL, 'isMonitoring', None, None, ), # 2
    (3, TType.I32, 'period', None, None, ), # 3
    (4, TType.MAP, 'records', (TType.STRING,None,TType.LIST,(TType.STRUCT,(MetricsRecord, MetricsRecord.thrift_spec))), None, ), # 4
  )

  def __init__(self, name=None, isMonitoring=None, period=None, records=None,):
    self.name = name
    self.isMonitoring = isMonitoring
    self.period = period
    self.records = records

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.isMonitoring = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.period = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.records = {}
          (_ktype35, _vtype36, _size34 ) = iprot.readMapBegin() 
          for _i38 in xrange(_size34):
            _key39 = iprot.readString();
            _val40 = []
            (_etype44, _size41) = iprot.readListBegin()
            for _i45 in xrange(_size41):
              _elem46 = MetricsRecord()
              _elem46.read(iprot)
              _val40.append(_elem46)
            iprot.readListEnd()
            self.records[_key39] = _val40
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MetricsContext')
    if self.name != None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.isMonitoring != None:
      oprot.writeFieldBegin('isMonitoring', TType.BOOL, 2)
      oprot.writeBool(self.isMonitoring)
      oprot.writeFieldEnd()
    if self.period != None:
      oprot.writeFieldBegin('period', TType.I32, 3)
      oprot.writeI32(self.period)
      oprot.writeFieldEnd()
    if self.records != None:
      oprot.writeFieldBegin('records', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.records))
      for kiter47,viter48 in self.records.items():
        oprot.writeString(kiter47)
        oprot.writeListBegin(TType.STRUCT, len(viter48))
        for iter49 in viter48:
          iter49.write(oprot)
        oprot.writeListEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ThriftDelegationToken(object):
  """
  Attributes:
   - delegationTokenBytes
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'delegationTokenBytes', None, None, ), # 1
  )

  def __init__(self, delegationTokenBytes=None,):
    self.delegationTokenBytes = delegationTokenBytes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.delegationTokenBytes = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ThriftDelegationToken')
    if self.delegationTokenBytes != None:
      oprot.writeFieldBegin('delegationTokenBytes', TType.STRING, 1)
      oprot.writeString(self.delegationTokenBytes)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

