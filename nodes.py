import bpy
from bpy.types import NodeTree, Node

# ============================
#  BLEN-DAW GENERAL TREE NODE
# ============================
class DAWTreeNode(NodeTree):
    bl_idname = 'BlenDAWTreeType'
    bl_label = "Blen-DAW Node Tree"
    bl_icon = 'NODETREE'

# ============================
# == BLEN-DAW TREE NODE POLL =
# ============================
class DAWTreeNodePoll:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'BlenDAWTreeType'

# ============================
# == AUDIO CUSTOM NODE ==
# ============================
class AudioCustomNode(Node, DAWTreeNode):
    bl_idname = 'AudioNodeType'
    bl_label = "Audio Node"
    bl_icon = 'SOUND'

    def init(self, context):
        self.outputs.new('AudioSocketType', "")

    def draw_label(self):
        return "Audio Node"

# ============================
# == VSE AUDIO CUSTOM NODE ==
# ============================
class VSEAudioCustomNode(Node, DAWTreeNode):
    bl_idname = 'VSEAudioNodeType'
    bl_label = "VSE Audio Channel"
    bl_icon = 'SOUND'

    def init(self, context):
        self.inputs.new('VSEAudioSocketType', "")

    def draw_label(self):
        return "VSE Audio Channel"
