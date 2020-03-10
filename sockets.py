import bpy
from bpy.types import NodeSocket
from bpy.props import EnumProperty, IntProperty

def get_items(scene, context):
    # path = bpy.context.preferences.addons['node_tree'].preferences.path_preferences
    path = '/opt'
    app_tuple = ()
    temp_tuple = ()
    files = [f for f in listdir(path) if isfile(join(path, f))]

    for i in files:
        temp_tuple = (i, i, i)
        app_tuple += (temp_tuple,)

    return app_tuple

# ============================
# === AUDIO NODE SOCKET ======
# ============================
class AudioNodeSocket(NodeSocket):
    bl_idname = 'AudioSocketType'
    bl_label = "Audio Node Socket"

    my_enum_prop: EnumProperty(name="Path", description="", items=get_items)

    def draw(self, context, layout, node, text):
        scene = context.scene
        row = layout.row(align=True)
        col = row.column()
        col.prop(self, 'my_enum_prop')
        col.operator("wm.open_software")

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


# ============================
# = VSE AUDIO NODE SOCKET ====
# ============================
class VSEAudioNodeSocket(NodeSocket):
    bl_idname = 'VSEAudioSocketType'
    bl_label = "VSE Audio Node Socket"

    samplerate_prop: EnumProperty(
        name="Sample Rate",
        description="",
        items=(
            ("48000", "48kHz", "48khz"),
            ("96000", "96kHz", "96kHz"),
        )
    )

    sampleformat_prop: EnumProperty(
        name="Sample Format",
        description="",
        items=(
            ('1', '8 Bit', '16bit'),
            ('2', '16 Bit', '16bit'),
            ('3', '24 Bit', '24bit'),
            ('4', '32 Bit Float', '32bitf'),
        )
    )

    channel_prop: EnumProperty(
        name="Channel",
        description="",
        items=(
            ('STEREO', 'Stereo', 'stereo'),
            ('MONO', 'Mono', 'mono'),
        )
    )

    duration_prop: IntProperty(
        name="Duration"
    )

    def draw(self, context, layout, node, text):
        global samplerate_wav, sampleformat_wav, channel_wav, duration_wav

        scene = context.scene
        row = layout.row(align=True)
        col = row.column()
        col.prop(self, 'channel_prop')
        col.prop(self, 'samplerate_prop')
        col.prop(self, 'sampleformat_prop')
        col.prop(self, 'duration_prop')
        col.operator("wm.update_vseaudio")

        samplerate_wav = int(self.samplerate_prop)
        sampleformat_wav = int(self.sampleformat_prop)
        channel_wav = self.channel_prop
        duration_wav = int(self.duration_prop)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)
