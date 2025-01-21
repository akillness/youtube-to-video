import instaloader
import os
from moviepy import VideoFileClip

def download_instagram_video(post_url, output_dir="downloads"):
    """
    Download Instagram video using Instaloader and return the file path.
    
    Args:
        post_url (str): URL of the Instagram post.
        output_dir (str): Directory to save downloaded videos.

    Returns:
        str: Path of the downloaded video.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize Instaloader
    loader = instaloader.Instaloader(download_videos=True, quiet=True)
    
    # Extract shortcode from the post URL
    shortcode = post_url.split("/")[-2]
    
    try:
        # Download the video
        loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target=output_dir)
        
        # Locate the downloaded video
        for file in os.listdir(output_dir):
            if file.endswith(".mp4"):
                video_path = os.path.join(output_dir, file)
                print(f"Downloaded video: {video_path}")
                return video_path
    
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

def convert_video_to_format(video_path, output_format="mp4"):
    """
    Convert a video to a specific format using MoviePy and delete the original video.
    
    Args:
        video_path (str): Path of the input video.
        output_format (str): Desired output format (e.g., 'mp4', 'avi').

    Returns:
        str: Path of the converted video.
    """
    output_path = video_path.rsplit(".", 1)[0] + f"_final.{output_format}"
    try:
        clip = VideoFileClip(video_path)
        clip.write_videofile(output_path, codec="libx264", bitrate="5000k", preset="slow")
        clip.close()
        
        # Delete the original video after successful conversion
        os.remove(video_path)
        print(f"Original video deleted: {video_path}")
        
        print(f"Converted video: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error converting video: {e}")
        return None

# Example usage
if __name__ == "__main__":
    instagram_post_url = "https://www.instagram.com/p/XXXXXXXXXXX/"
    
    # Step 1: Download the Instagram video
    downloaded_video = download_instagram_video(instagram_post_url)
    
    if downloaded_video:
        # Step 2: Convert the downloaded video and delete the original file
        convert_video_to_format(downloaded_video, output_format="mp4")