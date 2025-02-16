from kokoro import KPipeline
import soundfile as sf
import numpy as np
import torch
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

SPEAKER_LANG_MAPPING = {
    "a": ["af_alloy", "af_aoede", "af_bella", "af_heart", "af_jessica", 
             "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", 
             "af_sky", "am_adam", "am_echo", "am_eric", "am_fenrir", 
             "am_liam", "am_michael", "am_onyx", "am_puck", "am_santa"],
    "b": ["bf_alice", "bf_emma", "bf_isabella", "bf_lily", "bm_daniel",
             "bm_fable", "bm_george", "bm_lewis"],
    "j": ["jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro", "jm_kumo"],
    "z": ["zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi",
           "zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang"]
}

all_speakers = []
for speakers in SPEAKER_LANG_MAPPING.values():
    all_speakers.extend(speakers)

node_dir = os.path.dirname(os.path.abspath(__file__))
comfy_path = os.path.dirname(os.path.dirname(node_dir))
voices_path = os.path.join(comfy_path, "models", "Kokorotts", "voices")
voices = [p.name for p in Path(voices_path).iterdir() if p.is_file()]

class KokoroRun:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voice": (voices, {"default": "zm_yunyang.pt"}),
                "text": ("STRING", {
                    "multiline": True, 
                    "default": "你好啊! 世界."
                })
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "generate"
    CATEGORY = "MW-KokoroTTS"

    def _get_lang(self, voice):
        speaker = voice.removesuffix(".pt")
        if speaker in all_speakers:
            for k, v in SPEAKER_LANG_MAPPING.items():
                if speaker in v:
                    return k
        else:
            raise ValueError("This is a unsupported voice")

    def generate(self, text, voice):
        lang = self._get_lang(voice)
        pipeline = KPipeline(lang_code=lang)
        voice_tensor = torch.load(Path(voices_path, voice), weights_only=True)

        try:
            generator = pipeline(text, voice=voice_tensor, speed=1, split_pattern=r"\n+")
            audio_data = []
            for i, (gs, ps, data) in enumerate(generator):
                audio_data.append(data)
            audio_tensor = torch.from_numpy(np.concatenate(audio_data, axis=0)).unsqueeze(0).unsqueeze(0).float()
            logger.info(f"Generated audio with shape: {audio_tensor.shape}")
            return ({"waveform": audio_tensor, "sample_rate": 24000},)
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            return (None,)

NODE_CLASS_MAPPINGS = {
    "Kokoro Run": KokoroRun,
}