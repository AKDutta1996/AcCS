import pyautogui

if __name__ == '__main__':

    TaskbarPinnedChromeX, TaskbarPinnedChromeY = 972, 1050
    ChromeAddressBarX, ChromeAddressBarY = 221, 52

    AmazonWebDomain = "https://www.amazon.in/dp/"
    AmazonAsinCode = "B08D11DZ2W"

    ProductLink = AmazonWebDomain + AmazonAsinCode

    pyautogui.click(TaskbarPinnedChromeX, TaskbarPinnedChromeY)
    pyautogui.click(ChromeAddressBarX, ChromeAddressBarY)

    pyautogui.write(ProductLink)
    pyautogui.press('enter')    
