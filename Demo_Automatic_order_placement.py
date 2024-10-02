import pyautogui
import time
from pynput import keyboard

# 初始化 A1 到 A8 的變數
A1 = None
A2 = None
A3 = None
A4 = None
A5 = None
A6 = None
A7 = None
A8 = None

def on_press(key):
    global A1, A2, A3, A4, A5, A6, A7, A8
    try:
        if key.char == '1':
            # 記錄 A1 點的位置
            A1 = pyautogui.position()
            x, y = A1
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            # 擷取以 A1 為中心的區域截圖
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A1.png')
            print(f"A1 設定在位置 {A1}，並已保存截圖為 A1.png")
        elif key.char == '2':
            # 記錄 A2 點的位置
            A2 = pyautogui.position()
            x, y = A2
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A2.png')
            print(f"A2 設定在位置 {A2}，並已保存截圖為 A2.png")
        elif key.char == '3':
            # 記錄 A3 點的位置
            A3 = pyautogui.position()
            x, y = A3
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A3.png')
            print(f"A3 設定在位置 {A3}，並已保存截圖為 A3.png")
        elif key.char == '4':
            # 記錄 A4 點的位置
            A4 = pyautogui.position()
            x, y = A4
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A4.png')
            print(f"A4 設定在位置 {A4}，並已保存截圖為 A4.png")
        elif key.char == '5':
            # 記錄 A5 點的位置
            A5 = pyautogui.position()
            x, y = A5
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A5.png')
            print(f"A5 設定在位置 {A5}，並已保存截圖為 A5.png")
        elif key.char == '6':
            # 記錄 A6 點的位置
            A6 = pyautogui.position()
            x, y = A6
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A6.png')
            print(f"A6 設定在位置 {A6}，並已保存截圖為 A6.png")
        elif key.char == '7':
            # 記錄 A7 點的位置
            A7 = pyautogui.position()
            x, y = A7
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A7.png')
            print(f"A7 設定在位置 {A7}，並已保存截圖為 A7.png")
        elif key.char == '8':
            # 記錄 A8 點的位置
            A8 = pyautogui.position()
            x, y = A8
            left = x - 50
            top = y - 50
            width = 100
            height = 100
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('A8.png')
            print(f"A8 設定在位置 {A8}，並已保存截圖為 A8.png")
        elif key.char == 'c':
            # 確認所有點都已設定
            if None not in (A1, A2, A3, A4, A5, A6, A7, A8):
                # 移動到 A1 點並點擊
                print("移動到 A1 點並點擊...")
                pyautogui.moveTo(A1[0], A1[1], duration=1)
                pyautogui.click()
                print("在 A1 點等待 3 秒...")
                time.sleep(3)
                # 移動到 A3 點並點擊，輸入 "10"
                print("移動到 A3 點並點擊...")
                pyautogui.moveTo(A3[0], A3[1], duration=1)
                pyautogui.click()
                pyautogui.typewrite("10")
                print("已在 A3 點輸入 '10'")
                print("等待 3 秒...")
                time.sleep(3)
                # 移動到 A4 點並點擊，輸入 "TSM"
                print("移動到 A4 點並點擊...")
                pyautogui.moveTo(A4[0], A4[1], duration=1)
                pyautogui.click()
                pyautogui.typewrite("TSM")
                print("已在 A4 點輸入 'TSM'")
                # 按下 "Tab" 鍵兩次
                print("按下 'Tab' 鍵兩次...")
                pyautogui.press('tab', presses=2, interval=0.25)
                # 按下 "Down" 鍵四次
                print("按下 'Down' 鍵四次...")
                pyautogui.press('down', presses=4, interval=0.25)
                # 按下 "Tab" 鍵
                print("按下 'Tab' 鍵...")
                pyautogui.press('tab')
                # 輸入 "0.05"
                print("輸入 '0.05'...")
                pyautogui.typewrite("0.05")
                # 按下 "Tab" 鍵
                print("按下 'Tab' 鍵...")
                pyautogui.press('tab')
                # 按下 "Down" 鍵
                print("按下 'Down' 鍵...")
                pyautogui.press('down')
                # 搜尋並點擊 "Confirm_order.png"
                print("搜尋 'Confirm_order.png' 並點擊...")
                location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
                if location is not None:
                    x, y = pyautogui.center(location)
                    print(f"找到 'Confirm_order.png' 在位置 ({x}, {y})，正在點擊...")
                    pyautogui.moveTo(x, y, duration=1)
                    pyautogui.click()
                else:
                    print("未找到 'Confirm_order.png'，請確認圖檔存在且螢幕上顯示該圖案。")
            else:
                print("請確保所有點 A1 至 A8 都已設定。")
        elif key.char == 'q':
            # 結束程式
            print("結束程式。")
            return False  # 停止監聽器
    except AttributeError:
        # 處理特殊按鍵
        pass

# 啟動鍵盤監聽器
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
