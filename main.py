import os

applications = ["MultiViewer for F1.app", "Google Chrome.app",
                "GitHub Desktop.app", "Spotify.app", "Visual Studio Code.app", "VLC.app"]

for application in applications:
    folder_path = f"/Applications/{application}/Contents/Resources/"
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".lproj") and not file.startswith("base."):
                os.remove(os.path.join(root, file))
