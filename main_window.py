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
        stock_data[stock] = round(yf.Ticker(stock).history(period='1d')['Close'].iloc[-1], 2)  # Arrondi à 2 décimales
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
            buy_list.append((stocks_dict[stock], target_quantity - current_quantity, stock_values[stock]))
        elif target_quantity < current_quantity:
            sell_list.append((stocks_dict[stock], current_quantity - target_quantity, stock_values[stock]))

    # Affichage des résultats
    result_str = f"Valeur totale du portefeuille : {total_value} USD\n\nRééquilibrage du portefeuille :\n\n"
    
    result_str += "Actions à acheter :\n"
    for company_name, quantity, value in sorted(buy_list, key=lambda x: x[1], reverse=True):
        result_str += f"{company_name}: {quantity} actions ({value} USD)\n"
    
    result_str += "\nActions à vendre :\n"
    for company_name, quantity, value in sorted(sell_list, key=lambda x: x[1], reverse=True):
        result_str += f"{company_name}: {quantity} actions ({value} USD)\n"

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
    entry.insert(0, "1")  # Valeur par défaut de 1 action
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
