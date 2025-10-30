import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()


    # 撮影した画像を保存（この時点で保存しておく）
    app.write_img('images/camera_capture.png')


    # 画像をローカル変数に保存
    google_img: cv2.Mat = cv2.imread('images/google.png')
    if google_img is None:
        raise FileNotFoundError("google.png が見つかりません。パスまたはファイル名を確認してください。")

    capture_img: cv2.Mat = cv2.imread('images/camera_capture.png')  # 動作テスト用
    if capture_img is None:
        raise FileNotFoundError("camera_capture.png が見つかりません。出力フォルダを確認してください。")


    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y%c_hight, x%c_width]

    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01_k21003.png', google_img)
    print("lecture05_01_k21003.png を保存しました。")
if __name__ == "__main__":
    lecture05_01()
