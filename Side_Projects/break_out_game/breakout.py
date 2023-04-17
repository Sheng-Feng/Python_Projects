"""
File: breakout
Name: Aaron Kao
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second 10
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This program plays a Python game 'breakout'
    A ball will be bouncing around the GWindow.
    Players must control the paddle to bounce the ball and clear all bricks.
    If Player miss to catch the ball more than 3 times, the game is over.
    If Player clear all bricks, you win.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        if lives > 0 and graphics.all_brick_clear():
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.ball.y >= graphics.window.height - graphics.ball.height:  # If ball reach the bottom of window,
                graphics.reset_game()
                lives -= 1
            else:
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    graphics.set_dx(- graphics.get_dx())  # Bounce the ball when the ball reach left and right sides.
                if graphics.ball.y <= 0:
                    graphics.set_dy(- graphics.get_dy())  # Bounce the ball when the ball reach top side.
            graphics.collision()
            pause(FRAME_RATE)
        else:
            break   # Stop the loop if lost all lives or clear all bricks.


if __name__ == '__main__':
    main()
