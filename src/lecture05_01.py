import numpy as np
import cv2
import sys
import os

# --- VSCodeでのインポートエラー解決 ---
# このファイル(src/lecture05_01.py)の絶対パスを取得
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 'src'フォルダの親であるプロジェクトルートのパスを取得
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
# Pythonがモジュールを探すパスのリストにプロジェクトルートを追加
sys.path.append(PROJECT_ROOT)
# ------------------------------------

# プロジェクトルートがパスに追加されたため、'my_module'から正しくインポートできる
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    """
    カメラで画像をキャプチャし、'google.png'の白色部分に合成して保存する関数。
    (リサイズせず、繰り返し（タイリング）で合成するバージョン)
    """
    
    # === 1. ファイルパスの設定 (README.mdの構成に従う) ===
    # 元となる画像
    base_image_path = 'images/google.png'
    # キャプチャ画像を一時的に保存するパス
    captured_image_path = 'output_images/camera_capture.png'
    # 最終的な合成画像の保存パス
    output_image_path = 'output_images/composite_image.png'

    # === 2. カメラキャプチャの実行 ===
    print("カメラキャプチャを開始します...'q'キーで撮影して終了します。")
    app = MyVideoCapture()
    app.run() # Webカメラが起動し、'q'が押されるまでループ

    # 'q'が押された後、画像をファイルに保存 (MyVideoCaptureクラスの仕様)
    app.write_img(captured_image_path)
    print(f"'{captured_image_path}' にキャプチャ画像を保存しました。")


    # === 3. 画像の読み込み ===
    # ベースとなる画像（例: google.png）を読み込む
    google_img = cv2.imread(base_image_path)
    if google_img is None:
        print(f"エラー: ベース画像 '{base_image_path}' を読み込めません。")
        return

    # カメラでキャプチャして保存した画像を読み込む
    capture_img = cv2.imread(captured_image_path)
    if capture_img is None:
        print(f"エラー: キャプチャ画像 '{captured_image_path}' を読み込めません。")
        return

    print(f"ベース画像 サイズ: {google_img.shape}")
    print(f"キャプチャ画像 サイズ: {capture_img.shape}")


    # === 4. 画像の合成 (繰り返しバージョン) ===
    
    # 合成処理のために、両方の画像のサイズを取得
    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape
    
    print("画像の合成処理（繰り返し）を開始します...")
    
    # google_img の全ピクセルをチェック
    for x in range(g_width):
        for y in range(g_height):
            # (B, G, R) の順でピクセル値を取得
            b, g, r = google_img[y, x]
            
            # もしピクセルが純粋な白 (255, 255, 255) だったら
            if (b, g, r) == (255, 255, 255):
                
                # === 'capture_img' を繰り返すための座標計算 ===
                # google_imgの座標(y, x)に対応するcapture_imgの座標を
                # '%' (モジュロ演算子) を使って計算する
                capture_y = y % c_height
                capture_x = x % c_width
                # ----------------------------------------
                
                # キャプチャ画像の (capture_y, capture_x) のピクセルで置き換える
                google_img[y, x] = capture_img[capture_y, capture_x]

    print("画像の合成処理が完了しました。")

    # === 5. 書き込み処理 (implement me の実装) ===
    # 合成後の画像をファイルに保存
    try:
        cv2.imwrite(output_image_path, google_img)
        print(f"合成画像を '{output_image_path}' に保存しました。")
    except Exception as e:
        print(f"合成画像の保存に失敗しました: {e}")