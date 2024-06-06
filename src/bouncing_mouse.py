import win32api, win32con, time

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

SHIFT = 0x10
ESC = 0x1B

x = 100
y = 100

directionX = 1
directionY = 1


def shouldStop():
  return win32api.GetAsyncKeyState(SHIFT) or win32api.GetAsyncKeyState(ESC)

while True:
  if shouldStop():
    break
  
  if x >= SCREEN_WIDTH or x <= 0:
      directionX = -directionX
  if y >= SCREEN_HEIGHT or y <= 0:
      directionY = -directionY

  x = x + directionX
  y = y + directionY

  win32api.SetCursorPos((x, y))
  time.sleep(1/100)
