from flask import render_template
from app.main import main_bp

@main_bp.route('/')
def index():
    """RotaKaravan homepage/dashboard view showing stats and quick actions."""
    # Sample statistics to showcase on the dashboard
    stats = {
        'total_items': 12,
        'packed_items': 4,
        'categories_count': 4,
        'completion_percentage': 33
    }
    return render_template('main/index.html', stats=stats)
