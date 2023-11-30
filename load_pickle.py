import pickle

import numpy


with open('data.pickle', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    segments = pickle.load(file)

    for seg in segments:
        print(seg)