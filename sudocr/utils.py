import cv2
import numpy as np
from log import logger, log_level


def show(func):
    def wrapper(*args):
        res = func(*args)
        if log_level == 'DEBUG':
            for i, j in enumerate((res,)):
                cv2.imshow(str(i), j)  # TODO：打印函数名
                cv2.waitKey(0)
            cv2.destroyAllWindows()
        return res

    return wrapper


def show_contours(contours, image, color=(0, 0, 255)):
    def show_contours_fun(func):
        def wrapper(*args):
            res = func(*args)
            if log_level == 'DEBUG':
                contours_n = len(contours)
                for i, contour in enumerate(contours):
                    res = cv2.drawContours(image.copy(), [contour], -1, color, 3)
                    cv2.imshow(f'Contour {i + 1}/{contours_n}', res)
                    cv2.waitKey(0)
                cv2.destroyAllWindows()
            return res

        return wrapper

    return show_contours_fun


def get_cell_coordinates(cell_width):
    border_offset = 5
    cells = []

    for row in range(9):
        for col in range(9):
            x0 = col * cell_width + border_offset
            y0 = row * cell_width + border_offset
            x1 = x0 + cell_width - border_offset
            y1 = y0 + cell_width - border_offset
            cells.append((x0, x1, y0, y1))

    return cells


def pythagoras(pt1, pt2):
    return np.sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)


def transform(pts, img):
    pts = np.float32(pts)
    top_l, top_r, bot_l, bot_r = pts[0], pts[1], pts[2], pts[3]

    width = int(max(pythagoras(bot_r, bot_l), pythagoras(top_r, top_l)))
    height = int(max(pythagoras(top_r, bot_r), pythagoras(top_l, bot_l)))
    square = max(width, height) // 9 * 9

    dim = np.array(([0, 0], [square - 1, 0], [square - 1, square - 1], [0, square - 1]), dtype='float32')
    matrix = cv2.getPerspectiveTransform(pts, dim)
    warped = cv2.warpPerspective(img, matrix, (square, square))  # TODO: debug show
    return warped


def warp(contours, image):
    contours = [contours[0]]
    largest_contour = np.squeeze(contours[0])

    sums = [sum(i) for i in largest_contour]
    differences = [i[0] - i[1] for i in largest_contour]

    top_left = np.argmin(sums)
    top_right = np.argmax(differences)
    bottom_left = np.argmax(sums)
    bottom_right = np.argmin(differences)

    corners = [largest_contour[top_left], largest_contour[top_right], largest_contour[bottom_left],
               largest_contour[bottom_right]]

    tr = transform(corners, image)
    gray = cv2.cvtColor(tr, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return thresh


def get_corners_xy(contours):
    contours_array = np.concatenate([c for c in contours])
    x_array = contours_array[:, :, 0]
    y_array = contours_array[:, :, 1]
    logger.info(f'查看 array {x_array.shape}')
    x_max = np.max(x_array)
    x_min = np.min(x_array)
    y_max = np.max(y_array)
    y_min = np.min(y_array)
    logger.info(f'查看坐标 {x_min, x_max, y_min, y_max}')
    return x_min, x_max, y_min, y_max


def crop(coordinates, image):
    x_min, x_max, y_min, y_max = coordinates
    cropped = np.array(image)[y_min:y_max, x_min:x_max]
    return cropped


@show
def handle(contours, image):
    logger.info(f'开始处理图片')
    if len(contours) > 1:
        contour_area0 = cv2.contourArea(contours[0])
        contour_area1 = cv2.contourArea(contours[1])
        if contour_area1 < 0.25 * contour_area0:
            return warp(contours, image)
    return crop(get_corners_xy(contours), image)


def crop_bounds(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh_not = cv2.bitwise_not(thresh)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    dilated = cv2.dilate(thresh_not, kernel, iterations=1)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:9]
    return handle(contours, image)


def to_hodoku(puzzle):
    boundary = '*-----------*\n'
    de_line = '|---+---+---|\n'
    hodoku = boundary

    for r, i in enumerate(puzzle):
        if r in [3, 6, 9]:
            hodoku += de_line
        for c, j in enumerate(i):
            if c in [0, 3, 6]:
                hodoku += '|'
            hodoku += j if j else '.'
        hodoku += '|\n'

    return hodoku + boundary


def prettier(puzzle):
    print(to_hodoku(puzzle))
