'''import yfinance as yf

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
rebalance_portfolio(portfolio, stock_values, portfolio_value)'''


'''
import tkinter as tk
from tkinter import messagebox
import yfinance as yf

# Liste des tickers
stocks_dict = {
    'OR.PA': 'L\'Oréal SA',
    'MC.PA': 'LVMH Moët Hennessy Louis Vuitton',
    'RI.PA': 'Pernod Ricard SA',
    'SW.PA': 'Sodexo',
    'CAP.PA': 'Capgemini SE',
    'TTE.PA': 'TotalEnergies SE',
    'SU.PA': 'Schneider Electric SE',
    'GPDNF': 'Danone',
    'AI.PA': 'Air Liquide S.A.',
    'AC.PA': 'Accor SA'
}

# Fonction pour récupérer la valeur actuelle de chaque action
def get_stock_values(stocks):
    stock_data = {}
    for stock in stocks:
        stock_data[stock] = yf.Ticker(stock).history(period='1d')['Close'].iloc[-1]
    return stock_data

# Fonction pour rééquilibrer le portefeuille
def rebalance_portfolio():
    portfolio = {}
    total_value = 0

    # Collecter les informations du portefeuille via les entrées utilisateur
    for stock in stocks_dict:
        quantity = entry_dict[stock].get()
        try:
            quantity = int(quantity)
            if quantity < 1:
                raise ValueError("Le nombre d'actions doit être supérieur ou égal à 1.")
            portfolio[stock] = quantity
            total_value += quantity * stock_values.get(stock, 0)
        except ValueError:
            messagebox.showerror("Erreur", f"Entrée invalide pour {stocks_dict[stock]}. Veuillez entrer un nombre entier positif.")
            return

    # Rééquilibrage simplifié
    target_percentages = 100 / len(stocks_dict)
    buy_list = []
    sell_list = []

    for stock in portfolio:
        target_value = total_value * (target_percentages / 100)
        target_quantity = int(target_value // stock_values[stock])
        
        current_quantity = portfolio.get(stock, 0)
        if target_quantity > current_quantity:
            buy_list.append((stocks_dict[stock], target_quantity - current_quantity))
        elif target_quantity < current_quantity:
            sell_list.append((stocks_dict[stock], current_quantity - target_quantity))

    # Affichage des résultats
    result_str = "Rééquilibrage du portefeuille :\n\n"
    
    result_str += "Actions à acheter :\n"
    for company_name, quantity in sorted(buy_list, key=lambda x: x[1], reverse=True):
        result_str += f"{company_name}: {quantity} actions\n"
    
    result_str += "\nActions à vendre :\n"
    for company_name, quantity in sorted(sell_list, key=lambda x: x[1], reverse=True):
        result_str += f"{company_name}: {quantity} actions\n"

    result_label.config(text=result_str)


# Fenêtre principale de l'application
root = tk.Tk()
root.title("Rééquilibrage du Portefeuille")

# Récupérer les valeurs des actions
stock_values = get_stock_values(stocks_dict.keys())

# Création des éléments de l'interface graphique
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_dict = {}  # Dictionnaire pour stocker les entrées utilisateur

# Ajouter des champs d'entrée pour chaque action
for stock in stocks_dict:
    label = tk.Label(frame, text=stocks_dict[stock])
    label.grid(row=len(entry_dict), column=0, sticky="w", padx=10, pady=5)
    
    entry = tk.Entry(frame)
    entry.grid(row=len(entry_dict), column=1, padx=10, pady=5)
    entry_dict[stock] = entry  # Ajouter l'entrée au dictionnaire

# Bouton pour lancer le rééquilibrage
rebalance_button = tk.Button(root, text="Rééquilibrer le portefeuille", command=rebalance_portfolio)
rebalance_button.pack(pady=10)

# Label pour afficher les résultats
result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
result_label.pack(padx=10, pady=10)

# Lancer l'interface graphique
root.mainloop()
'''

import tkinter as tk
from tkinter import messagebox
import yfinance as yf

# Liste des tickers et des noms d'entreprises
stocks_dict = {
    'OR.PA': 'L\'Oréal SA',
    'MC.PA': 'LVMH Moët Hennessy Louis Vuitton',
    'RI.PA': 'Pernod Ricard SA',
    'SW.PA': 'Sodexo',
    'CAP.PA': 'Capgemini SE',
    'TTE.PA': 'TotalEnergies SE',
    'SU.PA': 'Schneider Electric SE',
    'GPDNF': 'Danone',
    'AI.PA': 'Air Liquide S.A.',
    'AC.PA': 'Accor SA'
}

# Fonction pour récupérer la valeur actuelle de chaque action
def get_stock_values(stocks):
    stock_data = {}
    for stock in stocks:
        stock_data[stock] = yf.Ticker(stock).history(period='1d')['Close'].iloc[-1]
    return stock_data

