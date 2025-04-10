import json
import os

# File to store the video data
JSON_FILE = "videos.json"

def load_videos():
    """Load videos from the JSON file. If file doesn't exist, return empty list."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    return []

def save_videos(videos):
    """Save videos to the JSON file."""
    with open(JSON_FILE, 'w') as file:
        json.dump(videos, file, indent=4)

def display_videos(videos):
    """Display all videos in a formatted way."""
    print("\n--- Video Library ---")
    for idx, video in enumerate(videos, 1):
        print(f"{idx}. {video['video_name']} ({video['duration']}) - {video['platform']}")

def add_video(videos):
    """Add a new video to the library."""
    print("\nAdd New Video")
    video = {
        "video_name": input("Video title: "),
        "link": input("URL: "),
        "duration": input("Duration (HH:MM:SS): "),
        "platform": input("Platform (YouTube/Udemy/etc): ")
    }
    videos.append(video)
    save_videos(videos)
    print("✅ Video added successfully!")

def edit_video(videos):
    """Edit an existing video."""
    display_videos(videos)
    try:
        choice = int(input("\nEnter video number to edit: ")) - 1
        if 0 <= choice < len(videos):
            print(f"\nEditing: {videos[choice]['video_name']}")
            videos[choice] = {
                "video_name": input(f"New title [{videos[choice]['video_name']}]: ") or videos[choice]['video_name'],
                "link": input(f"New URL [{videos[choice]['link']}]: ") or videos[choice]['link'],
                "duration": input(f"New duration [{videos[choice]['duration']}]: ") or videos[choice]['duration'],
                "platform": input(f"New platform [{videos[choice]['platform']}]: ") or videos[choice]['platform']
            }
            save_videos(videos)
            print("✅ Video updated!")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_video(videos):
    """Delete a video from the library."""
    display_videos(videos)
    try:
        choice = int(input("\nEnter video number to delete: ")) - 1
        if 0 <= choice < len(videos):
            deleted = videos.pop(choice)
            save_videos(videos)
            print(f"✅ Deleted: {deleted['video_name']}")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """Main menu loop."""
    videos = load_videos()
    while True:
        print("\n📺 Video Library Manager")
        print("1. View Videos")
        print("2. Add Video")
        print("3. Edit Video")
        print("4. Delete Video")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            display_videos(videos)
        elif choice == "2":
            add_video(videos)
        elif choice == "3":
            edit_video(videos)
        elif choice == "4":
            delete_video(videos)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initialize with sample data if file is empty
    if not os.path.exists(JSON_FILE):
        sample_data = [
            {
                "video_name": "Python Tutorial for Beginners",
                "link": "https://www.youtube.com/watch?v=9N6a-VLBa2I",
                "duration": "20:33",
                "platform": "YouTube"
            }
        ]
        save_videos(sample_data)
    
    main()
            

    