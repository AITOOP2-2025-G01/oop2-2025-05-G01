import os
import numpy as np
import cv2
from my_module.K24005.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"
    capture_img : cv2.Mat = app.get_img()

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                pass
                #implement me
                # キャプチャ画像内の対応する座標を計算 (グリッド配置のロジック)
                cap_x = x % c_width
                cap_y = y % c_hight
                
                # キャプチャ画像からピクセル値を取得し、Google画像に設定
                google_img[y, x] = capture_img[cap_y, cap_x]
                
                

    # 書き込み処理
    # implement me
    # 出力ディレクトリの準備
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    
    # 学籍番号K24005を指定してファイルを保存
    output_path = os.path.join(output_dir, "lecture05_01_K24005.png")
    cv2.imwrite(output_path, google_img)
    print(f"✅ 出力完了: {output_path}")
    