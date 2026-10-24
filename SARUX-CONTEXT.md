# SARUX — Proje amacı ve ortak bağlam

Tarih: 2026-10-25
Proje sahipleri: Yusuf ve Tamer
Kaynak: Yusuf'un bu tarihte anlattığı proje vizyonu
Derleyen: Codex

## 1. Bu dosya neden var?

Bu dosya, Sarux üzerinde çalışacak diğer ajanlara ortak başlangıç bağlamı sağlar. Yusuf ve Tamer'in ne yapmak istediğini her görüşmede yeniden anlatma ihtiyacını azaltır. Buradaki hedefler, mevcut uygulamanın bütün bu yeteneklere sahip olduğu anlamına gelmez.

## 2. Yusuf ve Tamer'in amacı

Yusuf ve arkadaşı Tamer, kendi başına çalışabilen bir kişisel bilgisayar ajanı geliştirmek istiyor. Projenin adı Sarux. Amaç, yalnızca sorulara cevap veren bir sohbet uygulaması yerine, kullanıcıyla iletişim kuran ve bilgisayarda somut işler yapabilen bir yardımcı oluşturmak.

Hermes agent, genel ajan yaklaşımı bakımından bir referans. Sarux'un öne çıkması istenen tarafı ise sesli komutlar ve kullanıcıyla daha doğrudan, birebir etkileşim.

## 3. Nasıl bir kullanım deneyimi istiyorlar?

1. Kullanıcı Sarux'a ağırlıklı olarak sesli komut verebilmeli.
2. Sarux kullanıcıyı anlayıp sözlü yanıt verebilmeli; etkileşim doğal bir konuşma gibi ilerleyebilmeli.
3. Kullanıcı bir iş istediğinde, Sarux bilgisayarda o işi yapabilmeli.
4. Gerektiğinde kullanıcıyla gündelik sohbet edebilmeli.
5. Sistemin arka planında çalışan ve ihtiyaç olduğunda ulaşılabilen bir yardımcı olmalı.
6. Her küçük adımın kullanıcı tarafından ayrı ayrı yönetilmesini gerektirmeden, verilen görevi kendi başına ilerletebilen bir ajan olmalı.

## 4. Yapması beklenen işler

Yusuf'un verdiği örnekler: “Onu aç”, “buraya bunu koy”, “şunu yap”, “bunu yap”. Bunlar uygulama açma ve bilgisayardaki küçük, gündelik işlemleri doğal dille yaptırma fikrini anlatıyor.

Beklenti, yalnızca nasıl yapılacağını tarif etmesi değil; uygun yetenek ve izinler bulunduğunda işlemi gerçekleştirmesi ve kullanıcıya cevap vermesi.

Bu örnekler henüz ayrıntılı bir özellik listesi veya sınırsız işlem yetkisi tanımı değildir. Hangi işlemlerin destekleneceği ve hangi işlemlerde kullanıcı kararı gerekeceği ayrıca tasarlanmalıdır.

## 5. Diğer projelerden nasıl ayrışmalı?

GitHub'da Jarvis ve benzeri isimlerle çok sayıda sesli asistan ve AI ajan projesi bulunuyor. Yusuf ve Tamer, Sarux'un benzerlerinin bir tekrarı olarak kalmasını istemiyor.

Sarux'un kendine özgü bazı özellikleri ve ek değerleri olması gerekiyor. Sistem uyumluluğu, Yusuf'un olası bir ayrışma alanı olarak verdiği örneklerden biri. Başka farklar da geliştirilebilir.

Ancak hangi özelliklerin Sarux'u ayrıştıracağı henüz kararlaştırılmış değil. Sistem uyumluluğunun kapsamı da açık değil; bu ifade şu aşamada belirli işletim sistemlerine destek sözü olarak yorumlanmamalı. Rakip incelemesi ve özellik seçimi ileride yapılacak çalışmalar.

## 6. Geliştirme yaklaşımı ve beklenti

- Proje, Yusuf ve Tamer'in birlikte geliştirdiği uzun vadeli bir çalışma olarak düşünülüyor.
- Geliştirmenin uzun soluklu olması bekleniyor; tek seferlik bir demo hedeflenmiyor.
- Zaman içinde daha gelişmiş bir ajan ortaya çıkarılmak isteniyor.
- Yusuf, sürecin sonunda güzel bir ürün çıkabileceğini düşünüyor.
- Bu konuşmada kesin teslim tarihi, bütçe, ticari model veya sürüm takvimi belirlenmedi.

## 7. Mevcut teknik başlangıç noktası

