import gradio as gr
from ocr import ocr
from utils import to_hodoku


def handle(image):
    if isinstance(image, str):
        raise gr.Error("输入错误")

    try:
        res = to_hodoku(ocr.ocr_sudo(image))
    except Exception as e:
        raise gr.Error(f"识别失败: {e}")
    return res


with gr.Blocks(gr.themes.Default(font=gr.themes.GoogleFont("IBM Plex Mono"), text_size='lg')) as app:
    gr.Interface(
        handle,
        gr.Image(sources=["upload", "webcam", "clipboard"]),
        gr.Textbox(
            label="Output",
            info="HoDoKu Format",
            show_copy_button=True,
        ),
        title="数独 OCR",
        allow_flagging='never',
    )


if __name__ == '__main__':
    app.launch(share=True, height=1080)
