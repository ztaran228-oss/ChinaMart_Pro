// Инициализируем Telegram Web App
const tg = window.Telegram.WebApp;

// Сообщаем Telegram, что приложение готово и расширяем его на весь экран
tg.expand();
tg.ready();

// Сообщаем цвет фона для шапки самого Telegram
tg.setHeaderColor('#121212');

// Временная база тестовых товаров
const products = [
    { id: 1, name: "Кроссовки Nike Air", price: "250 ¥", image: "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80" },
    { id: 2, name: "Рюкзак Xiaomi", price: "85 ¥", image: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&q=80" },
    { id: 3, name: "Наушники TWS", price: "120 ¥", image: "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80" },
    { id: 4, name: "Чехол iPhone 15", price: "20 ¥", image: "https://images.unsplash.com/photo-1603313011101-320f26a4f6f6?w=500&q=80" }
];

const catalogElement = document.getElementById('catalog');

// Функция вывода товаров на экран
function renderCatalog() {
    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        
        card.innerHTML = `
            <img src="${product.image}" class="product-image" alt="${product.name}">
            <h3 class="product-title">${product.name}</h3>
            <div class="product-price">${product.price}</div>
            <button class="add-btn" onclick="addToCart(${product.id}, '${product.name}')">В корзину</button>
        `;
        
        catalogElement.appendChild(card);
    });
}

// Реакция на нажатие кнопки "В корзину"
window.addToCart = function(productId, productName) {
    // Включаем тактильный отклик (вибрацию) при нажатии
    tg.HapticFeedback.impactOccurred('light');
    
    // Показываем окошко от самого Telegram
    tg.showAlert(`Товар "${productName}" добавлен в корзину!`);
}

// Запускаем отрисовку при загрузке
renderCatalog();
// Функция переключения вкладок
window.showTab = function(tabId) {
    // Скрываем все вкладки
    document.querySelectorAll('.tab-content').forEach(t => t.style.display = 'none');
    // Показываем нужную
    document.getElementById(tabId).style.display = 'block';
}

// Функция-заглушка для добавления товара (позже свяжем с базой)
window.addProduct = function() {
    const title = document.getElementById('title').value;
    const price = document.getElementById('price').value;
    alert("Товар '" + title + "' по цене " + price + " добавлен!");
}