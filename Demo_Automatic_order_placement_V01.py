import pyautogui
import json
import time
from pynput import keyboard

# 設定 A1 到 A8 的座標
points = {'A1': None, 'A2': None, 'A3': None, 'A4': None, 'A5': None, 'A6': None, 'A7': None, 'A8': None}

# 記錄座標並存檔區域圖片
def save_image(point_name):
    x, y = pyautogui.position()
    points[point_name] = (x, y)
    screenshot = pyautogui.screenshot(region=(x-50, y-50, 100, 100))
    screenshot.save(f'{point_name}_screenshot.png')
    print(f'{point_name} 位置: {x}, {y} 已存檔')

# 儲存座標為 JSON 檔案
def save_coordinates():
    with open('points.json', 'w') as f:
        json.dump(points, f)
    print("座標已儲存至 points.json")

# 從 JSON 檔案讀取座標
def load_coordinates():
    global points
    try:
        with open('points.json', 'r') as f:
            points = json.load(f)
        print("座標已載入")
    except FileNotFoundError:
        print("未找到 points.json 檔案")
# 
# # 自動滑鼠移動並執行操作
# def execute_sequence(start_point):
#     if all(points.values()):
#         pyautogui.moveTo(points[start_point], duration=1)
#         pyautogui.click()
#         time.sleep(3)
#         pyautogui.moveTo(points['A3'], duration=1)
#         pyautogui.click()
#         pyautogui.write('1')
#         time.sleep(3)
#         pyautogui.moveTo(points['A4'], duration=1)
#         pyautogui.click()
#         pyautogui.write('TQQQ')
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         for _ in range(4):
#             pyautogui.press('down')
#         pyautogui.press('tab')
#         pyautogui.write('0.05')
#         pyautogui.press('tab')
#         pyautogui.press('down')
#         confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
#         if confirm_location:
#             pyautogui.click(confirm_location)
#         print(f'{start_point} 操作已執行完成')


# 自動滑鼠移動並執行操作
def execute_sequence(start_point):
    if all(points.values()):
        pyautogui.moveTo(705, 257, duration=1)
        pyautogui.click()
        time.sleep(2)        
        
        
        pyautogui.moveTo(points[start_point], duration=1)
        pyautogui.click()
        time.sleep(1)
#         pyautogui.moveTo(points['A3'], duration=1)
#         pyautogui.click()
        pyautogui.press('tab')
        pyautogui.write('1')
        time.sleep(1)
#        pyautogui.moveTo(points['A4'],  pyautogui.press('tab'))
        pyautogui.press('tab')
#        pyautogui.click()
        pyautogui.write('TQQQ')
        pyautogui.press('tab')
        pyautogui.press('tab')
        for _ in range(4):
            pyautogui.press('down',1)
        pyautogui.press('tab')
        pyautogui.write('0.05')
        pyautogui.press('tab')
        #pyautogui.press('down')
#         confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
#         if confirm_location:
#             pyautogui.click(confirm_location)

        pyautogui.moveTo(points['A8'], duration=1)
        pyautogui.click()
        print(f'{start_point} 操作已執行完成')

# 偵測鍵盤輸入
def on_press(key):
    try:
        if key.char == '1':
            save_image('A1')
        elif key.char == '2':
            save_image('A2')
        elif key.char == '3':
            save_image('A3')
        elif key.char == '4':
            save_image('A4')
        elif key.char == '5':
            save_image('A5')
        elif key.char == '6':
            save_image('A6')
        elif key.char == '7':
            save_image('A7')
        elif key.char == '8':
            save_image('A8')
        elif key.char == 't':
            save_coordinates()
        elif key.char == 'r':
            load_coordinates()
        elif key.char == 'b':
            points['A1'] = (364, 546)
            points['A8'] = (1233, 836)  #TQQQ
          #  points['A8'] = (1233, 809)   #TSM
            execute_sequence('A1')            
        elif key.char == 's':
            points['A2'] = (365, 571)
            points['A8'] = (1233, 836)  # TQQQ
          #  points['A8'] = (1233, 809)   # TSM
            execute_sequence('A2')
        elif key.char == 'q':
            print("程式結束")
            return False  # 結束程式
    except AttributeError:
        pass

# 啟動鍵盤監聽
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
