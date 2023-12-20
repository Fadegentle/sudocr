import sudocr


pics_dir = './pictures'
pics_files = [
    'demo.png',
    'paper.jpg',
    'sudoku.png',
    'sudoku_num.png',
    'sudoku_num_dark.png',
    'sudoku_big_dark.png'
    'board.png',
]


if __name__ == '__main__':
    for fp in pics_files:
        puzzle = sudocr.OCR().ocr_sudo(pics_dir + fp)
        print(f'{fp} 识别结果为：')
        sudocr.prettier(puzzle)
