import glob
import os
import subprocess
import json
import time
from typing import *
from wechat_ocr.ocr_manager import OcrManager, OCR_MAX_TASK_ID

WECHAT_OCR_DIR = None
WECHAT_DIR = None

ocr_manager: OcrManager = None
ocr_res: dict = None


class OutputType:
    Detailed = "详细"
    Concise = "精简"


def get_ocr_paths(wechat_ocr_dir: str = "", wechat_dir: str = ""):
    global WECHAT_DIR
    global WECHAT_OCR_DIR

    if WECHAT_DIR and WECHAT_OCR_DIR:
        return

    if wechat_ocr_dir and wechat_dir:
        WECHAT_DIR = wechat_dir
        WECHAT_OCR_DIR = wechat_ocr_dir
        return

    def _find_wechat_dir():
        """查找微信路径"""

        try:
            cmd_str = 'reg query "HKCU\\Software\\Tencent\\WeChat" /v InstallPath'
            path = subprocess.check_output(cmd_str).decode().split('REG_SZ')[-1].strip()
            result = glob.glob(r"{}\*\mmmojo.dll".format(path))
            if len(result) != 0:
                return os.path.dirname(result[0])
        except:
            pass

        for item in "CDEFGHIJK":
            result = glob.glob(r"{}:\*\Tencent\WeChat\*\mmmojo.dll".format(item))
            if len(result) != 0:
                return os.path.dirname(result[0])

        for item in "CDEFGHIJK":
            result = glob.glob(r"{}:\*\WeChat\*\mmmojo.dll".format(item))
            if len(result) != 0:
                return os.path.dirname(result[0])

        return None

    def _find_wechat_plugins():
        """查找微信插件路径"""
        appdata_path = os.getenv('APPDATA')

        ocr_dir = os.path.join(appdata_path, r"Tencent\WeChat\XPlugin\Plugins\WeChatOCR")
        if not os.path.exists(ocr_dir):
            return None

        result = glob.glob(fr"{ocr_dir}\*\extracted\WeChatOCR.exe")
        if len(result) == 0:
            return None

        return os.path.dirname(result[0])

    # 自动找微信ocr插件的位置。因为自动查会慢一点，所以注释掉
    # wechat_ocr_dir = _find_wechat_plugins()
    # wechat_dir = _find_wechat_dir()





    if wechat_ocr_dir and wechat_dir:
        WECHAT_DIR = wechat_dir
        WECHAT_OCR_DIR = wechat_ocr_dir
        return

    raise FileNotFoundError("未找到微信路径，请用 “配置微信OCR” 指令手动指定路径")


def ocr_result_callback(img_path: str, results: dict):
    global ocr_res
    ocr_res = results


def start_wechat_ocr(wechat_ocr_dir: str = "", wechat_dir: str = ""):
    """启动微信OCR服务"""
    global ocr_manager

    get_ocr_paths(wechat_ocr_dir, wechat_dir)

    if not ocr_manager:
        ocr_manager = OcrManager(WECHAT_DIR)
        ocr_manager.SetExePath(WECHAT_OCR_DIR)
        ocr_manager.SetUsrLibDir(WECHAT_DIR)
        ocr_manager.SetOcrResultCallback(ocr_result_callback)
        ocr_manager.StartWeChatOCR()


def wechat_ocr(image_path, output_type=OutputType.Detailed) -> dict:
    global ocr_res
    ocr_res = None

    if not ocr_manager:
        start_wechat_ocr("./resource/wechatOcr/extracted","./resource/wechatOcr")

    # 开始识别图片
    ocr_manager.DoOCRTask(image_path)
    while ocr_manager.m_task_id.qsize() != OCR_MAX_TASK_ID:
        pass

    if output_type == OutputType.Concise:
        ocr_res["ocrResult"] = list(map(lambda i: i['text'], ocr_res["ocrResult"]))
        return ocr_res["ocrResult"]
    else:

        return ocr_res


image_path = "./resource/image/mission.png"
res = wechat_ocr(image_path, OutputType.Concise)
print(res)

