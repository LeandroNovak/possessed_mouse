import win32api, win32con, time, random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SHIFT = 0x10
ESC = 0x1B
Q = 0x51

x = int(SCREEN_WIDTH/2)
y = int(SCREEN_HEIGHT/2)

directionX = 1
directionY = 1

visited = set([])

sleep_time = 10/1000
elapsed_time = 0

def shouldStop():
  return win32api.GetAsyncKeyState(SHIFT) or win32api.GetAsyncKeyState(ESC) or win32api.GetAsyncKeyState(Q)

def selectDirection():
  while(True):
      possible_direction_x = random.randint(-1, 1)
      possible_direction_y = random.randint(-1, 1)

      new_position = (x + possible_direction_x, y + possible_direction_y)
      if(new_position in visited):
        continue
      else:
        visited.add(new_position)
        return (possible_direction_x, possible_direction_y)

while True:
  if shouldStop():
    break
  
  if x >= SCREEN_WIDTH or x <= 0:
    x = 1
    elapsed_time = 1
  if y >= SCREEN_HEIGHT or y <= 0:
    y = 1
    elapsed_time = 1

  if (elapsed_time >= 1):
    new_position = selectDirection()
    directionX = new_position[0]
    directionY = new_position[1]
    elapsed_time = 0

  x = x + directionX
  y = y + directionY

  win32api.SetCursorPos((x, y))

  elapsed_time = elapsed_time + sleep_time
  time.sleep(sleep_time)
