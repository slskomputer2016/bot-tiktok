from moviepy.config import change_settings
from pathlib import Path
from moviepy.video.fx.all import speedx


change_settings({
    "IMAGEMAGICK_BINARY":
        r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    ColorClip,
)

video = VideoFileClip("mountain_55.mp4")

kalimat = [
    "Hutan Kalimantan bukan sekadar pepohonan, tetapi rumah bagi kehidupan.",
    "Di balik kobaran api, banyak satwa yang kehilangan tempat tinggal.",
    "Musibah ini mengingatkan kita untuk lebih peduli kepada alam.",
    "Mari bersama-sama menjaga hutan dan kehidupan di dalamnya.",
    "Semoga Kalimantan kembali hijau dan tumbuh."
]

clips = []

durasi_text = (video.duration / len(kalimat));

for i, teks in enumerate(kalimat):

    # Waktu mulai
    start = i * durasi_text

    # =========================
    # TEXT
    # =========================

    text = TextClip(
        teks,
        fontsize=30,
        color="orange",
        font="Arial",
        method="caption",
        size=(700, 500),
        align="center"
    )

    text = (
        text
        .set_start(start)
        .set_duration(durasi_text)
        .set_position(("center", "center"))
    )

    # =========================
    # BACKGROUND
    # =========================

    padding_x = 30
    padding_y = 20

    background = ColorClip(
        size=(
            text.w + padding_x * 2,
            text.h + padding_y * 2
        ),
        color=(0, 0, 0)
    )

    background = (
        background
        .set_start(start)
        .set_duration(durasi_text)
        .set_opacity(0.6)
        .set_position(("center", "center"))
    )

    # =========================
    # MASUKKAN KE LIST
    # =========================

    clips.append(background)
    clips.append(text)

#========================================================
#========================================================
#========================================================


final = CompositeVideoClip([video] + clips)
final.write_videofile(
    "video_tiktok.mp4",
    codec="libx264",
    audio_codec="aac",
    fps=video.fps
)

video.close()
final.close()
