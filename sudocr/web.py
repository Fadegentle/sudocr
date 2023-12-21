import gradio as gr
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
