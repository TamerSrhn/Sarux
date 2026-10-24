<div align="center">
  <img src="Saruxpengu.jpg" alt="Sarux penguen maskotu" width="190">
  <h1>SARUX</h1>
  <p><strong>Windows için Türkçe sesli yapay zekâ asistanı</strong></p>
  <p>
    <img src="https://img.shields.io/badge/platform-Windows-3478c7?logo=windows&logoColor=white" alt="Windows">
    <img src="https://img.shields.io/badge/language-Python-3776ab?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/interface-Türkçe-6b7280" alt="Türkçe arayüz">
  </p>
  <p>
    <img src="Saruxpengu.jpg" alt="Sarux dinlerken" width="135">
    &nbsp;&nbsp;
    <img src="saruxpengukonus.jpg" alt="Sarux konuşurken" width="135">
  </p>
  <p><sub>Dinleme ve konuşma durumlarında değişen Sarux maskotu</sub></p>
</div>

---

Sarux; mikrofon üzerinden konuşmayı, yazılı mesaj göndermeyi ve yanıtları arayüzde görmeyi tek bir Windows uygulamasında birleştirir. Sade arayüzünde saat, yaklaşık konum, hava durumu ve bilgisayarın temel sistem bilgileri de gösterilir.

## Neler yapabilir?

- **Sesli sohbet:** Gemini Live üzerinden Türkçe konuşma ve sesli yanıt akışı.
- **Yazılı mesaj:** Mesajını arayüzün sağındaki alana yaz; senin mesajların ve Sarux'un metin yanıtları sohbet geçmişinde görünür.
- **Mikrofon kontrolü:** Mikrofonu istediğin an kapatıp yeniden aç.
- **Uyku ve uyanma:** Dinlemeyi geçici olarak durdurup Sarux'u tekrar etkinleştir.
- **Durum göstergesi:** Dinleme ve konuşma sırasında farklı penguen görselleri kullanılır.
- **Bilgi alanı:** Saat, IP tabanlı yaklaşık konum, hava durumu, CPU, RAM, disk, pil ve çalışma süresi.
- **Araçlar:** Sistem bilgisi, hava durumu, takvim, hatırlatıcılar, uygulama açma, medya ve desteklenen diğer eylemler.
- **Ses ve tercih ayarları:** Desteklenen ses seçenekleri ve uygulama ayarları arayüzden yönetilir.

## Hızlı başlangıç

### Gerekenler

- Windows 10 veya 11
- Python 3.10 veya üzeri
- İnternet bağlantısı
- Gemini API anahtarı
- Sesli kullanım için çalışan mikrofon ve hoparlör

### Kurulum

1. Bu depoyu GitHub'dan indirin veya klonlayın.

   ```powershell
   git clone <depo-adresi>
   cd SaruxAi-Github
   ```

2. `setup.bat` dosyasını çalıştırın. Betik `.venv` adlı sanal ortamı oluşturur, paketleri kurar ve yoksa örnek API ayar dosyasını kopyalar.

3. `config/api_keys.json` dosyasındaki `gemini_api_key` alanına kendi Gemini API anahtarınızı yazın. Örnek dosya `config/api_keys.example.json` olarak depoda bulunur.

   ```json
   {
     "gemini_api_key": "API_ANAHTARINIZI_BURAYA_YAZIN",
     "voice": "Charon"
   }
   ```

4. `SaruxAi.bat` dosyasına çift tıklayarak uygulamayı başlatın. Kaynak kodu elle çalıştırmak için:

   ```powershell
   .\.venv\Scripts\python.exe main.py
   ```

API anahtarını kaynak koda eklemeyin. `.gitignore`, gerçek `config/api_keys.json` dosyasını Git işlemlerinin dışında tutar. İlk açılışta uygulamanın ayar ekranını kullanarak anahtar girebilirsiniz.

## Uygulama kontrolleri

| Düğme | İşlev |
| --- | --- |
| **Mikrofonu Kapat / Aç** | Ses girişini Sarux'a göndermeyi geçici olarak durdurur veya sürdürür. |
| **Sarux'u Uyut / Uyandır** | Asistanın dinlemesini duraklatır veya yeniden başlatır. |
| **Sarux Kapat** | Uygulamayı kapatır. |

`Escape` uygulamayı kapatmaz. Uygulamayı ekrandaki **Sarux Kapat** düğmesiyle veya pencerenin kapatma düğmesiyle kapatın.

