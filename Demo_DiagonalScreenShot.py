import pyautogui
from PIL import ImageGrab
from pynput import keyboard

# 全域變數來儲存 A 和 B 位置
A_position = None
B_position = None
file_counter = 1
program_running = True  # 控制程式是否運行

def save_screenshot(A, B):
    global file_counter
    # 計算 A 和 B 之間的矩形區域
    left = min(A[0], B[0])
    top = min(A[1], B[1])
    right = max(A[0], B[0])
    bottom = max(A[1], B[1])

    # 截取螢幕指定區域
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # 儲存螢幕截圖並附上序號
    screenshot_name = f"screenshot_{file_counter}.png"
    screenshot.save(screenshot_name)
    print(f"已將螢幕區域儲存為 {screenshot_name}")

    # 序號遞增
    file_counter += 1

def on_press(key):
    global A_position, B_position, program_running

    try:
        if key.char == 'z':
            # 按下 'z'，記錄 A 位置
            A_position = pyautogui.position()
            print(f"A 位置已記錄: {A_position}")

        elif key.char == 'x':
            # 按下 'x'，記錄 B 位置
            B_position = pyautogui.position()
            print(f"B 位置已記錄: {B_position}")

        elif key.char == 'c':
            # 按下 'c'，當 A 和 B 都被記錄後，進行截圖
            if A_position and B_position:
                print(f"A 位置: {A_position}, B 位置: {B_position}，開始截圖...")
                save_screenshot(A_position, B_position)
            else:
                print("請先記錄 A 和 B 位置")

        elif key.char == 'q':
            # 按下 'q' 結束程式
            print("按下 'q'，程式結束。")
            program_running = False
            return False  # 結束監聽
    except AttributeError:
        pass  # 忽略特殊按鍵

def main():
    print("請使用 'z' 記錄 A 位置，'x' 記錄 B 位置，'c' 進行截圖，'q' 結束程式。")

    # 啟動鍵盤監聽
    with keyboard.Listener(on_press=on_press) as listener:
        while program_running:
            listener.join()

if __name__ == "__main__":
    main()
