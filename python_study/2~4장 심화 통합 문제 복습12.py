def get_stock_status(stock):
    if stock == 0:
        return "품절"
    elif stock <= 3:
        return "재고 부족"
    else:
        return "재고 충분"


def analyze_products(products):
    total_stock = 0
    sold_out_count = 0
    low_stock_count = 0
    max_sold = 0

    for product in products:
        name = product["name"]
        stock = product["stock"]
        sold = product["sold"]

        status = get_stock_status(stock)

        print(f"{name}: {status}")

        total_stock += stock

        if status == "품절":
            sold_out_count += 1

        if status == "재고 부족":
            low_stock_count += 1

        if sold > max_sold:
            max_sold = sold

    return {
        "total_stock": total_stock,
        "sold_out_count": sold_out_count,
        "low_stock_count": low_stock_count,
        "max_sold": max_sold
    }


products = [
    {"name": "노트북", "stock": 5, "sold": 12},
    {"name": "마우스", "stock": 0, "sold": 30},
    {"name": "키보드", "stock": 2, "sold": 8},
    {"name": "모니터", "stock": 10, "sold": 15}
]

result = analyze_products(products)

print()
print(f"전체 재고 수: {result['total_stock']}개")
print(f"품절 상품 수: {result['sold_out_count']}개")
print(f"재고 부족 상품 수: {result['low_stock_count']}개")
print(f"최고 판매 수량: {result['max_sold']}개")