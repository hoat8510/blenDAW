import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty

# ============================
# == GENERAL PREFERENCES GUI =
# ============================
class GeneralPreferences(AddonPreferences):
    bl_idname = __name__
    path_preferences: StringProperty()

    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'path_preferences')
