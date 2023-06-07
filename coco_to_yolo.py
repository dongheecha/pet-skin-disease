# This is a sample Python script.
import json
import os
import shutil
from glob import glob

import cv2

IMG_WIDTH = 1920
IMG_HEIGHT = 1080


def test_data_from_train(train_dir, test_dir):
    D_A1 = 0
    D_A2 = 0
    D_A3 = 0
    D_A4 = 0
    D_A5 = 0
    D_A6 = 0
    C_A1 = 0
    C_A2 = 0

    for file in glob(os.path.join(train_dir, '*.txt')):

        if 'D_A1' in file:
            print(file)
            if D_A1 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                D_A1 += 1
        elif 'D_A2' in file:
            print(file)
            if D_A2 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                D_A2 += 1
        elif 'D_A3' in file:
            print(file)
            if D_A3 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                D_A3 += 1
        elif 'D_A4' in file:
            print(file)
            if D_A4 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                D_A4 += 1
        elif 'D_A5' in file:
            print(file)
            if D_A5 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                D_A5 += 1

        elif 'D_A6' in file:
            print(file)
            if D_A6 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                D_A6 += 1
        elif 'C_A1' in file:
            print(file)
            if C_A1 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                C_A1 += 1

        elif 'C_A2' in file:
            print(file)
            if C_A2 < 2500:
                shutil.copy(f'{file}', f'{test_dir}')
                C_A2 += 1


def convert(x, y, width, height):
    x_centre = (x + (x + width)) / 2
    y_centre = (y + (y + height)) / 2

    # Normalization
    x_centre = x_centre / IMG_WIDTH
    y_centre = y_centre / IMG_HEIGHT
    w = width / IMG_WIDTH
    h = height / IMG_HEIGHT

    # Limiting upto fix number of decimal places
    x_centre = format(x_centre, '.6f')
    y_centre = format(y_centre, '.6f')
    w = format(w, '.6f')
    h = format(h, '.6f')

    return x_centre, y_centre, w, h


def extract_bbox_label_from_json(label, dir_path, output_path):
    for file in os.listdir(os.path.join(f'{dir_path}')):

        if file.split('.')[1] == 'json':
            f = open(os.path.join(f'{dir_path}/{file}'), 'r', encoding='UTF8')
            text = json.loads(f.read())
            file_name = file.split('.')[0]
            print(file)
            fw = open(f'{output_path}\\{file_name}.txt', 'w')

            for label_info in text['labelingInfo']:

                if list(label_info.keys())[0] == 'box':
                    bbox = label_info['box']['location'][0]

                    x = list(bbox.values())[0]
                    y = list(bbox.values())[1]
                    w = list(bbox.values())[2]
                    h = list(bbox.values())[3]

                    x_center, y_center, w, h = convert(x, y, w, h)

                    fw.write(f"{label} {x_center} {y_center} {w} {h}\n")

                    f.close()
                    continue  # Detection 1개만
    fw.close()


def get_keypoint_list(keypoint):
    keypoint_list = []

    keypoint_dict = dict()
    for keypoint in keypoint.items():

        if 'y' in keypoint[0]:
            keypoint_dict['y'] = keypoint[1]
            keypoint_list.append(keypoint_dict)
            keypoint_dict = dict()
        else:
            keypoint_dict['x'] = keypoint[1]
    return keypoint_list


def draw(image_path, keypoint):
    keypoint_list = []
    img = cv2.imread(image_path)
    keypoint_dict = dict()
    for keypoint in keypoint.items():

        if 'y' in keypoint[0]:
            keypoint_dict['y'] = keypoint[1]
            keypoint_list.append(keypoint_dict)
            keypoint_dict = dict()
        else:
            keypoint_dict['x'] = keypoint[1]

        for keypoint in keypoint_list:
            cv2.circle(img, (keypoint['x'], keypoint['y']), 7, (0, 255, 0))

        cv2.imshow('left keypoint !!!', img)
        cv2.waitKey(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    extract_bbox_label_from_json(
        dir_path="C:\\Users\\도니\\Downloads\\152.반려동물 피부질환 데이터\\01.데이터\\2.Validation\\2_라벨링데이터\\VL01\\반려묘\\피부\\일반카메라\\유증상\\A2_비듬_각질_상피성잔고리",
        output_path="C:\\dog-skin-disease\\data\\bbox\\validate\\image",
        label=6)
    # test_data_from_train(train_dir="C:\\dog-skin-disease\\data\\bbox\\train\\image",
    #                      test_dir="C:\\dog-skin-disease\\data\\bbox\\test\\image")
