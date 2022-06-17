#!/usr/bin/env python
# coding=utf-8
import os


def find_files(rootdir, ext=".md"):
    fileList = [os.path.join(root, file)
                for root, _, files in os.walk(rootdir)
                for file in files
                if file.endswith(ext)]
    return fileList


def get_question_count(file_name):
    cnt = 0
    if os.path.exists(file_name):
        with open(file_name) as fp:
            cnt = sum(1 for line in fp.readlines() if "####" in line)
        return cnt, True
    return cnt, False


if __name__ == "__main__":
    base_folder = "/home/mayank/code/mj/ebooks/python/p_faiq/content"
    cnt = 0
    cnt = sum(get_question_count(files)[0]
              for files in find_files(base_folder))
    print(cnt)