# Fonction pour rééquilibrer le portefeuille
def rebalance_portfolio():
    portfolio = {}
    total_value = 0

    # Collecter les informations du portefeuille via les entrées utilisateur
    for stock in stocks_dict:
        ticker = entry_dict[stock].get()  # Récupérer le ticker de l'utilisateur
        if ticker not in stocks_dict:  # Vérifier si le ticker est valide
            messagebox.showerror("Erreur", f"Le ticker {ticker} est invalide. Essayez à nouveau.")
            return
        company_name = stocks_dict[ticker]  # Nom associé au ticker
        
        quantity = entry_quantity_dict[stock].get()
        try:
            quantity = int(quantity)
            if quantity < 1:
                raise ValueError("Le nombre d'actions doit être supérieur ou égal à 1.")
            portfolio[ticker] = quantity
            total_value += quantity * stock_values.get(ticker, 0)
        except ValueError:
            messagebox.showerror("Erreur", f"Entrée invalide pour {company_name}. Veuillez entrer un nombre entier positif.")
            return

    # Rééquilibrage simplifié
    target_percentages = 100 / len(stocks_dict)
    buy_list = []
    sell_list = []

    for stock in portfolio:
        target_value = total_value * (target_percentages / 100)
        target_quantity = int(target_value // stock_values[stock])
        
        current_quantity = portfolio.get(stock, 0)
        if target_quantity > current_quantity:
            buy_list.append((stocks_dict[stock], target_quantity - current_quantity))
        elif target_quantity < current_quantity:
            sell_list.append((stocks_dict[stock], current_quantity - target_quantity))

    # Affichage des résultats
    result_str = "Rééquilibrage du portefeuille :\n\n"
    
    result_str += "Actions à acheter :\n"
    for company_name, quantity in sorted(buy_list, key=lambda x: x[1], reverse=True):
        result_str += f"{company_name}: {quantity} actions\n"
    
    result_str += "\nActions à vendre :\n"
    for company_name, quantity in sorted(sell_list, key=lambda x: x[1], reverse=True):
        result_str += f"{company_name}: {quantity} actions\n"

    result_label.config(text=result_str)

# Fenêtre principale de l'application
root = tk.Tk()
root.title("Rééquilibrage du Portefeuille")

# Récupérer les valeurs des actions
stock_values = get_stock_values(stocks_dict.keys())

# Création des éléments de l'interface graphique
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_dict = {}  # Dictionnaire pour stocker les entrées de tickers
entry_quantity_dict = {}  # Dictionnaire pour stocker les quantités d'actions

# Ajouter des champs d'entrée pour chaque action
for stock in stocks_dict:
    label = tk.Label(frame, text=stocks_dict[stock])
    label.grid(row=len(entry_dict), column=0, sticky="w", padx=10, pady=5)
    
    entry_ticker = tk.Entry(frame)
    entry_ticker.insert(0, stock)  # Pré-remplir avec le ticker par défaut
    entry_ticker.grid(row=len(entry_dict), column=1, padx=10, pady=5)
    entry_dict[stock] = entry_ticker  # Ajouter l'entrée ticker au dictionnaire
    
    entry_quantity = tk.Entry(frame)
    entry_quantity.insert(0, "1")  # Par défaut, on met 1 action
    entry_quantity.grid(row=len(entry_dict), column=2, padx=10, pady=5)
    entry_quantity_dict[stock] = entry_quantity  # Ajouter l'entrée quantité au dictionnaire

# Bouton pour ajouter une nouvelle action
def add_action():
    new_ticker = entry_new_ticker.get()
    if new_ticker not in stocks_dict:
        messagebox.showerror("Erreur", f"Le ticker {new_ticker} n'est pas valide. Essayez à nouveau.")
        return
    # Ajouter une nouvelle ligne pour la nouvelle action
    new_row = len(entry_dict)
    label = tk.Label(frame, text=stocks_dict[new_ticker])
    label.grid(row=new_row, column=0, sticky="w", padx=10, pady=5)
    
    entry_ticker = tk.Entry(frame)
    entry_ticker.insert(0, new_ticker)  # Pré-remplir avec le ticker
    entry_ticker.grid(row=new_row, column=1, padx=10, pady=5)
    entry_dict[new_ticker] = entry_ticker  # Ajouter l'entrée ticker
    
    entry_quantity = tk.Entry(frame)
    entry_quantity.insert(0, "1")  # Par défaut, 1 action
    entry_quantity.grid(row=new_row, column=2, padx=10, pady=5)
    entry_quantity_dict[new_ticker] = entry_quantity  # Ajouter l'entrée quantité

# Champ de texte pour entrer un nouveau ticker
entry_new_ticker = tk.Entry(root)
entry_new_ticker.pack(pady=5)

# Bouton pour ajouter une action supplémentaire
add_button = tk.Button(root, text="Ajouter une action", command=add_action)
add_button.pack(pady=5)

# Bouton pour lancer le rééquilibrage
rebalance_button = tk.Button(root, text="Rééquilibrer le portefeuille", command=rebalance_portfolio)
rebalance_button.pack(pady=10)

# Label pour afficher les résultats
result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
result_label.pack(padx=10, pady=10)

# Lancer l'interface graphique
root.mainloop()
