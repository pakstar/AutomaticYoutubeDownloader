import yt_dlp

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    # Set up the options for downloading (this will get the highest resolution)
    ydl_opts = {
        'format': 'best',
        'outtmpl': './%(title)s.%(ext)s',  # Saves the video with its title in the current directory
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
    print("Download complete.")

except Exception as e:
    print("An error occurred:", str(e))
