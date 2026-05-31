from flask import render_template, request, redirect, url_for
from app.items import items_bp

# Mock items database for initial demonstration without setup steps
MOCK_ITEMS = [
    {'id': 1, 'name': 'Katlanır Sandalye', 'category': 'Mutfak/Kamp', 'quantity': 2, 'is_packed': True},
    {'id': 2, 'name': 'Tüp ve Ocak Başlığı', 'category': 'Mutfak/Kamp', 'quantity': 1, 'is_packed': True},
    {'id': 3, 'name': 'İlk Yardım Seti', 'category': 'Güvenlik', 'quantity': 1, 'is_packed': False},
    {'id': 4, 'name': 'Çadır / Karavan Tentesi', 'category': 'Uyku', 'quantity': 1, 'is_packed': False},
    {'id': 5, 'name': 'El Feneri ve Kafa Lambası', 'category': 'Teknik', 'quantity': 2, 'is_packed': True},
    {'id': 6, 'name': 'Termos', 'category': 'Mutfak/Kamp', 'quantity': 1, 'is_packed': False},
]

@items_bp.route('/')
def list_items():
    """List all caravan/camping needs."""
    return render_template('items/list.html', items=MOCK_ITEMS)
