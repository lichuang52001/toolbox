# # # # # # # # # # # # # # # # # #
# FUNCTION: GET REMOTE SENSING IMAGES FROM A LARGE DATABASE via A GIVEN LOCATION (latitude & longitude)
# VERSION : 2.0
# DATE    : 2023.06.01
# MAINTAINER: lichuang52001@gmail.com
# # # # # # # # # # # # # # # # # #

# LOAD PACKAGES
import os
import math
import time
import argparse
import xml.etree.ElementTree as ET
import csv

def location_in_or_out(path, outfile, lati, longi):
    def location_in_xml(xml_file, xml, lati, longi):
        def point_in_quadrilateral(x, y, vertices):
            count = 0
            num_vertices = len(vertices)
            for i in range(num_vertices):
                x1, y1 = vertices[i]
                x2, y2 = vertices[(i + 1) % num_vertices]
                if ((y1 <= y and y < y2) or (y2 <= y and y < y1)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
                    count += 1
            return count % 2 == 1

        xml_content = xml
        xml_file = xml_file
        # Parse the XML content
        root = ET.fromstring(xml_content)

        # Extract and display some information
        CenterLatitude = float(root.find('CenterLatitude').text)
        CenterLongitude = float(root.find('CenterLongitude').text)
        TopLeftLatitude = float(root.find('TopLeftLatitude').text)
        TopLeftLongitude = float(root.find('TopLeftLongitude').text)
        TopRightLatitude = float(root.find('TopRightLatitude').text)
        TopRightLongitude = float(root.find('TopRightLongitude').text)
        BottomRightLatitude = float(root.find('BottomRightLatitude').text)
        BottomRightLongitude = float(root.find('BottomRightLongitude').text)
        BottomLeftLatitude = float(root.find('BottomLeftLatitude').text)
        BottomLeftLongitude = float(root.find('BottomLeftLongitude').text)

        vertices = [(BottomLeftLongitude, BottomLeftLatitude), (BottomRightLongitude, BottomRightLatitude), (TopRightLongitude, TopRightLatitude), (TopLeftLongitude, TopLeftLatitude)]
        point = (longi, lati)

        if point_in_quadrilateral(point[0], point[1], vertices):
            print(f"THE INPUT LOCATION IS INSIDE {xml_file}")
            center_distance = math.sqrt((CenterLongitude - longi)**2 + (CenterLatitude - lati)**2)
            xml_dir = os.path.dirname(file_path)
            out_file.append([center_distance, xml_dir])

        else:
            print(f"THE INPUT LOCATION IS OUTSIDE {xml_file}")

        return out_file

    def read_xml_file(xml_file):
        try:
            start_time = time.time()
            with open(xml_file, 'r') as file:
                xml_content = file.read()
            end_time = time.time()
            # Check if the read time exceeds 2 seconds
            read_time = end_time - start_time
            if read_time > 2:
                print(f"Skipping {xml_file} due to long read time: {read_time} seconds")
                xml_content = 'null'
            return xml_content
        except IOError:
            print(f"Skipping {xml_file} due to unreadable file")
            xml_content = 'null'
            return xml_content

    out_file = outfile
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('PAN.xml'):
                file_path = os.path.join(root, file)
                xml_content = read_xml_file(file_path)
                if xml_content != 'null':
                    out_file = location_in_xml(file_path, xml_content, lati, longi)


def sort_csv(input_csv, output_csv):
    input_filename = input_csv
    output_filename = output_csv

    rows = []
    with open(input_filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    sorted_rows = sorted(rows[1:], key=lambda x: float(x[0]))

    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in sorted_rows:
            writer.writerow(row)

    print(f'SORTED CSV FILE {output_csv} IS EXPORTED')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EXPORT THE IMAGES INCLUDING THE INPUT LOCATION BY WALKING THROUGH ALL PAN.XML IN THE INPUT PATH')
    parser.add_argument('--in_path', type=str, help='the input path')
    parser.add_argument('--out_file', type=str, help='the output file path')
    parser.add_argument('--latitude', type=float, help='the latitude')
    parser.add_argument('--longitude', type=float, help='the longitude')

    args = parser.parse_args()
    input_path = args.in_path
    out_file = args.out_file
    jing_du = args.latitude
    wei_du = args.longitude

    # TEST PARAMETER
    # input_path = '/home/chuang/Desktop/get_image_via_location/data'
    # out_file = '/home/chuang/Desktop/get_image_via_location/images_sorted.txt'
    # jing_du = 29.92
    # wei_du  = 73.83

    print(f'THE INPUT PATH IS: {input_path}')
    print(f'THE OUTPUT FILE IS: {out_file}')
    print(f'THE INPUT LATITUDE IS: {jing_du}')
    print(f'THE INPUT LONGITUDE IS: {wei_du}', '\n')

    inside_array = [ ]

    location_in_or_out(input_path, inside_array, jing_du, wei_du)
    
    print(inside_array)

    sorted_array = sorted(inside_array, key=lambda x: x[0])

    header = ["Distance", "Path"]
    sorted_array.insert(0, header)

    with open(out_file, 'w') as file:
        for item in sorted_array:
            file.write(str(item) + '\n')
