import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0]
        bricks = cast["brick"]
        score = cast["score"][0]
        
        for count, brick in enumerate(bricks):
            if ball.get_position().equals(brick.get_position()):
                velocity = ball.get_velocity().on_brick_hit()
                points = score.get_score()
                points = points + 1
                score.set_score(points)
                bricks.pop(count)
                return ball.set_velocity(velocity), score.set_text(f"Score: {points}")
            
        
        ball_pos = ball.get_position()
        paddle_pos = paddle.get_position()

        if ball_pos.get_x() in range(paddle_pos.get_x(),paddle_pos.get_x()+11) and ball_pos.get_y() == paddle_pos.get_y() - 1:
            velocity = ball.get_velocity().on_brick_hit()
            return ball.set_velocity(velocity)

        if ball_pos.get_x() == constants.MAX_X - 1 or ball_pos.get_x() == 1:
            velocity = ball.get_velocity().on_wall_hit()
            return ball.set_velocity(velocity)

        if ball_pos.get_y() == constants.MAX_Y - 1:
            print('Loser')
            sys.exit()