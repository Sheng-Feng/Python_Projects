"""
File: breakoutgraphics
Name: Aaron Kao
-------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2, x=(window_width-ball_radius*2)//2,
                          y=(window_height-ball_radius*2)//2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Default ball condition
        self.click = False

        # Default brick clear counter
        self.count = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.ball_velocity)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height, x=i*(brick_width+brick_spacing),
                                   y=brick_offset+j*(brick_height+brick_spacing))
                self.brick.filled = True
                self.brick.fill_color = (15*j, 8*j, 255-5*j)
                self.window.add(self.brick)

    def paddle_position(self, event):
        """
        Control the paddle position on the screen.
        """
        if event.x - self.paddle.width/2 <= 0:   # Boundary condition at the left side
            self.paddle.x = 0
        elif event.x + self.paddle.width/2 >= self.window.width:   # Boundary condition at the right side.
            self.paddle.x = self.window.width - self.paddle.width
        else:                            # Set mouse movement at the horizontal center point of paddle.
            self.paddle.x = event.x - self.paddle.width/2

    def ball_velocity(self, event):
        """
        Sets ball x velocity to a random negative or positive number.
        Sets ball y velocity to a constant number.
        """
        if not self.click:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.click = True    # Click T/F switch controls the ball movement which is not affect by the mouse click.

    def get_dx(self):
        """
        Getter Function: For safety, user can get dx value by this function.
        """
        return self.__dx

    def get_dy(self):
        """
        Getter Function: For safety, user can get dy value by this function.
        """
        return self.__dy

    def set_dx(self, dx):
        """
        Setter Function: For safety, user can set dx value by this function.
        """
        self.__dx = dx

    def set_dy(self, dy):
        """
        Getter Function: For safety, user can set dy value by this function.
        """
        self.__dy = dy

    def collision(self):
        """
        This function detects if the ball collides with an object.
        1. If the ball collides with an object, change velocity direction.
        2. If the object is brick, remove it.
        """
        # for i in range(2):  # Detect the four endpoints of the ball.
        #     for j in range(2):
        #         collision_obj = self.window.get_object_at(self.ball.x + i * self.ball.width,
        #                                                   self.ball.y + j * self.ball.height)
        for x in range(self.ball.x, self.ball.x+self.ball.width + 1, self.ball.width):    # other method. ball(x,y) need//2
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                collision_obj = self.window.get_object_at(x, y)
                if collision_obj is not None:
                    if collision_obj is self.paddle:
                        if self.__dy > 0:         # Avoid ball stick to the paddle. Idea from Jenny!
                            self.__dy = -self.__dy
                    else:
                        self.window.remove(collision_obj)   # If ball reach the brick, remove it.
                        self.count += 1
                        self.__dy = - self.__dy
                    return           # Terminate double for loop directly.

    def all_brick_clear(self):
        """
        This function judges whether all bricks are clear.
        If all bricks are clear, stop the program.
        """
        if self.count == BRICK_COLS * BRICK_ROWS:
            return False
        else:
            return True

    def reset_game(self):
        self.ball.x = (self.window.width - self.ball.width)//2
        self.ball.y = (self.window.width - self.ball.width) // 2
        self.__dx = 0
        self.__dy = 0
        self.click = False   # Click T/F switch controls the ball movement.

