import pyautogui
import time

def move_mouse_to_center_then_origin():
    # 取得螢幕的寬度和高度
    screen_width, screen_height = pyautogui.size()

    # 計算螢幕中央的位置
    center_x = screen_width // 2
    center_y = screen_height // 2

    # 將滑鼠移動到螢幕中央
    pyautogui.moveTo(center_x, center_y, duration=1)  # 1秒內移動到螢幕中央
    print(f"滑鼠已移動到螢幕中央: ({center_x}, {center_y})")
    
    # 暫停1秒
    time.sleep(1)

    # 緩慢將滑鼠移動回螢幕左上角（原點 0, 0）
    pyautogui.moveTo(0, 0, duration=5)  # 5秒內緩慢移動回原點
    print("滑鼠已緩慢移動回原點 (0, 0)")

if __name__ == "__main__":
    move_mouse_to_center_then_origin()