## Windows `.exe` oluşturma

Kurulum tamamlandıktan sonra proje klasöründe PowerShell açıp aşağıdaki komutları çalıştırın:

```powershell
.\.venv\Scripts\python.exe -m pip install pyinstaller
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --distpath dist_single --workpath build_single\temp SaruxAi.spec
```

Çıktı `dist_single/SaruxAi.exe` konumunda oluşturulur. `SaruxAi.spec`, penguen görsellerini ve istem metnini pakete ekler. Derleme klasörleri ve `.exe` dosyaları depoya dahil edilmez.

## Proje yapısı

```text
SaruxAi-Github/
├── actions/                  # Hava durumu, sistem bilgisi ve diğer araçlar
├── config/
│   └── api_keys.example.json # Gizli anahtar içermeyen örnek ayarlar
├── core/
│   └── prompt.txt            # Asistanın temel talimatları
├── memory/                   # Yerel hafıza kodu ve boş örnek veriler
├── Saruxpengu.jpg            # Dinleme görseli
├── saruxpengukonus.jpg       # Konuşma görseli
├── main.py                   # Asistan, canlı ses ve araç bağlantıları
├── ui.py                     # Tkinter arayüzü
├── app_config.py             # Yerel ayarların okunması ve kaydedilmesi
├── requirements.txt          # Python bağımlılıkları
├── setup.bat                 # Windows geliştirme kurulumu
├── SaruxAi.bat               # Uygulamayı başlatma kısayolu
└── SaruxAi.spec              # Tek dosyalı Windows paketi
```

## GitHub'da yayımlama

Bu proje için ayrılmış `SaruxAi-Github` klasörünü kullanın. GitHub'daki yükleme sayfasına kaynak dosyalarını ve alt klasörleri yükleyin:

1. GitHub hesabınızda **New repository** seçin ve depo adını belirleyin. Depoyu README, `.gitignore` veya lisans dosyasıyla otomatik başlatmayın; bu dosyalar proje klasöründe zaten bulunur.
2. Yeni deponun ana sayfasında **Add file → Upload files** seçin.
3. Masaüstündeki `SaruxAi-Github` klasörünün içindekileri (alt klasörler dahil) yükleme alanına sürükleyin.
4. **Commit changes** bölümüne `İlk kaynak kodu yüklemesi` gibi bir açıklama yazıp yüklemeyi onaylayın.

Yüklemeden önce `.gitignore` dosyasının bulunduğunu kontrol edin. `config/api_keys.json`, kişisel hafıza dosyaları, `.venv`, derleme klasörleri ve `.exe` depoya eklenmemelidir. GitHub, tarayıcıdan dosya veya klasör yüklemeyi anlatan [resmî yönergelerinde](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) bu adımları açıklar.

## Konum ve gizlilik

Hava durumu için internet gerekir. `SARUX_WEATHER_LOCATION` ortam değişkeni ayarlanmışsa o konum kullanılır; değilse uygulama IP adresinden yaklaşık şehir bilgisi bulmayı dener ve hava durumu servisine şehir adını gönderir. IP tabanlı konum kesin GPS konumu değildir. Konum sorgusu yapılamazsa uygulama varsayılan konuma döner.

API anahtarları ve uygulamanın kişisel hafıza dosyaları yerel kalmalıdır. Gerçek kullanıcı verilerini veya anahtarları bu depoya eklemeyin.

## Sorun giderme

- **API anahtarı isteniyor:** `config/api_keys.json` dosyasına Gemini anahtarını ekleyin veya arayüzdeki ayar ekranını kullanın.
- **Mikrofon bulunamıyor:** Windows gizlilik ayarlarından masaüstü uygulamalarının mikrofona erişebildiğini ve doğru giriş aygıtının seçildiğini kontrol edin.
- **Hava durumu görünmüyor:** İnternet bağlantısını kontrol edin. Konum sorgusu veya hava durumu servisi geçici olarak erişilemiyorsa bilgi alınamayabilir.
- **Paket kurulumu başarısız:** `setup.bat` dosyasını yeniden çalıştırın ve Python'ın terminalde `python --version` komutuyla erişilebilir olduğunu doğrulayın.

## Lisans

Bu depoda henüz bir `LICENSE` dosyası yoktur. Başkalarının kodu kullanmasına, değiştirmesine veya dağıtmasına izin vermek istiyorsanız depoyu yayımlamadan önce uygun bir açık kaynak lisansı ekleyin.
