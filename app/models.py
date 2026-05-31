from app import db

class Item(db.Model):
    """
    Kamp ve karavan ihtiyaç takip uygulaması için 'Item' (Eşya) modeli.
    
    GÜVENLİK BİLGİLENDİRMESİ (Bilişim Güvenliği):
    --------------------------------------------------
    SQLAlchemy ORM kullanımı, geleneksel veritabanı işlemlerinde sıkça yapılan 
    SQL sorgusu birleştirme (SQL string concatenation) hatalarını engeller. 
    Arka planda tüm sorguları parametreleştirerek (Parameterized Queries) çalıştırır.
    
    Bu sayede:
    1. Kullanıcı girdileri sorguya dahil edilmeden önce SQL motoru tarafından sadece 'veri' olarak işlenir.
    2. Girdilerin içine yerleştirilen zararlı SQL komutları (örn: ' OR '1'='1) komut olarak çalıştırılamaz.
    3. OWASP Top 10 listesinin en başında yer alan SQL Injection (SQL Enjeksiyonu) 
       zafiyeti otomatik olarak önlenmiş olur.
    --------------------------------------------------
    """
    __tablename__ = 'items'
    
    # Benzersiz Tanımlayıcı (Primary Key)
    id = db.Column(db.Integer, primary_key=True)
    
    # Eşya adı (Boş geçilemez)
    name = db.Column(db.String(100), nullable=False)
    
    # Kategori (Mutfak, Çadır, Elektronik vb.)
    category = db.Column(db.String(50), nullable=False, default='Genel')
    
    # Alındı/Paketlendi durumu (Varsayılan olarak hazırlanmadı)
    is_packed = db.Column(db.Boolean, default=False, nullable=False)
    
    def __repr__(self):
        """
        Nesnenin okunabilir temsilini döndürerek geliştirme aşamasındaki hata ayıklama 
        (debugging) süreçlerini daha güvenli ve pratik kılar.
        """
        return f'<Item {self.name} ({self.category}) - Hazır: {self.is_packed}>'
