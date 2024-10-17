# webhook_ngrok_server_v05_7.py

import json
import requests
import threading
import queue
import pynput
import pyautogui
import time
from flask import Flask, request

# 用於存儲 SCREEN1 和 SCREEN2 座標
screen1 = None
screen2 = None

# 獲取螢幕解析度
screen_width, screen_height = pyautogui.size()

app = Flask(__name__)
event_queue = queue.Queue()

# 初始化位置變數
positions = {'A0': None, 'A1': None, 'A2': None, 'A3': None, 'A4': None, 
             'A5': None, 'A6': None, 'A7': None, 'A8': None, 'A9': None}

# 讀取文字檔中的網址列表
def load_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

# 將收到的 JSON 資料轉發至指定網址
def forward_payload(urls, payload):
    # 設置請求的 headers，加入 'Accept' 標頭，並確保 'Content-Type' 為 'application/json'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        # 若某些 API 需要授權，這裡可以添加 API key 或 token
        # 'Authorization': 'Bearer YOUR_API_KEY'
    }
    for url in urls:
        try:
            # 發送 POST 請求，並打印回應狀態碼
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print(f"Sent payload to {url}, Status code: {response.status_code}")
            print(f"轉傳封包: {json.dumps(payload, indent=4)}")
        except Exception as e:
            print(f"Error sending payload to {url}: {e}")


# 儲存圖片的函數
def save_screenshot(x1, y1, x2, y2):
    # 確保截圖區域在螢幕範圍內
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(screen_width, x2), min(screen_height, y2)
    
    if x1 == x2 or y1 == y2:
        print("無效的截圖區域，寬度或高度為 0")
        return
    
    region = (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    try:
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save('screenshot.png')
        print(f"已保存截圖到 'screenshot.png'，區域: {region}")
    except Exception as e:
        print(f"截圖過程中發生錯誤: {e}")

# 尋找圖像中心點座標並儲存到 JSON 檔案
def find_image_center_and_save(image_path):
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        if location:
            center = pyautogui.center(location)
            # 將 numpy.int64 轉換為標準的 int
            center_x, center_y = int(center[0]), int(center[1])
            print(f"找到 {image_path} 的中心點座標: ({center_x}, {center_y})")
            # 將座標儲存到 JSON 檔案
            with open('image_location.json', 'w') as f:
                json.dump({"image_center": {"x": center_x, "y": center_y}}, f)
            print(f"已將中心點座標儲存到 'image_location.json'")
        else:
            print(f"無法找到 {image_path} 圖像")
    except Exception as e:
        print(f"尋找圖像過程中發生錯誤: {e}")
        

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
        
# 將接收到的 JSON 封包寫入檔案
def log_webhook_data(data):
    with open('webhook_log.txt', 'a') as f:
        f.write(json.dumps(data, indent=4))
        f.write('\n\n')  # 每個封包後增加一個空行，讓日誌更易讀

# webhook 處理程式
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"接收到封包: {json.dumps(data, indent=4)}")
    urls = load_urls('urls.txt')
    forward_payload(urls, data)    

# 將封包存入日誌檔案
    log_webhook_data(data)
    
    event_queue.put(data)
    return 'Received', 200

# 多執行緒監聽鍵盤事件
def on_press(key):

    global screen1, screen2  # 明確宣告要使用全局變數

    try:
        if key.char == '!':
            save_positions()  # 按下 '!' 鍵時儲存位置
        elif key.char == '*':
            load_positions()  # 按下 '*' 鍵時讀取位置
