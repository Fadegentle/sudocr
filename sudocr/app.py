import argparse

from log import logger
from ocr import OCR

parser = argparse.ArgumentParser(description='识别数独')
parser.add_argument('--image-path', '-i', dest='image', help='识别图片路径')
args = parser.parse_args()

if __name__ == '__main__':
    res = OCR().ocr_sudo(args.image)
    logger.info(res) if res else logger.error(f"数独识别失败")