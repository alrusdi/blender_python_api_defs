'''Bmesh
   
'''


def BoolProperty(name="", description="", default=False, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
   '''Returns a new boolean property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL'].
      @subtype (string): Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def EnumProperty(items, name="", description="", default="", options={'ANIMATABLE'}, update=None, get=None, set=None):
   '''Returns a new enumerator property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @default (string or set): The default value for this enum, a string from the identifiers used in *items*.If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead.
      
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'ENUM_FLAG', 'LIBRARY_EDITABLE'].
      @items (sequence of string tuples or a function): sequence of enum items formatted:[(identifier, name, description, icon, number), ...] where the identifier is used
      for python access and other values are used for the interface.
      The three first elements of the tuples are mandatory.
      The forth one is either the (unique!) number id of the item or, if followed by a fith element 
      (which must be the numid), an icon string identifier.
      Note the item is optional.
      For dynamic values a callback can be passed which returns a list in
      the same format as the static list.
      This function must take 2 arguments (self, context)
      WARNING: There is a known bug with using a callback,
      Python must keep a reference to the strings returned or Blender will crash.
      
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def StringProperty(name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None):
   '''Returns a new string property definition.
      
      Arguments:
      @name (string): Name used in the user interface.
      @description (string): Text used for the tooltip and api documentation.
      @default (string): initializer string.
      @options (set): Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL'].
      @subtype (string): Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'NONE'].
      @update (function): function to be called when this value is modified,This function must take 2 values (self, context) and return None.
      *Warning* there are no safety checks to avoid infinite recursion.
      

   '''

   pass

def axis_conversion(from_forward='Y', from_up='Z', to_forward='Y', to_up='Z'):
   '''Each argument us an axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z']
      where the first 2 are a source and the second 2 are the target.
      
   '''

   pass

def axis_conversion_ensure(operator, forward_attr, up_attr):
   '''Function to ensure an operator has valid axis conversion settings, intended
      to be used from bpy.types.Operator.check.
      
      Arguments:
      @operator (bpy.types.Operator): the operator to access axis attributes from.
      @forward_attr (string): attribute storing the forward axis
      @up_attr (string): attribute storing the up axis

      @returns (bool): True if the value was modified.
   '''

   return bool

def create_derived_objects(scene, ob):
   

   pass

def free_derived_objects(ob):
   

   pass

def path_reference(filepath, base_src, base_dst, mode='AUTO', copy_subdir='', copy_set=None, library=None):
   '''Return a filepath relative to a destination directory, for use with
      exporters.
      
      Arguments:
      @filepath (string): the file path to return,supporting blenders relative '//' prefix.
      
      @base_src (string): the directory the *filepath* is relative too(normally the blend file).
      
      @base_dst (string): the directory the *filepath* will be referenced from(normally the export path).
      
      @mode (string): the method used get the path in['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY']
      
      @copy_subdir (string): the subdirectory of *base_dst* to use when mode='COPY'.
      @copy_set (set): collect from/to pairs when mode='COPY',pass to *path_reference_copy* when exporting is done.
      
      @library (bpy.types.Library or None): The library this path is relative to.

      @returns (str): the new filepath.
   '''

   return str

def path_reference_copy(copy_set, report=<built-in function print>):
   '''Execute copying files of path_reference
      
      Arguments:
      @copy_set (set): set of (from, to) pairs to copy.
      @report (function): function used for reporting warnings, takes a string argument.

   '''

   pass

path_reference_mode = (<built-in function EnumProperty>, {'name': 'Path Mode', 'items': (('AUTO', 'Auto', 'Use Relative paths with subdirectories only'), ('ABSOLUTE', 'Absolute', 'Always write absolute paths'), ('RELATIVE', 'Relative', 'Always write relative paths (where possible)'), ('MATCH', 'Match', 'Match Absolute/Relative setting with input path'), ('STRIP', 'Strip Path', 'Filename only'), ('COPY', 'Copy', 'Copy the file to the destination path (or subdirectory)')), 'attr': 'path_mode', 'default': 'AUTO', 'description': 'Method used to reference paths'}) #constant value 

def unique_name(key, name, name_dict, name_max=-1, clean_func=None, sep='.'):
   '''Helper function for storing unique names which may have special characters
      stripped and restricted to a maximum length.
      
      Arguments:
      @key (any hashable object associated with the *name*.): unique item this name belongs to, name_dict[key] will be reusedwhen available.
      This can be the object, mesh, material, etc instance its self.
      
      @name (string): The name used to create a unique value in *name_dict*.
      @name_dict (dict): This is used to cache namespace to ensure no collisionsoccur, this should be an empty dict initially and only modified by this
      function.
      
      @clean_func (function): Function to call on *name* before creating a unique value.
      @sep (string): Separator to use when between the name and a number when aduplicate name is found.
      

   '''

   pass

def unpack_face_list(list_of_tuples):
   

   pass

def unpack_list(list_of_tuples):
   

   pass

class ExportHelper:
   

   def check(self, context):
      
   
      pass
   
   def invoke(self, context, event):
      
   
      pass
   


class ImportHelper:
   

   def check(self, context):
      
   
      pass
   
   def invoke(self, context, event):
      
   
      pass
   


