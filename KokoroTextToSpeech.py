from kokoro import KPipeline, KModel
import soundfile as sf
import numpy as np
import torch
import logging
import os
from pathlib import Path
import folder_paths


logger = logging.getLogger(__name__)

SPEAKER_LANG_MAPPING = {
    "a": [
        "af_alloy.pt",
        "af_aoede.pt",
        "af_bella.pt",
        "af_heart.pt",
        "af_jessica.pt",
        "af_kore.pt",
        "af_nicole.pt",
        "af_nova.pt",
        "af_river.pt",
        "af_sarah.pt",
        "af_sky.pt",
        "am_adam.pt",
        "am_echo.pt",
        "am_eric.pt",
        "am_fenrir.pt",
        "am_liam.pt",
        "am_michael.pt",
        "am_onyx.pt",
        "am_puck.pt",
        "am_santa.pt"
    ],
    "b": [
        "bf_alice.pt",
        "bf_emma.pt",
        "bf_isabella.pt",
        "bf_lily.pt",
        "bm_daniel.pt",
        "bm_fable.pt",
        "bm_george.pt",
        "bm_lewis.pt"
    ],
    "e": [
        "ef_dora.pt",
        "em_alex.pt",
        "em_santa.pt"
    ],
    "f": [
        "ff_siwis.pt"
    ],
    "h": [
        "hf_alpha.pt",
        "hf_beta.pt",
        "hm_omega.pt",
        "hm_psi.pt"
    ],
    "i": [
        "if_sara.pt",
        "im_nicola.pt"
    ],
    "j": [
        "jf_alpha.pt",
        "jf_gongitsune.pt",
        "jf_nezumi.pt",
        "jf_tebukuro.pt",
        "jm_kumo.pt"
    ],
    "p": [
        "pf_dora.pt",
        "pm_alex.pt",
        "pm_santa.pt"
    ],
    "z": [
        "zf_xiaobei.pt",
        "zf_xiaoni.pt",
        "zf_xiaoxiao.pt",
        "zf_xiaoyi.pt",
        "zm_yunjian.pt",
        "zm_yunxi.pt",
        "zm_yunxia.pt",
        "zm_yunyang.pt"
    ]
}

all_speakers = []
for speakers in SPEAKER_LANG_MAPPING.values():
    all_speakers.extend(speakers)

zh_all_speakers = ['zf_001.pt', 'zf_002.pt', 'zf_003.pt', 'zf_004.pt', 'zf_005.pt', 'zf_006.pt', 'zf_007.pt', 'zf_008.pt', 
                   'zf_017.pt', 'zf_018.pt', 'zf_019.pt', 'zf_021.pt', 'zf_022.pt', 'zf_023.pt', 'zf_024.pt', 'zf_026.pt', 
                   'zf_027.pt', 'zf_028.pt', 'zf_032.pt', 'zf_036.pt', 'zf_038.pt', 'zf_039.pt', 'zf_040.pt', 'zf_042.pt', 
                   'zf_043.pt', 'zf_044.pt', 'zf_046.pt', 'zf_047.pt', 'zf_048.pt', 'zf_049.pt', 'zf_051.pt', 'zf_059.pt', 
                   'zf_060.pt', 'zf_067.pt', 'zf_070.pt', 'zf_071.pt', 'zf_072.pt', 'zf_073.pt', 'zf_074.pt', 'zf_075.pt', 
                   'zf_076.pt', 'zf_077.pt', 'zf_078.pt', 'zf_079.pt', 'zf_083.pt', 'zf_084.pt', 'zf_085.pt', 'zf_086.pt', 
                   'zf_087.pt', 'zf_088.pt', 'zf_090.pt', 'zf_092.pt', 'zf_093.pt', 'zf_094.pt', 'zf_099.pt', 'zm_009.pt', 
                   'zm_010.pt', 'zm_011.pt', 'zm_012.pt', 'zm_013.pt', 'zm_014.pt', 'zm_015.pt', 'zm_016.pt', 'zm_020.pt', 
                   'zm_025.pt', 'zm_029.pt', 'zm_030.pt', 'zm_031.pt', 'zm_033.pt', 'zm_034.pt', 'zm_035.pt', 'zm_037.pt', 
                   'zm_041.pt', 'zm_045.pt', 'zm_050.pt', 'zm_052.pt', 'zm_053.pt', 'zm_054.pt', 'zm_055.pt', 'zm_056.pt', 
                   'zm_057.pt', 'zm_058.pt', 'zm_061.pt', 'zm_062.pt', 'zm_063.pt', 'zm_064.pt', 'zm_065.pt', 'zm_066.pt', 
                   'zm_068.pt', 'zm_069.pt', 'zm_080.pt', 'zm_081.pt', 'zm_082.pt', 'zm_089.pt', 'zm_091.pt', 'zm_095.pt', 
                   'zm_096.pt', 'zm_097.pt', 'zm_098.pt', 'zm_100.pt']

models_dir =  folder_paths.models_dir

