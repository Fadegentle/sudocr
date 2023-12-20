最近在用 `HoDoKu` 解其他软件的数独，填数字的过程太折磨了，受不了一点，就想着能不能自动化，参考了一下网上随便写的，请多包涵🤣

---

目标格式（来自 [`HoDoKu Manual`](https://hodoku.sourceforge.net/en/docs_play.php)）：

```
 *-----------*

 |6..|..2|3..|

 |125|6..|...|

 |..4|7..|.2.|

 |---+---+---|

 |73.|...|84.|

 |...|...|...|

 |.46|...|.15|

 |---+---+---|

 |.5.|..8|1..|

 |...|..3|472|

 |..7|2..|..8|

 *-----------*
```
 
未来希望可以识别带可能数字的格式：
```
 *--------------------------------------------------------------------*

 | 6      7      89     | 189    189    2      | 3      5      4      |

 | 1      2      5      | 6      3      4      | 9      8      7      |

 | 3      89     4      | 7      589    59     | 6      2      1      |

 *----------------------+----------------------+----------------------|

 | 7      3      29     | 159    12569  1569   | 8      4      69     |

 | 5      1      289    | 89     4      679    | 27     69     3      |

 | 89     4      6      | 3      289    79     | 27     1      5      |

 *----------------------+----------------------+----------------------|

 | 2      5      3      | 4      7      8      | 1      69     69     |

 | 89     689    1      | 59     569    3      | 4      7      2      |

 | 4      69     7      | 2      169    169    | 5      3      8      |

 *--------------------------------------------------------------------*
```

---

参考资料：
1. [基于OpenCV及Python的数独问题识别与求解](https://blog.csdn.net/howlclat/article/details/78838214)
2. [OCR-recognition-and-Solve-sudoku-recursively](https://github.com/one066/OCR-recognition-and-Solve-sudoku-recursively/blob/main/sudoku.py)
3. [How to remove convexity defects in a Sudoku square?](https://stackoverflow.com/questions/10196198/how-to-remove-convexity-defects-in-a-sudoku-square)
4. [sudoku-py](https://github.com/AliShazly/sudoku-py)
5. [sudoku-solver](https://github.com/lesskop/sudoku-solver)
6. [sudoku-terminator]( https://github.com/gameofdimension/sudoku-terminator)