# Recursive-Nested-ZIP-to-Text-Extractorr / İç İçe ZIP Çıkarıcı

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

A Python script to recursively extract ZIP archives and display the content of the final text file found. / İç içe geçmiş ZIP dosyalarını yinelemeli olarak çıkarır ve en sonunda bulunan metin dosyasının içeriğini gösterir.

## Purpose / Amaç

This script aims to easily access specific text content within complex, multi-layered ZIP archives. It is particularly useful in automated processes or when analyzing deeply packaged data. / Bu betiğin amacı, karmaşık bir yapıya sahip, katmanlarca ZIP dosyası içeren arşivlerden belirli bir metin içeriğine kolayca ulaşmaktır. Özellikle otomatikleştirilmiş süreçlerde veya derinlemesine paketlenmiş verileri analiz etmek gerektiğinde faydalıdır.

## How to Run / Nasıl Çalıştırılır

1.  **Ensure Python is installed.** (Python 3.x is recommended) / **Python'ın kurulu olduğundan emin olun.** (Python 3.x önerilir)
2.  Save the script file (with `.py` extension). / Betik dosyasını (`.py` uzantılı) kaydedin.
3.  Assign the path of the outermost ZIP file you want to process to the `zip_file_path` variable. / İşlemek istediğiniz en dıştaki ZIP dosyasının yolunu `zip_dosya_yolu` değişkenine atayın.
4.  Assign the path of the directory where extracted files will be saved to the `output_directory` variable. / Çıkarılan dosyaların kaydedileceği dizinin yolunu `cikti_dizini` değişkenine atayın.
5.  Run the script from the command line or a Python development environment: / Komut satırında veya bir Python geliştirme ortamında betiği çalıştırın:

    ```bash
    python your_script_name.py
    ```

    (Replace `your_script_name.py` with the name of your script file.) / (Burada `your_script_name.py` sizin betik dosyanızın adıdır.)

## Requirements / Gereksinimler

* Python 3.x
* `zipfile` library (included in the Python standard library) / `zipfile` kütüphanesi (Python standart kütüphanesinde bulunur)
* `os` library (included in the Python standard library) / `os` kütüphanesi (Python standart kütüphanesinde bulunur)

## Usage / Kullanım

When the script is executed, it opens the specified ZIP file and checks its contents. If it finds another ZIP file inside, it extracts it to the specified output directory and continues this process until it finds a text file (.txt). Finally, it prints the content of the innermost text file to the console. / Betik çalıştırıldığında, belirtilen ZIP dosyasını açar ve içindeki dosyaları kontrol eder. Eğer içinde başka bir ZIP dosyası varsa, onu belirtilen çıktı dizinine çıkarır ve bu işleme, içinde bir metin dosyası (.txt) bulunana kadar devam eder. En sonunda bulunan metin dosyasının içeriği ekrana yazdırılır.

## Example / Örnek

If the `matryoshka.zip` file has the following structure: / Eğer `matryoshka.zip` dosyası şu şekilde bir yapıya sahipse:
