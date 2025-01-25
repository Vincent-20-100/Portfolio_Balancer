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
    'GPDNF',         # Danone
    'AI.PA',          # Air Liquide
    'AC.PA'           # Accor
]

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
    
    # Calculer la quantité idéale de chaque action à acheter/vendre
    target_portfolio = {}
    for stock in portfolio:
        target_value = total_value * (target_percentages / 100)  # Valeur cible pour chaque action
        target_quantity = int(target_value // stock_values[stock])  # Arrondi à l'entier inférieur
        target_portfolio[stock] = target_quantity
    
    # Affichage des actions à acheter ou vendre
    for stock, target_quantity in target_portfolio.items():
        current_quantity = portfolio.get(stock, 0)
        if target_quantity > current_quantity:
            print(f"Acheter {target_quantity - current_quantity} actions de {stock}")
        elif target_quantity < current_quantity:
            print(f"Vendre {current_quantity - target_quantity} actions de {stock}")
        else:
            print(f"Aucune action à acheter/vendre pour {stock}")

    return target_portfolio

# Récupérer les valeurs actuelles des actions
stock_values = get_stock_values(stocks)
print("Valeurs actuelles des actions :")
for stock, value in stock_values.items():
    print(f"{stock}: {value} USD")

# Demander à l'utilisateur le nombre d'actions qu'il possède
portfolio = get_user_portfolio(stocks)

# Calculer la valeur actuelle du portefeuille
portfolio_value = calculate_portfolio_value(portfolio, stock_values)
print(f"\nValeur totale actuelle du portefeuille: {portfolio_value} USD (ou EU ? à vérif sur yahoo) ")

# Rééquilibrer le portefeuille
rebalance_portfolio(portfolio, stock_values, portfolio_value)


"""import yfinance as yf

# Liste des 10 actions du portefeuille IDL (exemples)
stocks_test = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'MSFT', 'META', 'NFLX', 'NVDA', 'SPY', 'VTI']
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
    
    # Calculer la répartition cible pour chaque titre (basé sur sa valeur)
    target_percentages = {stock: stock_values[stock] / total_value for stock in stock_values}
    
    # Calculer la quantité idéale de chaque action à acheter/vendre
    target_portfolio = {}
    for stock in portfolio:
        target_value = total_value * target_percentages[stock]
        target_quantity = int(target_value // stock_values[stock])  # Arrondi à l'entier inférieur
        target_portfolio[stock] = target_quantity
    
    # Affichage des actions à acheter ou vendre
    for stock, target_quantity in target_portfolio.items():
        current_quantity = portfolio.get(stock, 0)
        if target_quantity > current_quantity:
            print(f"Acheter {target_quantity - current_quantity} actions de {stock}")
        elif target_quantity < current_quantity:
            print(f"Vendre {current_quantity - target_quantity} actions de {stock}")
        else:
            print(f"Aucune action à acheter/vendre pour {stock}")

    return target_portfolio

# Récupérer les valeurs actuelles des actions
stock_values = get_stock_values(stocks)
print("Valeurs actuelles des actions :")
for stock, value in stock_values.items():
    print(f"{stock}: {value} USD")

# Demander à l'utilisateur le nombre d'actions qu'il possède
portfolio = get_user_portfolio(stocks)

# Calculer la valeur actuelle du portefeuille
portfolio_value = calculate_portfolio_value(portfolio, stock_values)
print(f"\nValeur totale actuelle du portefeuille: {portfolio_value} USD")

# Rééquilibrer le portefeuille
rebalance_portfolio(portfolio, stock_values, portfolio_value)

"""