import time


class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def start(self):
        while True:
            if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
                break

            time.sleep(1)
            self.seconds -= 1

            if self.seconds < 0:
                self.seconds = 59
                self.minutes -= 1
                if self.hours > 0 > self.minutes:
                    self.minutes = 59
                    self.hours -= 1

            print(f"{self.hours} hours {self.minutes} minutes {self.seconds} seconds remaining...")

        print("Timer completed!")
