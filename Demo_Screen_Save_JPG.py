import pyautogui
from PIL import Image

# 擷取螢幕的特定區域並存儲為 JPG 檔案
def capture_screen_area(left, top, width, height, output_filename):
    # 擷取螢幕特定區域
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # 儲存為 JPG 檔案
    screenshot = screenshot.convert("RGB")  # 轉換為 RGB 模式以保存 JPG
    screenshot.save(output_filename, "JPEG")
    print(f"圖片已成功保存為 {output_filename}")

# 定義螢幕區域的左上角座標 (left, top) 和區域大小 (width, height)
left = 100
top = 100
width = 300
height = 200

# 定義輸出的 JPG 檔案名稱
output_filename = "captured_area.jpg"

# 擷取螢幕區域並保存為 JPG
capture_screen_area(left, top, width, height, output_filename)
