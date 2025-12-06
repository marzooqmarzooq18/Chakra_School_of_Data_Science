class Student:
    def __init__(self, name, total_chapters):
        self.name = name
        self.total_chapters = total_chapters
        self.completed = 0

    def update_progress(self, chapters_done):
        """Add completed chapters and update progress."""
        self.completed += chapters_done  # ← Set breakpoint here for debugging
        if self.completed > self.total_chapters:
            self.completed = self.total_chapters

    def progress_percent(self):
        """Return how much of the course is completed."""
        return (self.completed / self.total_chapters) * 100
