import curses
from threading import Thread
from time import sleep
from controller import TimerController, TimerView
import simpleaudio as sa

class TextTimerView(TimerView):

    def __init__(self, model):
        self._controller = TimerController(model, self)
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

    def __del__(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

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
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, str(time))
        self.stdscr.refresh()

    def timer_done(self):
        """Indicate the timer is done."""
        # Play a sound
        wave_obj = sa.WaveObject.from_wave_file("coffee.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        self.stdscr.refresh()

    def _getTimeFromUser(self):
        """Get a positive integer time from the user."""
        while True:
            self.stdscr.addstr(0, 0, "Enter time in seconds: ")
            s = self.stdscr.getstr().decode('utf-8')
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
        self.stdscr.addstr(1, 0, "Hit return to pause or resume timer")
        while True:
            self.stdscr.getch()
            self.stdscr.addstr(2, 0, "Paused")
            self.stdscr.refresh()
            self._controller.pause()
            self.stdscr.getch()
            self._controller.resume()