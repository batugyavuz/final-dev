# RotaKaravan - Proje Mimari Raporu

Bu rapor, RotaKaravan projesinin genel mimarisini, kullanılan teknolojileri ve kod düzenini açıklamaktadır.

---

## 1. Mimari Tasarım
Proje, Flask topluluğu tarafından en iyi pratik (Best Practice) olarak önerilen **Application Factory** ve **Blueprints** desenleri üzerine kurulmuştur.

### A. Application Factory (`create_app`)
Klasik Flask uygulamalarında `app` nesnesi global olarak tanımlanır ve her yerde içe aktarılır. Bu durum büyük projelerde dairesel içe aktarma (circular import) hatalarına neden olur. 
`create_app` fonksiyonu sayesinde:
- Uygulama ayarları dinamik olarak (geliştirme veya canlı ortam) yüklenir.
- Test yazımı kolaylaşır, çünkü her test için sıfırdan yeni bir uygulama örneği (instance) oluşturulabilir.

### B. Blueprints (Modüler Yapı)
Uygulama işlevsel olarak iki ana modüle bölünmüştür:
1. **`main`**: Giriş ekranı, bilgilendirmeler ve temel gösterge paneli (Dashboard) işlerini yürütür.
2. **`items`**: Karavan ve kamp malzemelerinin yönetimini (ekleme, çıkarma, paketlendi olarak işaretleme) sağlar.

---

## 2. Klasör ve Dosya Rolleri

| Dosya / Klasör | Görevi / Rolü |
| :--- | :--- |
| `run.py` | Uygulamayı çalıştıran ana tetikleyici dosya. |
| `.env` | Şifreler, veritabanı yolları gibi çevre değişkenlerini tutar (güvenlik için). |
| `config.py` | `.env` dosyasındaki verileri okur ve Flask'ın anlayacağı ayarlara dönüştürür. |
| `requirements.txt` | Projenin çalışması için gereken Python paket listesi. |
| `app/__init__.py` | Uygulama fabrikasının kurulduğu yer. Eklentileri ve Blueprint'leri birbirine bağlar. |
| `app/models.py` | Veritabanı tablolarının (SQLAlchemy modellerinin) tanımlandığı yer. |
| `app/static/` | CSS tasarımları, JavaScript kodları ve görsellerin barındığı klasör. |
| `app/templates/` | Jinja2 motoru ile HTML sayfalarının oluşturulduğu yer. |

---

## 3. İlerisi İçin Öneriler (Geliştirme Yol Haritası)
- **Veritabanı Göçü (Migration)**: `Flask-Migrate` entegre edilerek veritabanı şemasındaki değişiklikler kolayca yönetilebilir.
- **Dinamik Veri Yönetimi**: Mevcut mock (sahte) verilerin yerine, `models.py` içindeki `Item` modeli kullanılarak SQLite veritabanından gerçek veriler çekilip kaydedilebilir (CRUD işlemleri).
- **Kullanıcı Yetkilendirme (Auth)**: Kamp listelerinin kişiye özel olması için `Flask-Login` kullanılarak sisteme üye girişi eklenebilir.
