# RotaKaravan - Yapay Zeka Geliştirme Günlüğü (AI Journal)

Bu günlük, RotaKaravan projesinin geliştirilme aşamalarındaki tasarım kararlarını, mimari seçimleri ve yapay zeka tarafından atılan adımları detaylandırmaktadır.

## 📅 31 Mayıs 2026

### 🛠️ Yapılan İşlemler ve Kararlar
1. **Mimari Model Belirlenmesi**:
   - Spagetti kod yapısını engellemek için Flask uygulamalarında standart ve profesyonel kabul edilen **Application Factory (`create_app`)** deseni tercih edildi.
   - Modülerlik sağlamak ve farklı işlevleri ayırmak için **Blueprints** mimarisi kuruldu.
2. **Blueprint Dağılımı**:
   - `main`: Genel paneli, istatistikleri ve anasayfa akışını barındırıyor.
   - `items`: Eşyalar/ihtiyaçlar listesinin listelenmesi ve gelecekteki CRUD işlemlerini yönetiyor.
3. **Veritabanı Altyapısı**:
   - İleride SQL veritabanı (SQLite/PostgreSQL) entegrasyonunu kolaylaştırmak amacıyla `app/models.py` içinde SQLAlchemy `Item` modeli tanımlandı.
4. **Tasarım Arayüz Seçimi**:
   - Doğa ve karavan ruhuna uygun olarak koyu yeşil ve kehribar sarısı renk tonlarında, yarı saydam cam efekti sunan **Glassmorphism** stiliyle modern bir CSS tasarımı oluşturuldu.

### 📝 Teknik Detaylar
- Giriş noktası: `run.py`
- Ayarlar: `config.py` ve `.env`
- Arayüz Kütüphaneleri: Google Fonts (Outfit), FontAwesome (İkonlar)
