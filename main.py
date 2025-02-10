import yfinance as yf

# Liste des actions
stocks = [
    'OR.PA',          # L'Oréal
    'MC.PA',          # LVMH
    'RI.PA',          # Pernod Ricard
    'SW.PA',          # Sodexo
    'CAP.PA',         # Cap Gemini
    'TTE.PA',         # TotalEnergies
    'SU.PA',          # Schneider Electric
    'GPDNF',          # Danone
    'AI.PA',          # Air Liquide
    'AC.PA'           # Accor
]

# Dictionnaire pour stocker les tickers et leurs noms
stocks_dict = {}
for ticker in stocks:
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    company_name = stock_info.get('longName', 'Nom non disponible')  # Récupère le nom de l'entreprise
    stocks_dict[ticker] = company_name  # Associer le ticker au nom de l'entreprise

# Fonction pour récupérer la valeur actuelle de chaque action
def get_stock_values(stocks):
    stock_data = {}
    for stock in stocks:
        stock_data[stock] = yf.Ticker(stock).history(period='1d')['Close'].iloc[-1]
    return stock_data

# Fonction pour demander à l'utilisateur combien d'actions il possède
def get_user_portfolio(stocks):
    portfolio = {}
    print("Entrez le nombre d'actions que vous possédez pour chaque titre :")
    for stock in stocks:
        while True:
            try:
                quantity = int(input(f"Nombre d'actions pour {stock}: "))
                if quantity < 0:
                    raise ValueError("Le nombre d'actions ne peut pas être négatif.")
                portfolio[stock] = quantity
                break
            except ValueError as e:
                print(f"Entrée invalide : {e}. Veuillez entrer un nombre entier positif.")
    return portfolio

# Fonction pour calculer la valeur du portefeuille actuel
def calculate_portfolio_value(portfolio, stock_values):
    total_value = 0
    for stock, quantity in portfolio.items():
        total_value += quantity * stock_values[stock]
    return total_value

# Fonction de rééquilibrage du portefeuille
def rebalance_portfolio(portfolio, stock_values, total_value):
    print("\nRééquilibrage du portefeuille :")
    
    # Calculer la répartition cible pour chaque titre (répartition équitable entre toutes les actions)
    target_percentages = 100 / len(stocks)  # 100% divisé par le nombre d'actions
    
    # Créer des listes pour les actions à acheter et à vendre
    buy_list = []
    sell_list = []
    
    # Calculer la quantité idéale de chaque action à acheter/vendre
    for stock in portfolio:
        target_value = total_value * (target_percentages / 100)  # Valeur cible pour chaque action
        target_quantity = int(target_value // stock_values[stock])  # Arrondi à l'entier inférieur
        
        # Comparer la quantité cible avec la quantité actuelle
        current_quantity = portfolio.get(stock, 0)
        if target_quantity > current_quantity:
            buy_list.append((stocks_dict.get(stock, stock), target_quantity - current_quantity))  # Nom de l'action et quantité à acheter
        elif target_quantity < current_quantity:
            sell_list.append((stocks_dict.get(stock, stock), current_quantity - target_quantity))  # Nom de l'action et quantité à vendre
    
    # Trier les listes par ordre décroissant de quantité
    buy_list.sort(key=lambda x: x[1], reverse=True)
    sell_list.sort(key=lambda x: x[1], reverse=True)
    
    # Afficher les actions à acheter
    print("Actions à acheter :")
    for company_name, quantity in buy_list:
        print(f"{company_name}: {quantity} actions")
    
    # Afficher les actions à vendre
    print("\nActions à vendre :")
    for company_name, quantity in sell_list:
        print(f"{company_name}: {quantity} actions")

    return buy_list, sell_list

# Récupérer les valeurs actuelles des actions
stock_values = get_stock_values(stocks)
# Récupérer les valeurs actuelles des actions et trier par ordre décroissant
sorted_stock_values = sorted(stock_values.items(), key=lambda x: x[1], reverse=True)
# Affichage des stocks triés par valeur décroissante
print("Valeurs actuelles des actions :")
for stock, value in sorted_stock_values:
    print(f"{stock}: {value} USD")
55
# Demander à l'utilisateur le nombre d'actions qu'il possède
portfolio = get_user_portfolio(stocks)

# Calculer la valeur actuelle du portefeuille
portfolio_value = calculate_portfolio_value(portfolio, stock_values)
print(f"\nValeur totale actuelle du portefeuille: {portfolio_value} USD")

# Rééquilibrer le portefeuille
rebalance_portfolio(portfolio, stock_values, portfolio_value)