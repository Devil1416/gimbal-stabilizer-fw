"""Complementary filter combining gyro integration and accelerometer."""
import math

class ComplementaryFilter:
    """
    Fuses gyroscope and accelerometer to estimate roll/pitch.
    alpha: weight on gyro (0–1); (1-alpha) on accel.
    """

    def __init__(self, alpha: float = 0.98):
        if not 0 < alpha < 1:
            raise ValueError("alpha must be in (0,1)")
        self.alpha = alpha
        self.roll  = 0.0
        self.pitch = 0.0

    def update(self, ax: float, ay: float, az: float,
               gx: float, gy: float, dt: float) -> tuple[float, float]:
        """
        ax/ay/az: accelerometer (m/s^2)
        gx/gy: gyro rates (rad/s) for roll and pitch axes
        Returns (roll_rad, pitch_rad).
        """
        accel_roll  = math.atan2(ay, az)
        accel_pitch = math.atan2(-ax, math.sqrt(ay**2 + az**2))
        self.roll  = self.alpha*(self.roll  + gx*dt) + (1-self.alpha)*accel_roll
        self.pitch = self.alpha*(self.pitch + gy*dt) + (1-self.alpha)*accel_pitch
        return self.roll, self.pitch
