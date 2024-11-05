import random

class Snake:
  def __init__(self, init_body, init_direction):
    self.body = init_body
    self.direction = init_direction

  def head(self):
    return self.body[-1]
  
  def take_step(self, position):
    self.body = self.body[1:] + [position]

  def set_direction(self, direction):
    self.direction = direction

  def extend_body(self, position):
    self.body.append(position)
    



class Apple:
  def __init__(self, init_position):
    self.position = init_position


class Game:
  UP = (-1, 0)  
  DOWN = (1, 0)
  LEFT = (0, -1)
  RIGHT = (0, 1)

  def __init__(self, width, height):
    self.width = width
    self.height = height

    init_body = [(0, 0),(1, 0),(2, 0),(3, 0),(4, 0)]
    self.snake = Snake(init_body, self.DOWN)

    init_apple = (random.randrange(0, self.height), random.randrange(0, self.width))

    while init_apple in init_body:
      init_apple = (random.randrange(0, self.width), random.randrange(0, self.height))

    self.apple = Apple(init_apple)
    # print(self.apple.position)
    
   


  def play(self):
    self.render()
    while True:
      direct = input().upper()

      if direct == "W" and self.snake.direction != self.DOWN:
        self.snake.set_direction(self.UP)
      if direct == "S" and self.snake.direction != self.UP:
        self.snake.set_direction(self.DOWN)
      if direct == "A" and self.snake.direction != self.RIGHT:
        self.snake.set_direction(self.LEFT)
      if direct == "D" and self.snake.direction != self.LEFT:
        self.snake.set_direction(self.RIGHT)

      next_position = self.next_position(self.snake.head(), self.snake.direction)
      
      # ran into boundaries
      if next_position is None:
        # Game over
        print("Game Over :(")
        break

      # ran into self
      if next_position in self.snake.body:
        # Game over
        print("Game Over :(")
        break
      
      # TODO check if next_position is the apple
      if next_position == self.apple.position:
        self.snake.extend_body(next_position)
        self.regenerate_apple()
        

      self.snake.take_step(next_position)

      self.render()

  def board_matrix(self):
    matrix = []
    for i in range(self.height): # rows
      row = []
      for j in range(self.width): # cols
        if (i, j) in self.snake.body:
          head = self.snake.head()
          if (i, j) == head:
            row.append("X")
          else:
            row.append("O")
        elif (i,j) == self.apple.position:
          row.append("*")
        else:
          row.append(None)
      matrix.append(row)
    return matrix

  def render(self):
    matrix = self.board_matrix()
    print("+" + "-" * self.width + "+")

    for row in matrix:
      line = "|"
      for square in row:
        if square is None:
          line += " "
        else:
          line += str(square)
      line += "|"
      print(line)
    print("+" + "-"* self.width + "+")

  def next_position(self, head, direction):
    next_position = (head[0] + direction[0], head[1] + direction[1])

    # Check if next_position is in bounds
    if 0 <= next_position[0] < self.height and 0 <= next_position[1] < self.width:
        return next_position
    else:
        return None
    
  def regenerate_apple(self):
    new_apple_loc = (random.randrange(0, self.height), random.randrange(0, self.width))

    while new_apple_loc in self.snake.body:
      new_apple_loc = (random.randrange(0, self.height), random.randrange(0, self.width))

    self.apple = Apple(new_apple_loc)



  

game = Game(20, 10)
game.play()
