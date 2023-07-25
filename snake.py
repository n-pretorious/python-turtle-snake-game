from turtle import Turtle

MOVE_DISTANCE = 15
STARTING_POSITIONS = [(0, 0), (-MOVE_DISTANCE, 0), (-2 * MOVE_DISTANCE, 0)]
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = self.create_segment(position)
            self.segments.append(new_segment)

    @staticmethod
    def create_segment(position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        return segment

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def set_direction(self, direction):
        if self.head.heading() != direction:
            self.head.setheading(direction)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.set_direction(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.set_direction(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.set_direction(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.set_direction(RIGHT)

    def grow_snake(self):
        tail = self.segments[-1]
        new_tail = self.create_segment(tail.position() - (MOVE_DISTANCE, 0))
        self.segments.append(new_tail)

    def check_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
