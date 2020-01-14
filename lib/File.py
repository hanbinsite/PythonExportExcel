# -*- coding:  UTF-8 -*-
import os
import time


class FILE:
    def __init__(self):
        if os.path.exists("data") is False:
            os.mkdir("data")
        self.filePath = r"data/" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".xlsx"
        if os.path.exists(self.filePath) is False:
            open(self.filePath, mode='wt', encoding='utf-8')
            # os.mknod(self.filePath)

    def __enter__(self):
        return self.filePath

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.filePath)
