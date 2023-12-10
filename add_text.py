import os
import subprocess
import sys

def add_text_to_mp4(input_folder, first_line_text, output_folder, font_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mp4_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]
    mp4_files.sort()

    for i, mp4_file in enumerate(mp4_files, start=1):
        input_file = os.path.join(input_folder, mp4_file)
        output_file = os.path.join(output_folder, f"{first_line_text}-{i}.mp4")

        ffmpeg_command = (
            f'ffmpeg -i "{input_file}" -vf '
            f'"drawtext=text=\'{first_line_text}\':x=(w-tw)/2:y=h/5:fontsize=80:fontcolor=yellow:fontfile={font_path}, '
            f'drawtext=text=\'{i}\':x=(w-tw)/2:y=3*h/4:fontsize=80:fontcolor=yellow:fontfile={font_path}" '
            f'-c:a copy "{output_file}" -y'
        )

        subprocess.run(ffmpeg_command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_folder> <first_line_text> <output_folder> [font_path]")
        sys.exit(1)

    input_folder_path = sys.argv[1]
    first_line_text = sys.argv[2]
    output_folder_path = sys.argv[3]
    font_path = sys.argv[4] if len(sys.argv) >= 5 else "te.ttf"

    add_text_to_mp4(input_folder_path, first_line_text, output_folder_path, font_path)
