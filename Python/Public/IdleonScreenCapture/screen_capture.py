from PIL import ImageGrab
import cv2
import numpy as np

def capture_screen(region=None):
    """
    Captures a screenshot of the specified region.
    :param region: A tuple of (x, y, width, height) that specifies the capture area.
    :return: A PIL image of the captured area.
    """
    screenshot = ImageGrab.grab(bbox=region)
    screenshot.save("screenshot.png")
    return screenshot

def find_template_in_screenshot(screenshot, template, threshold=0.8):
    """
    This function finds the template image in the screenshot.
    :param screenshot: The screenshot image in which to search for the template.
    :param template: The template image to find.
    :param threshold: The threshold for matching the template.
    :return: The top-left corner coordinates of the template in the screenshot.
    """
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(np.array(template), cv2.COLOR_BGR2GRAY)

    # Use template matching to find the template in the screenshot
    res = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Find where the match exceeds the threshold
    loc = np.where(res >= threshold)

    # Assuming the highest value is the best match, return the first one
    if loc[0].size > 0 and loc[1].size > 0:
        pt = loc[::-1][0][0], loc[::-1][1][0]
        return pt
    else:
        return None

# You will need to load or define your templates somewhere in your code
fish_template = cv2.imread('fish.png')
power_bar_template = cv2.imread('power_bar.png')
region_to_capture = (0, 0, 800, 600)

# Assuming you have a screenshot
screenshot = capture_screen(region=region_to_capture)

# Find the fish
fish_position = find_template_in_screenshot(screenshot, fish_template)
# Find the power bar
power_bar_position = find_template_in_screenshot(screenshot, power_bar_template)
screenshot.show()

print(fish_position)
print(power_bar_position)
