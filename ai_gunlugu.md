# RotaKaravan - Yapay Zeka Geliştirme Günlüğü (AI Journal)

*Oturum 1 — 31 Mayıs — 14:36-15:05*

Ajan'a kamp ve karavan ihtiyaç takip uygulaması (RotaKaravan) için Application Factory ve Blueprints mimarisine sahip klasör yapısı oluşturması yönünde istek verdim. Ajan ilk planda projeyi varsayılan `scratch` klasöründe tasarladı; ancak ben projenin masaüstünde `batu` klasöründe olmasını istedim.

Masaüstünde klasör oluşturulduğunda ilk başta bulamadım. Ajan, Windows sistemlerdeki OneDrive yönlendirmesini fark ederek gerçek masaüstü yolunun `C:\Users\mihra\OneDrive\Masaüstü\batu` olduğunu tespit etti ve dosyaları oraya başarıyla taşıdı. 

Ardından, veritabanı modeli `models.py` dosyasını oluştururken Bilişim Güvenliği bölümü hassasiyetlerim doğrultusunda SQL Injection zafiyetine karşı koruma sağlayan SQLAlchemy ORM yapısının güvenliğini açıklayan Türkçe yorum satırlarını eklettim. Son olarak bilgisayarda Git kurulu olmadığını fark edince Ajan'a Git kurdurdum, yerel depoyu oluşturup ilk commit'i hazırlattım ve `https://github.com/batugyavuz/final-dev.git` adresine kodları yüklettim.

*Bu oturumdan asıl öğrendiğim:* Proje dosyalarının yerel dizinlerde kaybolmaması için OneDrive entegrasyonu olan Windows sistemlerde gerçek masaüstü yolunu doğrulamak gerektiği ve kodları doğrudan otomatik Git yapılandırmasıyla yüklemenin zamandan kazandırdığıdır. Ayrıca güvenlik yorum satırlarının ilk aşamada eklenmesi kod inceleme süreçlerinde güvenli yazılım prensiplerini belgelemiş oldu.
