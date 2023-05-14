import os

applications = ["MultiViewer for F1", "Google Chrome",
                "GitHub Desktop", "Spotify", "Visual Studio Code", "VLC"]  # Change these to your own apps

for application in applications:
    folder_path = f"/Applications/{application}.app/Contents/Resources/"
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".lproj") and not file.startswith("base."):
                os.remove(os.path.join(root, file))