#        elif key.char == 'b':
#            perform_buy_sequence()  # 執行購買流程
#        elif key.char == 's':
#            perform_sell_sequence()  # 執行賣出流程
        elif key.char == '/':
            return False  # 停止伺服器
        elif key.char == '+':  # 儲存 SCREEN1 座標
            screen1 = pyautogui.position()
            print(f"SCREEN1座標已儲存: {screen1}")
        elif key.char == '-':  # 儲存 SCREEN2 座標
            screen2 = pyautogui.position()
            print(f"SCREEN2座標已儲存: {screen2}")
            # 當 SCREEN1 和 SCREEN2 座標都已設定時儲存圖片
            if screen1 is not None and screen2 is not None:
                print(f"將從 {screen1} 到 {screen2} 進行截圖")
                save_screenshot(screen1[0], screen1[1], screen2[0], screen2[1])
                screen1, screen2 = None, None  # 重置座標
        elif key.char == '?':  # 尋找並顯示圖像中心點座標
            find_image_center_and_save('find_webform.png')                
    except AttributeError:
        pass
    except Exception as e:
        print(f"按鍵處理過程中發生錯誤: {e}")        

# 執行購買流程
def perform_buy_sequence():
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
#        pyautogui.click(positions['A0'])    
#        pyautogui.press('pageup',5)
        pyautogui.click(positions['A0'])
        pyautogui.press('pageup',5)
        time.sleep(3.5)
        
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
            time.sleep(1.5)
            pyautogui.click(positions['A0'])            
        else:
            print("無法找到確認按鈕")
# 執行購買流程(json)
def perform_buy_sequence_json(mystock,mystock_size):
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
#        pyautogui.moveTo(positions['A0'])        
#        pyautogui.press('pageup',5) 
        pyautogui.click(positions['A0'])
#        pyautogui.press('pageup',5)         
        time.sleep(1.5)            #time.sleep(3.5)

        pyautogui.click(positions['A1'])
        pyautogui.press('tab')
        time.sleep(0.05)          # Liwei           
        #pyautogui.write('1')
        pyautogui.write(mystock_size)
        time.sleep(0.1)        
        pyautogui.press('tab')
        time.sleep(0.1)
        #pyautogui.write('TSM')
        pyautogui.write(mystock)
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.write('0.05')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.1)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
#            pyautogui.moveTo(confirm_location)
            pyautogui.click(confirm_location)  # pyautogui.click()
            time.sleep(1)
#            pyautogui.click(positions['A0'])
#            time.sleep(1)
        else:
            print("無法找到確認按鈕")
            
# 執行賣出流程
def perform_sell_sequence():
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
#        pyautogui.moveTo(positions['A0'])    
#        pyautogui.press('pageup',5)    
        pyautogui.click(positions['A0'])
        pyautogui.press('pageup',5)              
        time.sleep(1.5)
        
        pyautogui.moveTo(positions['A2'])
        pyautogui.click()
        pyautogui.press('tab')
        time.sleep(0.05)          # Liwei   
        pyautogui.write('1')
        time.sleep(0.1)          # Liwei         
        pyautogui.press('tab')
        time.sleep(0.1)          # Liwei            
        pyautogui.write('TSM')
        time.sleep(0.1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(0.1)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.05)
        pyautogui.press('tab')
        pyautogui.write('0.05')
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.1)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
            pyautogui.moveTo(confirm_location)
            pyautogui.click()
        else:
            print("無法找到確認按鈕")

# 執行賣出流程(json)
def perform_sell_sequence_json(mystock,mystock_size):
    if all(positions[f'A{i}'] for i in range(1, 9)):  # 確保 A1 到 A8 都已設定
#        pyautogui.moveTo(positions['A0'])    
#        pyautogui.press('pageup',5)          
        pyautogui.click(positions['A0'])
#        pyautogui.press('pageup',5)      
        time.sleep(1.5)            #time.sleep(3.5)
        pyautogui.click(positions['A2'])
        time.sleep(0.01)          # Liwei           
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
        time.sleep(1)
        for _ in range(4):
            pyautogui.press('down')
            time.sleep(0.05)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.write('0.05')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.5)
        confirm_location = pyautogui.locateOnScreen('Confirm_order.png', confidence=0.8)
        if confirm_location:
#            pyautogui.moveTo(confirm_location)
            pyautogui.click(confirm_location)  # pyautogui.click()
            time.sleep(1)
#            pyautogui.click(positions['A0'])            
#            time.sleep(1)
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
