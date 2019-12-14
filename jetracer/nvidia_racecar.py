from .racecar import Racecar
import traitlets
from .tianracer_servo import ServoKit


class NvidiaRacecar(Racecar):
    
    steering_gain = traitlets.Float(default_value=1)
    steering_offset = traitlets.Float(default_value=0)
    throttle_gain = traitlets.Float(default_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kit = ServoKit()

    @traitlets.observe('steering')
    def _on_steering(self, change):
        self.kit.servo = change['new'] * self.steering_gain + self.steering_offset

    @traitlets.observe('throttle')
    def _on_throttle(self, change):
        self.kit.motor = change['new'] * self.throttle_gain
