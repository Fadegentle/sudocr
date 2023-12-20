import cv2
import numpy as np
from paddleocr import PaddleOCR
from loguru import logger
import utils


class OCR:

    def __init__(self):
        self.model = PaddleOCR(lang='en', use_gpu=True)

    def ocr(self, image, det=False, rec=True, cls=False):
        return self.model.ocr(np.array(image), det=det, rec=rec, cls=cls)

    def ocr_digit(self, cell_image):
        ocr_data = self.ocr(cell_image)
        char = (ocr_data[0][0][0] if ocr_data else '').strip().replace(':', '8')
        return char if char.isdigit() else ''

    @logger.catch
    def ocr_sudo(self, image):
        if isinstance(image, str):
            image = cv2.imread(image)
        logger.info(f'识别图片大小: {image.shape}')
        sudo = utils.crop_bounds(image)
        cell_width = sudo.shape[1] // 9
        cell_coordinates = utils.get_cell_coordinates(cell_width)
        digits = [self.ocr_digit(utils.crop(cell, sudo)) for cell in cell_coordinates]
        puzzle = [digits[i:i + 9] for i in range(0, len(digits), 9)]
        return puzzle
