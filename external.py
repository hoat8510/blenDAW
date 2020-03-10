import bpy
from bpy.types import Operator

# ============================
# == OPERATOR OPEN SOFTWARE ==
# ============================
class OpenSoftwareOperator(Operator):
    bl_idname = "wm.open_software"
    bl_label = "Open"

    def execute(self, context):
        process = subprocess.Popen([bpy.context.preferences.addons['node_tree'].preferences.path_preferences])
        return {'FINISHED'}

# ============================
#  UPDATE VSE AUDIO OPERATOR
# ============================
class UpdateVSEAudioOperator(Operator):
    bl_idname = "wm.update_vseaudio"
    bl_label = "Update"

    def execute(self, context):
        global samplerate_wav, sampleformat_wav, channel_wav, duration_wav

        blendaw_index = len([f for f in listdir(audio_path) if isfile(join(audio_path, f))])
        file_name = 'blendaw_{}.wav'.format(blendaw_index)

        data_size = duration_wav * samplerate_wav
        data = [(0, 0) for x in range(data_size)]

        channel = -1
        if channel_wav == 'MONO': channel = 1
        elif channel_wav == 'STEREO': channel = 2

        wave_file = wave.open(audio_path + file_name, 'w')
        wave_file.setparams((channel, sampleformat_wav, samplerate_wav, data_size, 'NONE', 'not compressed'))
        for values in data:
            for i in values:
                wave_file.writeframes(struct.pack('h', int(i)))
        wave_file.close()
        return {'FINISHED'}
