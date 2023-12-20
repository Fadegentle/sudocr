import sys

import gradio as gr
from loguru import logger
from ocr import OCR
from utils import to_hodoku


def handle(image):
    if isinstance(image, str):
        raise gr.Error("输入错误")

    try:
        res = to_hodoku(OCR().ocr_sudo(image))
    except Exception as e:
        raise gr.Error(f"识别失败: {e}")
    return res


def get_sukocr():
    logger.remove()
    logger.add(sys.stderr, level="DEBUG")
    return handle


ocr = gr.Interface(
    handle,
    gr.Image(sources=["upload", "webcam", "clipboard"]),
    gr.Textbox(
            label="Output",
            info="HoDoKu Format",
            show_copy_button=True,
        ),
    title="数独 OCR"
)
ocr.launch()
