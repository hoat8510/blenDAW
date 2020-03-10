import bpy
from nodeitems_utils import NodeCategory, NodeItem

# ============================
# ===== NODE CATEGORIES ======
# ============================
class NodeCategories(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'BlenDAWTreeType'

node_categories = [
    NodeCategories('AUDIONODES', "Audio Node", items=[
        NodeItem("AudioNodeType"),
    ]),

    NodeCategories('MASTERNODES', "VSE Audio Node", items=[
        NodeItem("VSEAudioNodeType"),
    ]),
]
