from threading import Thread
from time import sleep
from controller import TimerController, TimerView
import simpleaudio as sa

class TextTimerView(TimerView):

    def __init__(self, model):
        self._controller = TimerController(model, self)

    def run(self):
        """Run the text-based timer."""
        time = self._getTimeFromUser()
        self._thread = Thread(target=self._input_loop, daemon=True)
        self._thread.start()
        self._controller.start(time)
        while not self._controller.stopped():
            sleep(1)

    def update_time(self, time):
        """Display the time."""
        print(time)

    def timer_done(self):
        """Indicate the timer is done."""
        # Play a sound
        wave_obj = sa.WaveObject.from_wave_file("coffee.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print("DING DING DING DING DING")

    def _getTimeFromUser(self):
        """Get a positive integer time from the user."""
        while True:
            s = input("Enter time in seconds: ")
            if s[0] == 'q':
                return 
            try:
                time = int(s) 
                assert time >= 0
                return time
            except:
                continue

    def _input_loop(self):
        """Accept user input to pause or resume. Run in a new thread."""
        print("Hit return to pause or resume timer")
        while True:
            input()
            print("Paused")
            self._controller.pause()
            input()
            self._controller.resume()
