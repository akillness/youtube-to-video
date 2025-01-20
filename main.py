# streamlit_app.py

import streamlit as st
from pytube import YouTube
import os

# Streamlit 앱
st.title("YouTube Video Downloader")

# 유튜브 URL 입력
youtube_url = st.text_input("Enter YouTube URL:")

# 다운로드 버튼
if st.button("Download Video"):
    if youtube_url:
        try:
            # YouTube 객체 생성
            yt = YouTube(youtube_url)
            st.write(f"**Video Title:** {yt.title}")
            st.write(f"**Channel:** {yt.author}")
            st.write(f"**Views:** {yt.views:,}")

            # 동영상 다운로드 (최고 해상도 선택)
            video = yt.streams.get_highest_resolution()
            output_path = "./downloads"
            os.makedirs(output_path, exist_ok=True)
            video_file = video.download(output_path)

            # 다운로드 성공 메시지
            st.success("Video downloaded successfully!")
            st.write(f"**Saved to:** {video_file}")

            # 파일 제공
            with open(video_file, "rb") as f:
                st.download_button(
                    label="Download File",
                    data=f,
                    file_name=os.path.basename(video_file),
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")