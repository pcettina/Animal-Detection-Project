#https://chat.openai.com/share/f7d127f8-7da4-4751-9683-243c82731246
#help above
import cv2
import os
import argparse
import csv

def split_right(input_video, cap):
    # Get video information
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    top_half_height = int(frame_height * 0.55)  # Adjust the portion of the top half as needed
    bottom_half_height = frame_height - top_half_height
    # Vertical Half borders
    left_half_width = int(frame_width * 0.35)  # Adjust the portion of the top half as needed
    right_half_width = frame_width - left_half_width

    output_top_right_video = cv2.VideoWriter(f'{input_video[:len(input_video)-8]}output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width-left_half_width, top_half_height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        top_half = frame[0:top_half_height, :]
        top_right_half = top_half[:, left_half_width:frame_width]
        output_top_right_video.write(top_right_half)
    cap.release()
    output_top_right_video.release()

def split_left(input_video, cap):
    # Get video information
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    top_half_height = int(frame_height * 0.55)  # Adjust the portion of the top half as needed
    bottom_half_height = frame_height - top_half_height
    # Vertical Half borders
    left_half_width = int(frame_width * 0.65)  # Adjust the portion of the top half as needed
    right_half_width = frame_width - left_half_width

    output_top_left_video = cv2.VideoWriter(f'{input_video[:len(input_video)-8]}output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (left_half_width, top_half_height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        top_half = frame[0:top_half_height, :]
        top_left_half = top_half[:, 0:left_half_width]
        output_top_left_video.write(top_left_half)
    cap.release()
    output_top_left_video.release()

def split_bottom(input_video, cap):
    # Get video information
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    top_half_height = int(frame_height * 0.25)  # Adjust the portion of the top half as needed
    bottom_half_height = frame_height - top_half_height
    # Vertical Half borders
    left_half_width = int(frame_width * 0.5)  # Adjust the portion of the top half as needed
    right_half_width = frame_width - left_half_width

    output_bottom_video = cv2.VideoWriter(f'{input_video[:len(input_video)-8]}output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height - top_half_height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        bottom_half = frame[top_half_height:frame_height, :]
        output_bottom_video.write(bottom_half)
    cap.release()
    output_bottom_video.release()


def split_video(folder_path):
    file_path = os.listdir(folder_path)
    print(file_path)
    
    for input_video in file_path:
        if input_video.endswith('crop.mp4'):

            # Open the video
            video_path = os.path.join(folder_path, input_video)
            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():
                print('Error: Could not open the video.')
                exit()

            # Get video information
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))

            if(input_video.endswith('bottom_crop.mp4')):
                split_bottom(input_video, cap)
            elif(input_video.endswith('left_crop.mp4')):
                split_left(input_video, cap)
            elif(input_video.endswith('right_crop.mp4')):
                split_right(input_video, cap)


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Split a video into Trident and save each part as a separate video.')
    parser.add_argument('input_folder', help='Input video folder path')
    args = parser.parse_args()

    # Get the input video path
    input_folder = args.input_folder

    # Check if the input video file exists
    if not os.path.exists(input_folder):
        print('Error: Input video file not found.')
        exit()

    # Call the function to split the videos and create CSV
    split_video(input_folder)