Yerel proje klasörü: C:\Users\yusuf\Desktop\Sarux-test

2026-10-25 tarihindeki kod incelemesinde görülen yapı:

- Windows için Python tabanlı masaüstü uygulaması.
- Metin ve araç kararları için Gemini.
- Bas-konuş ses girişi ve yerel Faster-Whisper-XXL transkripsiyonu.
- Sesli yanıt için Azure Speech.
- Bilgisayarda işlem yapmak için ayrı araç modülleri.

Bu bölüm mevcut başlangıç noktasını kaydeder. Teknoloji seçimlerinin uzun vadede değişmez olduğu veya hedeflenen otonom ajan deneyiminin tamamlandığı anlamına gelmez.

## 8. Henüz netleşmemiş konular

1. Sarux'u benzer projelerden ayıracak somut özellikler.
2. Sistem uyumluluğunun kapsamı ve desteklenecek donanımlar/işletim sistemleri.
3. Kendi başına çalışma sınırları, izinler ve kullanıcı onayı gerektiren işlemler.
4. Arka planda çalışma ve kullanıcıya erişilebilir olma biçimi.
5. Sesli etkileşimin nihai biçimi; mevcut bas-konuş yaklaşımının sürüp sürmeyeceği.
6. Özellik öncelikleri ve geliştirme yol haritası.

Bu maddeler açık tasarım sorularıdır; Yusuf ve Tamer'in verilmiş kararları gibi sunulmamalıdır.

## 9. Bu projede çalışacak ajanlar için

- Önerileri bu vizyonla ilişkilendir: sesle iletişim kuran, bilgisayarda iş yapan ve arka planda çalışan kişisel ajan.
- Mevcut kodun sunduğu yeteneklerle uzun vadeli hedefleri birbirinden ayır.
- Kesinleşmemiş özellikleri, platform desteğini ve takvimi varsayma.
- Yeni bir fikir önerirken bunun Yusuf ve Tamer'in mevcut kararı değil, öneri olduğunu belirt.
- Bu dosyayı başlangıç bağlamı olarak kullan; güncel kullanıcı talimatları ve sonradan alınan kararlar önceliklidir.

## Tek paragrafta proje

Sarux, Yusuf ve Tamer'in birlikte geliştirdiği; kendi başına çalışabilen, kullanıcıdan ağırlıklı olarak sesli komut alan, onunla birebir konuşabilen, bilgisayardaki gündelik işleri gerçekleştirebilen ve sistemin arka planında çalışan bir kişisel ajan projesidir. Hermes benzeri ajan yaklaşımını, daha yoğun sesli etkileşimle birleştirmeyi hedefler. GitHub'daki Jarvis benzeri projelerden kendine özgü özelliklerle ayrışması istenmektedir; bu farkların tam olarak ne olacağı henüz belirlenmemiştir. Geliştirmenin uzun soluklu olması beklenmektedir.

---

## 10. Yaşayan repo bağlamı — 2026-10-25

Bu bölüm, masaüstündeki ilk vizyon notunu koruyarak Sarux reposunda son görülen durumu ekler. İlk bölümlerdeki vizyon hedefleri tamamlanmış özellik garantisi değildir. Her ajan işe başlamadan önce canlı Git durumunu ve testleri yeniden kontrol etmelidir.

### Yusuf'un son teknik tercihleri

- Sarux'un standart ses adaptörü **PyAudio** olacak.
- Varsayılan beyin **Codex** olacak; kullanıcı Codex ile çalıştırmak istiyor.
- Uygulamaya **gece modu** eklenecek.
- Önceki proje hedefi, Gemini/Codex/Claude gibi seçilebilir beyinler ve beyinlerden bağımsız ortak araç/aksiyon yönlendirmesidir. Son Codex tercihi diğer beyinleri otomatik olarak kapsam dışına çıkarmaz.
- Sesli giriş yerel Faster-Whisper-XXL ile bas-konuş; riskli dış işlemler açık kullanıcı onayıyla, shell yetkisi dar sınırla kalmalı.
- Codex için yerel/resmî App Server oturumu kullanılmalı; OAuth/token kopyalanmamalı veya kaynak dosyalara yazılmamalı.

**TTS karar notu:** Masaüstündeki ilk bağlam, README ve mevcut `main.py` Azure Speech Neural kullanıyor. Ayrı bir kayıt Gemini TTS'i tüm beyinler için seçilmiş olarak gösteriyor. Bu çelişki Yusuf tarafından yeniden netleştirilene kadar TTS sağlayıcısını değiştirme; mevcut kodu Azure kullanıyor diye tarif et, bunu güncel ürün kararı olarak kesinleştirme.

