import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import concurrent.futures
import multiprocessing
import time
import telegram
import asyncio
import nest_asyncio

# Jupyter Notebook'un event loop'unu iç içe yerleştirme
nest_asyncio.apply()

# Telegram bot tokenınızı ve chat ID'nizi ekleyin
bot_token = "YOUR_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

async def send_telegram_message(message):
    """Telegram API ile mesaj gönderir."""
    try:
        bot = telegram.Bot(token=bot_token)
        await bot.sendMessage(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Telegram mesajı gönderilirken hata oluştu: {e}")

def fetch_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except Exception as e:
        print(f"Hata: {e}")
        return None

def process_url(url):
    try:
        soup = fetch_url(url)
        if soup:
            mesaj_sayisi_elementi = soup.find('li', {'title': 'Mesaj'})
            if mesaj_sayisi_elementi:
                mesaj_sayisi_raw = mesaj_sayisi_elementi.get_text(strip=True)
                mesaj_sayisi = ''.join(filter(str.isdigit, mesaj_sayisi_raw))
                mesaj_sayisi = int(mesaj_sayisi)
                if mesaj_sayisi > 10:
                    sayfa_sayisi = mesaj_sayisi // 10 + 1
                    with open('/content/yeniurl.txt', 'a') as yeni_url_file:
                        yeni_url_file.write(f"{url}\n")
                    for sayfa in range(2, sayfa_sayisi + 1):
                        yeni_url = f"{url}page-{sayfa}"
                        with open('/content/yeniurl.txt', 'a') as yeni_url_file:
                            yeni_url_file.write(f"{yeni_url}\n")
                else:
                    with open('/content/yeniurl.txt', 'a') as yeni_url_file:
                        yeni_url_file.write(f"{url}\n")

                with open('/content/logyeni.txt', 'a') as output_file:
                    output_file.write(f"{url}: {mesaj_sayisi}\n")
            else:
                with open('/content/logyeni.txt', 'a') as output_file:
                    output_file.write(f"{url}: Mesaj sayısı bulunamadı\n")
    except Exception as e:
        with open('/content/logyeni.txt', 'a') as output_file:
            output_file.write(f"{url}: Hata - {str(e)}\n")

async def main():
    urls = []
    with open('/content/urlss.txt', 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]

    start_time = time.time()
    processed_urls = 0
    total_urls = len(urls)

    with concurrent.futures.ProcessPoolExecutor(max_workers=5 * multiprocessing.cpu_count()) as executor:
        for _ in tqdm(executor.map(process_url, urls), total=total_urls):
            processed_urls += 1
            elapsed_time = time.time() - start_time
            if elapsed_time >= 600:  # 10 dakika (600 saniye)
                message = f"İlerleme: {processed_urls}/{total_urls}"
                await send_telegram_message(message)
                start_time = time.time()  # Zamanlayıcıyı sıfırla

if __name__ == "__main__":
    asyncio.run(main())
