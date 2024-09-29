# (1) 安裝 python3-venv，以便創建虛擬環境：
sudo apt install python3-venv
# (2) 創建虛擬環境：
# 在專案目錄中創建一個虛擬環境來隔離套件，假設目錄名稱為 myenv：
python3 -m venv myenv
# (3) 啟動虛擬環境：
#     啟動後，會發現命令提示符前面會多一個 (myenv)，表示已進入虛擬環境。
source myenv/bin/activate
# (4) 使用 pip 安裝 pyautogui：
#     這樣安裝的 pyautogui 只會在這個虛擬環境內可用，不會影響系統全域套件。
pip install pyautogui
# (5) 測試安裝是否成功：
python -c "import pyautogui; print(pyautogui)"



