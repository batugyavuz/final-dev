# RotaKaravan - Yapay Zeka Geliştirme Günlüğü (AI Journal)

*Oturum 1 — 31 Mayıs — 14:36-15:05*

Ajan'a kamp ve karavan ihtiyaç takip uygulaması (RotaKaravan) için Application Factory ve Blueprints mimarisine sahip klasör yapısı oluşturması yönünde istek verdim. Ajan ilk planda projeyi varsayılan `scratch` klasöründe tasarladı; ancak ben projenin masaüstünde `batu` klasöründe olmasını istedim.

Masaüstünde klasör oluşturulduğunda ilk başta bulamadım. Ajan, Windows sistemlerdeki OneDrive yönlendirmesini fark ederek gerçek masaüstü yolunun `C:\Users\mihra\OneDrive\Masaüstü\batu` olduğunu tespit etti ve dosyaları oraya başarıyla taşıdı. 

Ardından, veritabanı modeli `models.py` dosyasını oluştururken Bilişim Güvenliği bölümü hassasiyetlerim doğrultusunda SQL Injection zafiyetine karşı koruma sağlayan SQLAlchemy ORM yapısının güvenliğini açıklayan Türkçe yorum satırlarını eklettim. Son olarak bilgisayarda Git kurulu olmadığını fark edince Ajan'a Git kurdurdum, yerel depoyu oluşturup ilk commit'i hazırlattım ve `https://github.com/batugyavuz/final-dev.git` adresine kodları yüklettim.

*Bu oturumdan asıl öğrendiğim:* Proje dosyalarının yerel dizinlerde kaybolmaması için OneDrive entegrasyonu olan Windows sistemlerde gerçek masaüstü yolunu doğrulamak gerektiği ve kodları doğrudan otomatik Git yapılandırmasıyla yüklemenin zamandan kazandırdığıdır. Ayrıca güvenlik yorum satırlarının ilk aşamada eklenmesi kod inceleme süreçlerinde güvenli yazılım prensiplerini belgelemiş oldu.

---

*Oturum 2 — 31 Mayıs — 15:09-15:11*

Ajan'a `items` blueprint'i içerisine kamp eşyaları için CRUD (Ekleme, Okuma, Güncelleme, Silme) rotalarını yazdırma talimatı verdim. Veritabanında bulunmayan bir ID için güncelleme veya silme isteği geldiğinde sistemin çökmemesi için `abort(404)` hata kontrolünü eklettim. Ayrıca uygulamanın ilk çalışmasında veritabanı tablolarının otomatik oluşması için `run.py` dosyasına uygulama bağlamı (app context) kodunu entegre ettik.

Arayüz tarafında, sade bir tablo görünümü yerine modern ve mobil uyumlu bir görünüm için Bootstrap 5 (CDN) entegrasyonu yaptık. `templates/base.html` dosyasını güncelledikten sonra `items/dashboard.html` şablonunu oluşturup eşyaların kategorilerine (Mutfak, Çadır, Teknik vb.) göre ayrı panellerde listelenmesini sağladık. "Alındı" (`is_packed=True`) olarak işaretlenen eşyaların üzerini çizdirip, opaklığını azaltarak soluklaşmasını sağlayan CSS stillerini bağladık. Değişiklikleri test ettikten sonra sorunsuzca GitHub'a gönderdik.

*Bu oturumdan asıl öğrendiğim:* Jinja2'nin `selectattr` filtresini kullanarak veritabanından gelen verileri şablonda dinamik olarak kategorilere göre gruplandırmanın, karmaşık backend sorguları yazmaktan çok daha pratik olduğudur. Ayrıca Bootstrap 5 ve özel koyu tema renklerinin harmanlanmasıyla çok daha profesyonel bir kamp teması elde ettik.

---

*Oturum 3 — 31 Mayıs — 15:12-15:15*

Kullanıcıların hazırlık motivasyonunu artırmak amacıyla sayfanın en üstünde gösterilecek bir ilerleme (progress) göstergesi tasarlanmasını istedim. Ajan, bu yüzdeyi backend tarafında (`routes.py`) veritabanından halihazırda çekilmiş olan veriler üzerinden dinamik olarak hesaplayan mantığı kurdu. Böylece ekstra SQL sorgusu çalıştırmayarak performansı artırmış olduk.

Bootstrap 5 ile hazırlanan bu ilerleme çubuğu, eşyaların paketlenme durumuna göre gerçek zamanlı dolmaktadır. Ayrıca istek doğrultusunda, hazırlık oranı tam olarak %100'e ulaştığında ilerleme çubuğunun renginin yeşile (`bg-success`) dönmesini sağlayan koşullu sınıf yapısı Jinja şablonuna entegre edildi. Yapılan tüm değişiklikler başarıyla yerel commit yapılıp GitHub deposuna aktarıldı.

*Bu oturumdan asıl öğrendiğim:* Kod tasarımında dinamik arayüz elementlerinin (ilerleme çubuğu vb.) veri tabanındaki güncellemeleri anında yansıtmasının kullanıcı deneyimini (UX) ciddi oranda yükselttiğidir. Ayrıca, backend'de performans iyileştirmesi yaparak gereksiz SQL sorgularından kaçınmanın önemi bu oturumda daha net anlaşıldı.

---

*Oturum 4 — 31 Mayıs — 15:13-15:15*

Projenin canlı ortama (Render.com) sorunsuz taşınabilmesi amacıyla yapılandırma hazırlığı yaptık. Ajan'a, production düzeyinde HTTP sunucusu olarak **Gunicorn** kullanılabilmesi için `requirements.txt` dosyasına `gunicorn` kütüphanesini eklettim. Gunicorn'un Application Factory yapısındaki Flask uygulamasını çağırabilmesi için kök dizinde bir `wsgi.py` dosyası oluşturduk. Değişiklikleri Git ile yerel depoya commit edip GitHub'a (`main` dalına) gönderdik.

*Bu oturumdan asıl öğrendiğim:* Canlıya alma (deployment) süreçlerinde, geliştirme aşamasındaki built-in Flask sunucusu yerine Gunicorn gibi dayanıklı bir WSGI sunucusunun kullanılmasının zorunlu olduğunu ve Application Factory modellerinde uygulamanın doğrudan başlatılabilmesi için `wsgi.py` gibi bir giriş noktası ara katmanının gerekliliğidir.