kokoro_path = os.path.join(models_dir, "Kokorotts", "Kokoro-82M")
kk_config_path = os.path.join(kokoro_path, "config.json")
kk_model_path = os.path.join(kokoro_path, "kokoro-v1_0.pth")
voices_path = os.path.join(kokoro_path, "voices")

zh_kokoro_path = os.path.join(models_dir, "Kokorotts", "Kokoro-82M-v1.1-zh")
zh_kk_config_path = os.path.join(zh_kokoro_path, "config.json")
zh_kk_model_path = os.path.join(zh_kokoro_path, "kokoro-v1_1-zh.pth")
zh_voices_path = os.path.join(zh_kokoro_path, "voices")

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class KokoroRun:
    def __init__(self):
        self.model_cache = None
        self.voice_tensor = None
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voice": (all_speakers, {"default": "zm_yunyang.pt"}),
                "text": ("STRING", {"forceInput": True}),
                "unload_model": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "generate"
    CATEGORY = "🎤MW/MW-KokoroTTS"

    def _get_lang(self, voice):
        if voice in all_speakers:
            for k, v in SPEAKER_LANG_MAPPING.items():
                if voice in v:
                    return k
        else:
            raise ValueError("This is a unsupported voice")

    def generate(self, text, voice, unload_model):

        if self.model_cache is None:      
            self.model_cache = KModel(
                        config = kk_config_path,
                        model = kk_model_path).to(device).eval()

        lang = self._get_lang(voice)
        pipeline = KPipeline(lang_code=lang, repo_id=None, model=self.model_cache)
        self.voice_tensor = torch.load(Path(voices_path, voice), weights_only=True)

        try:
            generator = pipeline(text, voice=self.voice_tensor, speed=1, split_pattern=r"\n+")
            audio_data = []
            for i, (gs, ps, data) in enumerate(generator):
                audio_data.append(data)
            audio_tensor = torch.from_numpy(np.concatenate(audio_data, axis=0)).unsqueeze(0).unsqueeze(0).float()
            logger.info(f"Generated audio with shape: {audio_tensor.shape}")

            if unload_model:
                self.model_cache = None
                self.voice_tensor = None
                torch.cuda.empty_cache()

            return ({"waveform": audio_tensor, "sample_rate": 24000},)
        
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")

            if unload_model:
                self.model_cache = None
                self.voice_tensor = None
                torch.cuda.empty_cache()
            raise


class KokoroZHRun:
    def __init__(self):
        self.model_cache = None
        self.en_model_cache = None
        self.voice_tensor = None

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voice": (zh_all_speakers, {"default": "zf_001.pt"}),
                "text": ("STRING", {"forceInput": True}),
                "unload_model": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)
    FUNCTION = "generate"
    CATEGORY = "🎤MW/MW-KokoroTTS"
    def generate(self, text, voice, unload_model):
        REPO_ID = 'hexgrad/Kokoro-82M-v1.1-zh'
        if self.model_cache is None:
            self.model_cache = KModel(
                        repo_id=REPO_ID,
                        config = zh_kk_config_path,
                        model = zh_kk_model_path).to(device).eval()

            self.en_model_cache = KPipeline(lang_code='a',
                                repo_id=REPO_ID, 
                                model=False)
        
        def en_callable(text):
            if text == 'Kokoro':
                return 'kˈOkəɹO'
            elif text == 'Sol':
                return 'sˈOl'
            return next(self.en_model_cache(text)).phonemes
        
        zh_pipeline = KPipeline(lang_code="z", 
                        repo_id=REPO_ID, 
                        model=self.model_cache, 
                        en_callable=en_callable)
        self.voice_tensor = torch.load(Path(zh_voices_path, voice), weights_only=True)
        
        def speed_callable(len_ps):
            speed = 0.8
            if len_ps <= 83:
                speed = 1
            elif len_ps < 183:
                speed = 1 - (len_ps - 83) / 500
            return speed * 1.1
        
        try:
            generator = zh_pipeline(text, voice=self.voice_tensor, speed=speed_callable, split_pattern=r"\n+")
            audio_data = []
            for i, (gs, ps, data) in enumerate(generator):
                audio_data.append(data)
                audio_data.append(np.zeros(5000))

            audio_tensor = torch.from_numpy(np.concatenate(audio_data, axis=0)).unsqueeze(0).unsqueeze(0).float()
            logger.info(f"Generated audio with shape: {audio_tensor.shape}")

            if unload_model:
                self.model_cache = None
                self.en_model_cache = None
                self.voice_tensor = None
                torch.cuda.empty_cache()
                
            return ({"waveform": audio_tensor, "sample_rate": 24000},)
        
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            if unload_model:
                self.model_cache = None
                self.en_model_cache = None
                self.voice_tensor = None
                torch.cuda.empty_cache()
            raise


NODE_CLASS_MAPPINGS = {
    "Kokoro Run": KokoroRun,
    "Kokoro ZH Run": KokoroZHRun
}