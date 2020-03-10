import bpy
import nodeitems_utils
import os

# Information of the add-on
bl_info = {
    'name': 'BlenDAW',
    'category': 'All',
    'author': 'Michael',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Audio node to incorporate software audio tools and import them on the VSE'
}

# Global variables
blender_path = os.getcwd()
audio_path = blender_path + '/audio/'
process = None
prefereed_path = ''
samplerate_wav = 0
sampleformat_wav = 0
channel_wav = ''
duration_wav = 0

#==============================================
from . import sockets as bds
from . import external as bde
from . import prefs as bdp
from . import nodes as bdn
from . import nodecat as bdc
#==============================================

# =============================
# == EVERY CLASS TO REGISTER ==
# =============================
classes = [
    bdp.GeneralPreferences,
    bdn.DAWTreeNode,
    bds.AudioNodeSocket,
    bds.VSEAudioNodeSocket,
    bdn.AudioCustomNode,
    bdn.VSEAudioCustomNode,
    bde.OpenSoftwareOperator,
    bde.UpdateVSEAudioOperator,
]

# =============================
# ===== REGISTER FUNCTION =====
# =============================
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('CUSTOM_NODES', bdc.node_categories)


# =============================
# === UNREGISTER FUNCTION =====
# =============================
def unregister():
    nodeitems_utils.unregister_node_categories('CUSTOM_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
