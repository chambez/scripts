#!/bin/bash

# 输入文件路径
input_file="$1"
echo "input_file: ${input_file}"

# 输出文件路径
output_path="$2"
echo "output_path: ${output_path}"

# 分割文件的目标大小（单位为MB）
split_size_mb="$3"
echo "split_size: ${split_size_mb}MB"

# 将MB转换为字节
split_size=$((split_size_mb * 1024 * 1024 * 8))
echo "split_size_bytes: ${split_size}"

# 输出文件名的基本格式
output_format="${output_path}/output_%04d.mp4"

# 如果输出路径不存在，则创建目录
if [ ! -d "$output_path" ]; then
  mkdir -p "$output_path"
fi

# 使用ffprobe获取输入文件的时长和平均比特率
duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$input_file")
bitrate=$(ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 "$input_file")
echo "duration: ${duration}"
echo "bitrate: ${bitrate}"

# 将浮点数转换为整数
duration_int=${duration%.*}
bitrate_int=${bitrate%.*}
echo "duration_int: ${duration_int}"
echo "bitrate_int: ${bitrate_int}"

# 计算要分割的片段数
segment_count=$((($duration_int * $bitrate_int) / $split_size + 1))
echo "segment_count: ${segment_count}"

# 计算每个分割片段的时长（以秒为单位）
segment_duration=$((($duration_int + $segment_count - 1) / $segment_count))
echo "segment_duration: ${segment_duration}"

# 使用ffmpeg进行分割
ffmpeg -i "$input_file" -c copy -map 0 -segment_time $segment_duration -f segment -reset_timestamps 1 -segment_format_options movflags=+faststart "$output_format"
