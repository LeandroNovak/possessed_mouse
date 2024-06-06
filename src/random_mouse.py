import win32api, win32con, time, random, math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

DIRECTIONS = [1, 0, -1]

SHIFT = 0x10
ESC = 0x1B
Q = 0x51

x = int(SCREEN_WIDTH / 2)
y = int(SCREEN_HEIGHT / 2)

directionX = 1
directionY = 1

sleep_time = 10/1000
elapsed_time = 0

def getKey(key):
  return win32api.GetAsyncKeyState(key)

def shouldStop():
  return getKey(SHIFT) or getKey(ESC) or getKey(Q)

while True:
  if shouldStop():
    break
  
  # check for screen bounds so it doesn't disappear
  if x >= SCREEN_WIDTH or x <= 0:
    directionX = -directionX
    elapsed_time = 0
  if y >= SCREEN_HEIGHT or y <= 0:
    directionY = -directionY
    elapsed_time = 0

  if (elapsed_time >= 1):
    if (random.random() > 0.5):
      directionX = random.randint(-1, 1)
    if (random.random() > 0.5):
      directionY = random.randint(-1, 1)
    elapsed_time = 0

  # avoid stopping
  if (directionX == 0 and directionY == 0):
    elapsed_time = 1
    continue

  x = x + directionX
  y = y + directionY

  win32api.SetCursorPos((x, y))

  elapsed_time = elapsed_time + sleep_time
  time.sleep(10/1000)

