import httpx
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import multiprocessing
import time

# URL'leri içeren txt dosyasının yolunu belirtin
file_path = '/content/url.txt'

# URL'leri txt dosyasından okuyun
with open(file_path, 'r') as file:
    url_list = [line.strip() for line in file if line.strip()]

disclaimer = "'zynp_msgdata' veri seti 'sekerlipencere' tarafından hazırlanmıştır."
cpu_count = multiprocessing.cpu_count()
max_workers = cpu_count * 300  # İşlemci çekirdek sayısının 20 katı kadar iş parçacığı oluştur

def fetch_content(url):
    try:
        with httpx.Client(timeout=5) as client:
            response = client.get(url)
            response.raise_for_status()
            return url, response.text
    except Exception as e:
        print(f"URL alınamadı: {url} - Hata: {e}")
        return url, None

def process_content(url_content):
    url, webpage = url_content
    if webpage is None:
        return None

    try:
        soup = BeautifulSoup(webpage, 'html.parser')
        soru_div = soup.find('div', class_='p-title')
        if soru_div:
            soru = soru_div.get_text(strip=True)
            ayrintili_soru_div = soup.find('div', class_='bbWrapper')
            ayrintili_soru = ayrintili_soru_div.get_text(strip=True) if ayrintili_soru_div else ''
            cevap_divs = soup.find_all('div', class_='bbWrapper')[1:]
            cevaplar = [cevap.get_text(strip=True) for cevap in cevap_divs]
            return {
                'soru': soru,
                'url': url,
                'ayrintili_soru': ayrintili_soru,
                'cevaplar': cevaplar,
                'atıf': disclaimer
            }
    except Exception as e:
        print(f"İçerik işlenirken hata oluştu: {url} - Hata: {e}")
        return None

def write_to_json(result):
    if result:
        with open('sonuc.json', 'a', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
            f.write('\n')

def main():
    batch_size = 500  # Toplu işleme için isteklerin gruplanacağı boyut
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(0, len(url_list), batch_size):
            batch_urls = url_list[i:i+batch_size]
            futures = [executor.submit(fetch_content, url) for url in batch_urls]
            with tqdm(total=len(futures), desc="Toplam İşleniyor", unit="URL") as pbar:
                for future in as_completed(futures):
                    url_content = future.result()
                    result = process_content(url_content)
                    write_to_json(result)
                    pbar.update(1)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Toplam süre: {end_time - start_time:.2f} saniye")
