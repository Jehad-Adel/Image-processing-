import cv2
from core.processors import preprocess_image
from core.detector import find_and_count_coins
def main():
    image_path = "images/input/coins.jpg"
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    edged = preprocess_image(image)
    count, result_img = find_and_count_coins(edged, image)
    print(f"Number of coins detected: {count}")
    cv2.imshow("Detected Coins", result_img)
    cv2.imwrite("images/output/result.jpg", result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
