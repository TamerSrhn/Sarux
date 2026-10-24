# Sarux — Agent çalışma kuralları

Her görevden önce `SARUX-CONTEXT.md` ve `README.md` dosyalarını oku; sonra `git status --short --branch` ile canlı çalışma ağacını kontrol et.

## Kaynak ve doğruluk

- Güncel Yusuf talimatı, eski proje notlarından üstündür. `SARUX-CONTEXT.md` içindeki vizyonu tamamlanmış özellik gibi sunma; kod, test ve Windows smoke test kanıtını ayrı değerlendir.
- Eski veya çelişen kararları sessizce ezme. Çelişki kullanıcı kararını etkiliyorsa netleştir; güvenli varsayımla ilerliyorsan varsayımı yaz.
- Yalnız gerçekten çalıştırdığın testleri ve gördüğün çıktıları raporla. Worker/başka ajan özeti tek başına kanıt değildir.

## Çalışma ağacı ve değişiklikler

- Mevcut uncommitted değişiklikleri koru. `git reset`, `git clean`, toplu stage veya başkasının değişikliklerini ezme.
- Kod değişikliğinde dar kapsamlı test yaz/çalıştır; tamamlanınca ilgili regression testlerini ve mümkünse tam test paketini çalıştır.
- Paralel işler yalnız bağımsızsa yürüsün; aynı dosyanın tek yazarı olsun. Aynı repoda birden fazla ajan kod yazacaksa ayrı branch/worktree kullan.
- Doğrulanmış kilometre taşından sonra `SARUX-CONTEXT.md` içindeki yaşayan durum bölümünü tarih, kanıt ve kalan engellerle güncelle.

## Güvenlik ve yetki

- API anahtarı, OAuth token, parola veya özel anahtarı kaynak koda, test fixture'ına, loga, bağlam dosyasına ya da Git'e yazma. Credential Manager/uygun yerel kasayı kullan; Codex token'ını Sarux'a kopyalama.
- Shell ve bilgisayar kontrolünü dar tut. Riskli veya dış dünyada sonuç doğuran işlemler kullanıcı onayı gerektirir.
- Dosya silme, canlı dağıtım, satın alma veya erişim/credential değişikliği için ayrıca açık onay al.

## GitHub akışı

- Küçük, mantıksal ve test edilmiş değişiklikleri ayrı commit'lere ayır; commit mesajını Conventional Commits biçiminde yaz.
- PR açıklamasında amaç, kapsam, test komutları ve gerçek sonuçları belirt.
- `git status`/diff'i kontrol et ve yalnız bu işe ait dosyaları stage et. Kullanıcı açıkça istemedikçe push, PR açma veya merge yapma; merge için ayrıca açık onay gerekir.
