## 使用 Python 快速輕鬆地將 HEIC 轉換為 JPG
HEIC 格式是一種由 Apple 推廣的高效圖像格式，它具有更好的壓縮效果和更高的影像品質。但儘管 HEIC 格式在 Apple 設備上廣泛使用，但在其他平台（如 Windows 和 Android）上仍然存在一些兼容性問題，這使得許多用戶在想要分享 HEIC 圖片時感到困擾。

本文將介紹如何使用 Python 編寫一個簡單的程式，將 HEIC 格式的圖片輕鬆快速地轉換為更通用的 JPG 格式。我們將使用 Pillow和 pillow-heif（用於處理 HEIC 的套件）來解決這個問題。而會選擇這個套件的原因，是因為原先想要在windows安裝pyheif，但是發現很多問題導致裝不起來，因此才會改用pillow-heif。

## 運行程式
要使用此程式，請按照以下步驟操作：

1. 確保您已經安裝了 Python 以及 Pillow 和 pillow-heif 庫。
2. 將上述程式保存為名為 heic_to_jpg.py 的文件。
3. 在程式所在的目錄下創建一個名為 image 的文件夾，將您想要轉換的 HEIC 圖片放入該文件夾中。
4. 打開命令列 ( CMD )，進入至程式所在的目錄，然後運行以下命令：

```bash
python heic_to_jpg.py
```

程式將自動尋找 `/image` 文件夾中的所有 HEIC 文件並將其轉換為 JPG 文件。轉換後的 JPG 文件將與源 HEIC 文件位於相同的文件夾中。

## 結論
這次我們介紹如何使用 Python 和 Pillow庫，將 HEIC 圖片轉換為 JPG 格式。這是一個簡單但實用的程式，可以方便地將 HEIC 圖片轉換為更通用的 JPG 格式。如果您有任何問題或想了解更多關於 Python 圖像處理的信息，請隨時在評論區提問！

## 擴展功能
雖然我們在這篇文章中主要關注將 HEIC 轉換為 JPG，但您還可以使用類似的方法將 HEIC 文件轉換為其他圖像格式，如 webp。您還可以使用 Pillow 庫進行更高級的影像處理，例如調整影像大小、應用濾鏡和編輯影像的資料數據等。

更多內容可以參考：[michaelpig](https://michaelpig0912.github.io/)
