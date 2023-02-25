class Ball:
    def __init__(self, mass, size):
        self.mass = mass
        self.size = size
        self.position = 0
        self.velocity = 0

    def update_position(self, time_step):
        self.position += self.velocity * time_step

    def update_velocity(self, force, time_step):
        acceleration = force / self.mass
        self.velocity += acceleration * time_step


class Gravity:
    def __init__(self, acceleration):
        self.acceleration = acceleration

    def calculate_force(self, ball):
        return ball.mass * self.acceleration


if __name__ == '__main__':
    ball = Ball(0.1, 0.05)
    gravity = Gravity(9.8)

    time_step = 0.01
    for i in range(20):
        force = gravity.calculate_force(ball)
        ball.update_velocity(force, time_step)
        ball.update_position(time_step)

        print('Position: %.4f' % ball.position)

