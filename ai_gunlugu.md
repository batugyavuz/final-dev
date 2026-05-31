# RotaKaravan - Yapay Zeka Geliştirme Günlüğü (AI Journal)

*Oturum 1 — 31 Mayıs — 14:36-15:05*

Ajan'a kamp ve karavan ihtiyaç takip uygulaması (RotaKaravan) için Application Factory ve Blueprints mimarisine sahip klasör yapısı oluşturması yönünde istek verdim. Ajan ilk planda projeyi varsayılan `scratch` klasöründe tasarladı; ancak ben projenin masaüstünde `batu` klasöründe olmasını istedim.

Masaüstünde klasör oluşturulduğunda ilk başta bulamadım. Ajan, Windows sistemlerdeki OneDrive yönlendirmesini fark ederek gerçek masaüstü yolunun `C:\Users\mihra\OneDrive\Masaüstü\batu` olduğunu tespit etti ve dosyaları oraya başarıyla taşıdı. 

Ardından, veritabanı modeli `models.py` dosyasını oluştururken Bilişim Güvenliği bölümü hassasiyetlerim doğrultusunda SQL Injection zafiyetine karşı koruma sağlayan SQLAlchemy ORM yapısının güvenliğini açıklayan Türkçe yorum satırlarını eklettim. Son olarak bilgisayarda Git kurulu olmadığını fark edince Ajan'a Git kurdurdum, yerel depoyu oluşturup ilk commit'i hazırlattım ve `https://github.com/batugyavuz/final-dev.git` adresine kodları yüklettim.

*Bu oturumdan asıl öğrendiğim:* Proje dosyalarının yerel dizinlerde kaybolmaması için OneDrive entegrasyonu olan Windows sistemlerde gerçek masaüstü yolunu doğrulamak gerektiği ve kodları doğrudan otomatik Git yapılandırmasıyla yüklemenin zamandan kazandırdığıdır. Ayrıca güvenlik yorum satırlarının ilk aşamada eklenmesi kod inceleme süreçlerinde güvenli yazılım prensiplerini belgelemiş oldu.

---

*Oturum 2 — 31 Mayıs — 15:09-15:15*

Ajan'a `items` blueprint'i içerisine kamp eşyaları için CRUD (Ekleme, Okuma, Güncelleme, Silme) rotalarını yazdırma talimatı verdim. Veritabanında bulunmayan bir ID için güncelleme veya silme isteği geldiğinde sistemin çökmemesi için `abort(404)` hata kontrolünü eklettim. Ayrıca uygulamanın ilk çalışmasında veritabanı tablolarının otomatik oluşması için `run.py` dosyasına uygulama bağlamı (app context) kodunu entegre ettik.

Arayüz tarafında, sade bir tablo görünümü yerine modern ve mobil uyumlu bir görünüm için Bootstrap 5 (CDN) entegrasyonu yaptık. `templates/base.html` dosyasını güncelledikten sonra `items/dashboard.html` şablonunu oluşturup eşyaların kategorilerine (Mutfak, Çadır, Teknik vb.) göre ayrı panellerde listelenmesini sağladık. "Alındı" (`is_packed=True`) olarak işaretlenen eşyaların üzerini çizdirip, opaklığını azaltarak soluklaşmasını sağlayan CSS stillerini bağladık. Değişiklikleri test ettikten sonra sorunsuzca GitHub'a gönderdik.

*Bu oturumdan asıl öğrendiğim:* Jinja2'nin `selectattr` filtresini kullanarak veritabanından gelen verileri şablonda dinamik olarak kategorilere göre gruplandırmanın, karmaşık backend sorguları yazmaktan çok daha pratik olduğudur. Ayrıca Bootstrap 5 ve özel koyu tema renklerinin harmanlanmasıyla çok daha profesyonel bir kamp teması elde ettik.
