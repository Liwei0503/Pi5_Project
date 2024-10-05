#platform test code : webhook_ngrok_server_v05_1.py  (20241006)
import json
import threading
import queue
import pynput
import pyautogui
import time
from flask import Flask, request

app = Flask(__name__)
event_queue = queue.Queue()

# 初始化位置變數
positions = {'A0': None, 'A1': None, 'A2': None, 'A3': None, 'A4': None, 
             'A5': None, 'A6': None, 'A7': None, 'A8': None, 'A9': None}

# 儲存位置到 JSON 檔案
def save_positions():
    with open('positions.json', 'w') as f:
        json.dump(positions, f)
    print("當前位置已保存到 positions.json")

# 從 JSON 檔案讀取位置
def load_positions():
    global positions
    try:
        with open('positions.json', 'r') as f:
            positions = json.load(f)
        print("已從 positions.json 讀取位置")
    except FileNotFoundError:
        print("無法找到 positions.json 檔案")

# webhook 處理程式
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"接收到封包: {json.dumps(data, indent=4)}")
    event_queue.put(data)
    return 'Received', 200

# 多執行緒監聽鍵盤事件
def on_press(key):
    try:
        if key.char == 't':
            save_positions()  # 按下 't' 鍵時儲存位置
        elif key.char == 'r':
            load_positions()  # 按下 'r' 鍵時讀取位置
        elif key.char == 'b':
            perform_buy_sequence()  # 執行購買流程
        elif key.char == 's':
            perform_sell_sequence()  # 執行賣出流程
        elif key.char == 'q':
            return False  # 停止伺服器
    except AttributeError:
        pass

# 執行購買流程
def perform_buy_sequence():
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
        pyautogui.press('pageup',5)
        pyautogui.click(positions['A0'])
        pyautogui.press('pageup',5)
        time.sleep(1.5)
        
        pyautogui.moveTo(positions['A1'])
        pyautogui.click()
        pyautogui.press('tab')
        pyautogui.write('1')
        pyautogui.press('tab')
        pyautogui.write('TQQQ')
        time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.5)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.write('0.05')
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.5)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
            pyautogui.moveTo(confirm_location)
            pyautogui.click()
        else:
            print("無法找到確認按鈕")
# 執行購買流程(json)
def perform_buy_sequence_json(mystock,mystock_size):
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
        pyautogui.press('pageup',5) 
        pyautogui.click(positions['A0'])
        pyautogui.press('pageup',5)         
        time.sleep(1.5)

        pyautogui.click(positions['A1'])
        pyautogui.press('tab')
        #pyautogui.write('1')
        pyautogui.write(mystock_size)
        pyautogui.press('tab')
        #pyautogui.write('TSM')
        pyautogui.write(mystock)
        time.sleep(0.25)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.5)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.15)
        pyautogui.press('tab')
        pyautogui.write('0.05')
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.5)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
            pyautogui.moveTo(confirm_location)
            pyautogui.click()
        else:
            print("無法找到確認按鈕")
            
# 執行賣出流程
def perform_sell_sequence():
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
        pyautogui.press('pageup',5)    
        pyautogui.click(positions['A0'])
        pyautogui.press('pageup',5)              
        time.sleep(1.5)
        
        pyautogui.moveTo(positions['A2'])
        pyautogui.click()
        pyautogui.press('tab')
        time.sleep(0.1)          # Liwei   
        pyautogui.write('1')
        time.sleep(0.1)          # Liwei         
        pyautogui.press('tab')
        time.sleep(0.1)          # Liwei            
        pyautogui.write('TSM')
        time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.5)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.write('0.05')
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.5)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
            pyautogui.moveTo(confirm_location)
            pyautogui.click()
        else:
            print("無法找到確認按鈕")

# 執行賣出流程(json)
def perform_sell_sequence_json(mystock,mystock_size):
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
        pyautogui.press('pageup',5)          
        pyautogui.click(positions['A0'])
        pyautogui.press('pageup',5)      
        time.sleep(1.5)
        pyautogui.click(positions['A2'])
        pyautogui.press('tab')
        time.sleep(0.1)          # Liwei   
       # pyautogui.write('1')
        pyautogui.write(mystock_size)
        time.sleep(0.1)          # Liwei         
        pyautogui.press('tab')
        time.sleep(0.1)          # Liwei            
       # pyautogui.write('TSM')
        pyautogui.write(mystock)       
        time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.5)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.write('0.05')
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.5)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
            pyautogui.moveTo(confirm_location)
            pyautogui.click()
        else:
            print("無法找到確認按鈕")

# 監聽封包隊列並處理
def process_webhook_data():
    while True:
        data = event_queue.get()
        if data['side'] == 'buy':
            perform_buy_sequence_json(data['pair'],data['size'])
        elif data['side'] == 'sell':
            perform_sell_sequence_json(data['pair'],data['size'])

if __name__ == "__main__":
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()

    threading.Thread(target=process_webhook_data, daemon=True).start()

    app.run(port=5000)
