## 功能介绍
1. 将一个横屏的长视频分割成一个个小视频
2. 每个小视频转换成9:16的竖屏视频，空白部分使用类似剪映的背景模糊效果
3. 依次对每个小视频添加文字/集数信息

## 环境准备
- python3
- ffmpeg
- ffprobe

## 使用方法

1. **分割视频**
- 比如你的视频大小是600M 时长是30分钟 你想得到长度大致相等的15个小视频 那么每个视频的时长是2分钟左右 大小是40M左右
- 执行`segment_videos.sh`脚本
```
sh segment_videos.sh 原视频所在目录 准换后的视频存放目录 每个视频的文件大小
```
例如：
```
sh segment_videos.sh /home/test/西游记后传.mp4 ./convert_videos 40
```

2. **将分割后的每个小视频都加上背景模糊效果**
- 执行脚本`blur_all_video.py`
```
python3 blur_all_video.py 视频目录 转换后的视频存放目录
```
例如：
```
python3 blur_all_video.py ./convert_videos ./blur_videos
```

3. **给每个视频加上片名和集数**
- 执行脚本`add_text.py`
```
python3 add_text.py 视频目录 要添加的文本信息 转换后的视频存放目录 字体文件路径
```
例如：
```
python3 add_text.py ./blur_videos 西游记后传 ./final_videos te.ttf
```

## 视频讲解
- https://www.youtube.com/watch?v=p8gYKYjn4Ec

---
- 每个脚本功能比较独立 感兴趣的话可以把这个3个步骤整合下
