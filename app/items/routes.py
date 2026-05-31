from flask import render_template, request, redirect, url_for, abort
from app import db
from app.items import items_bp
from app.models import Item

@items_bp.route('/')
def list_items():
    """List all caravan/camping needs from the SQLite database."""
    items = Item.query.all()
    return render_template('items/list.html', items=items)

@items_bp.route('/add', methods=['POST'])
def add_item():
    """Create a new item in the database."""
    name = request.form.get('name')
    category = request.form.get('category', 'Genel')
    quantity = request.form.get('quantity', 1, type=int)

    if not name or name.strip() == "":
        return redirect(url_for('items.list_items'))

    new_item = Item(name=name.strip(), category=category.strip(), quantity=quantity)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('items.list_items'))

@items_bp.route('/toggle/<int:item_id>', methods=['POST'])
def toggle_item(item_id):
    """Toggle is_packed status (True/False). If ID is not found, aborts with 404."""
    item = Item.query.get_or_404(item_id)
    item.is_packed = not item.is_packed
    db.session.commit()
    return redirect(url_for('items.list_items'))

@items_bp.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    """Delete an item. If ID is not found, aborts with 404."""
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('items.list_items'))
