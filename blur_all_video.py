import os
import subprocess
import sys

def process_video(input_file, output_file):
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'split[a][b];[a]scale=1080:1920,boxblur=40:5[1];[b]scale=1080:ih*1080/iw[2];[1][2]overlay=0:(H-h)/2',
        '-c:v', 'libx264',
        '-crf', '18',
        '-preset', 'veryfast',
        '-aspect', '9:16',
        '-f', 'mp4',
        output_file,
        '-y'
    ]
    subprocess.run(ffmpeg_command, check=True)

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.mp4'):
            input_file_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '-blur.mp4'
            output_file_path = os.path.join(output_folder, output_filename)

            process_video(input_file_path, output_file_path)
            print(f'Processed: {input_file_path} -> {output_file_path}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    process_folder(input_folder, output_folder)
