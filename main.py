from pytube import YouTube
def download_video(video_url, output_path='.'):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        print(f"Video Downloaded Sucessfully to {output_path}")
    except Exception as e:
        print(f"Error in Downloading video")

if __name__ == "__main__":
    video_url = input("Enter video url \n")
    output_path = "C:\\Visual Code\\Python\\youtube downloader"
    download_video(video_url, output_path)