### Repo ve doğrulanmış durum

- Kanonik kod deposu: `/home/yusuf/projects/Sarux`; `origin`: `https://github.com/TamerSrhn/Sarux.git`.
- Windows ZIP test klasörü: `C:\Users\yusuf\Desktop\Sarux-test`.
- Son incelenen dal: `feat/multi-brain-voice-backends`; son kaydedilmiş commit `c5eb6e4` (`feat: add validated brain selection config`). Kod değişiklikleri ve yeni modüller çalışma ağacında **commit edilmemiş** durumda. Yeni dosyaları eklerken bu mevcut değişiklikleri temizleme, sıfırlama veya topluca stage etme.
- `main.py`, Codex App Server ve Gemini beyinlerini başlatabiliyor; Claude seçilirse runtime henüz bağlı değil ve hata veriyor.
- Provider seçimi şu an `gemini` ve `codex` içeriyor, varsayılan Codex. Ancak `tests/test_provider_selection.py` içindeki Claude kayıt-normalizasyon testi hâlâ Claude bekliyor. Bu tutarsızlığı bir sonraki kod işinde çöz; Claude desteği kararını testleri susturmak için sessizce silme.
- `requirements.txt` PyAudio 0.2.14 kullanıyor. `setup.ps1`, Windows'ta resmi PyAudio wheel uyumluluğu için Python 3.13 x64 arıyor. Bu güncel kurulum YUBUS'ta henüz uçtan uca doğrulanmadı.
- `ui_theme.py` gündüz/gece paletini sağlıyor; tema birim testleri var, fakat `ui.py` içinde henüz kullanılmıyor. Yani gece modu arayüze entegre edilmiş değil.
- `main.py` ses çıkışında şu an `AzureSpeechTTS` kullanıyor.
- README, bu dalın yeni durumuyla tam eşleşmeyebilir; dağıtım öncesinde gerçek provider/ses/kurulum davranışına göre güncellenmeli.

### Bu snapshot'ta çalıştırılan hedefli testler

2026-10-25 tarihinde Linux repo kopyasında:

- `python3 -m unittest discover -s tests -p 'test_pyaudio_audio.py' -v` — **4 test geçti**.
- `python3 -m unittest discover -s tests -p 'test_codex_app_server.py' -v` — **8 test geçti**.
- `python3 -m unittest discover -s tests -p 'test_ui_theme.py' -v` — **3 test geçti**; bu yalnız palet modülünü doğrular, UI entegrasyonunu değil.
- `python3 -m unittest discover -s tests -p 'test_provider_selection.py' -v` — **6 testten 5'i geçti, 1'i kaldı**: `test_reads_and_normalizes_a_valid_saved_selection`, `CLAUDE` değerinin `codex`'e düşmesini hata olarak bildiriyor.
- Tam test paketi bu snapshot'ta çalıştırılmadı.
- Önceki Windows testleri daha eski `sounddevice` ZIP'i içindi; son PyAudio/Codex/gece modu değişiklikleriyle karıştırılmamalı. Bu yeni snapshot için Windows kurulum, gerçek mikrofon/TTS ve gerçek Codex yanıt turu doğrulanmış değil. `codex app-server --disable plugins --disable apps --help` Windows'ta çalıştı; bu gerçek yanıt testi değildir.

### Sonraki mantıklı doğrulama sırası

1. Claude'un yakın vadede seçilebilir beyin olup olmayacağına karar ver; provider listesi ve testleri tutarlı yap.
2. Gece modu paletini gerçek UI bileşenlerine ve kalıcı ayara bağla; Windows UI smoke test yap.
3. Python 3.13 x64 üzerinde PyAudio kurulumunu ve gerçek giriş/çıkışı Windows'ta doğrula.
4. Codex App Server ile gerçek yanıt turunu ve ortak tool router'ı uçtan uca test et.
5. README'yi güncelle, tam test paketini ve Windows smoke testini çalıştır; sonra küçük, testli commit'ler ve kullanıcı talimatındaki PR akışıyla ilerle.

### Bağlamı güncel tutma

Her doğrulanmış kilometre taşından sonra bu bölüme kısa, tarihli bir güncelleme ekle: yapılan değişiklik, kanıt/test komutu ve kalan engel. Vizyon bölümünü gerçekleşmiş özellik gibi yeniden yazma. Eski snapshot'ı tarih ve kanıtla sakla; kaynakla çelişen yeni kararları sessizce ezme, Yusuf'tan netleştir.
