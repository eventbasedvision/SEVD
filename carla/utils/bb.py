import cv2
import xml.etree.ElementTree as ET
import os
import glob
import random


def draw_bounding_boxes(image_path, xml_path, output_path):
    image = cv2.imread(image_path)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall('object'):
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        # w = xmax - xmin
        # h = ymax - ymin
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    cv2.imwrite(output_path, image)


image_path = '/Users/manideepreddyaliminati/Documents/coding/research/carla/utils'
output_path = f'./data/'
png_files = glob.glob(os.path.join(image_path, '*.png'))
for png_file in png_files:
    img = os.path.abspath(png_file)
    annotation = img.replace("images", "annotations").replace("png", "xml")
    draw_bounding_boxes(image_path, annotation, output_path)

# xml_path = '/home/apg/manideep/carla/out/test/976.xml'
# output_path = '/home/apg/manideep/carla/out/test/output_image_with_boxes.jpg'

# draw_bounding_boxes(image_path, xml_path, output_path)
