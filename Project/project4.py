
import os
import shutil
import logging
from datetime import datetime

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh"],
    "Others": []  
}


logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



class FileOrganizer:
    def __init__(self, target_dir, by_date=False, dry_run=False):
        self.target_dir = target_dir
        self.by_date = by_date
        self.dry_run = dry_run

    def _get_category(self, file):
        """Return category based on extension"""
        ext = os.path.splitext(file)[1].lower()
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                return category
        return "Others"

    def _get_date_folder(self, file_path):
        """Return folder name based on modification date (YYYY-MM)"""
        timestamp = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(timestamp)
        return date.strftime("%Y-%m")

    def organize(self):
        """Organize files into subfolders"""
        for entry in os.scandir(self.target_dir):
            if entry.is_file():
                category = self._get_category(entry.name)
                dest_folder = os.path.join(self.target_dir, category)

                
                if self.by_date:
                    date_folder = self._get_date_folder(entry.path)
                    dest_folder = os.path.join(dest_folder, date_folder)

                os.makedirs(dest_folder, exist_ok=True)

                dest_path = os.path.join(dest_folder, entry.name)

                if self.dry_run:
                    print(f"[DRY RUN] Would move: {entry.path} → {dest_path}")
                else:
                    shutil.move(entry.path, dest_path)
                    logging.info(f"Moved {entry.path} → {dest_path}")
                    print(f"✅ Moved {entry.name} → {dest_folder}")


def main():
    print("=== Automated File Organizer ===")
    target = input("Enter directory path to organize: ").strip()
    if not os.path.isdir(target):
        print("❌ Invalid directory path.")
        return

    by_date = input("Organize by date? (y/n): ").strip().lower() == "y"
    dry_run = input("Dry run mode? (y/n): ").strip().lower() == "y"

    organizer = FileOrganizer(target, by_date, dry_run)
    organizer.organize()

    print("🎉 Organization complete!")


if __name__ == "__main__":
    main()
