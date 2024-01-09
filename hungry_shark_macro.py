import datetime
import ctypes
import pyautogui


def set_system_date(year, month, day):
    try:
        ctypes.windll.shell32.IsUserAnAdmin()  # Check if script is run as administrator
        ctypes.windll.kernel32.SetLocalTime(year, month, day, 0, 0, 0, 0, 0)
        print(f"System date set to: {month}/{day}/{year}")
    except Exception as e:
        print(f"Error setting system date: {e}")


def main():
    current_date = datetime.date.today()
    new_date = current_date + datetime.timedelta(days=1)

    set_system_date(new_date.year, new_date.month, new_date.day)


if __name__ == "__main__":
    main()




pyautogui.moveTo(1000, 200)
pyautogui.click()
pyautogui.typewrite('Hello, World!')