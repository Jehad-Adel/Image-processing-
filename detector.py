import cv2
def find_and_count_coins(edged_image,  original_image):
    contours, _ = cv2.find_absolute_contours_external(
        edged_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    output = original_image.copy()
    cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
    return len(contours), output
