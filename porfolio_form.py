
stocks = []
stocks_dict = {}

# Fonction pour demander à l'utilisateur quel ticker et combien d'actions
def get_user_portfolio(stocks):
    portfolio = {}
    print("Entrez le ticker et le nombre d'actions que vous possédez pour chaque titre :")
    
    while True:
        # Demander le ticker de l'action
        ticker = input("Quel titre possédez-vous (ticker) ? ")
        
        # Vérifier si le ticker est valide
        if ticker not in stocks_dict:
            print(f"Erreur : Le ticker {ticker} n'est pas valide ou indisponible. Essayez à nouveau.")
            continue  # Demander à nouveau le ticker
        
        # Si le ticker est valide, afficher le nom de l'entreprise
        company_name = stocks_dict[ticker]
        print(f"Vous avez sélectionné {company_name}.")
        
        while True:
            # Demander la quantité d'actions
            try:
                quantity = int(input(f"Combien d'actions de {company_name} possédez-vous ? "))
                if quantity < 1:
                    raise ValueError("Le nombre d'actions doit être supérieur ou égal à 1.")
                portfolio[ticker] = quantity
                break  # Sortir de la boucle si la quantité est valide
            except ValueError as e:
                print(f"Entrée invalide : {e}. Veuillez entrer un nombre entier supérieur ou égal à 1.")
        
        # Demander si l'utilisateur souhaite entrer un autre ticker
        another = input("Souhaitez-vous ajouter un autre titre ? (oui/non) ").lower()
        if another != 'oui':
            break  # Sortir de la boucle principale si l'utilisateur ne veut plus ajouter d'actions
    
    return portfolio

# Récupérer les informations du portefeuille de l'utilisateur
portfolio = get_user_portfolio(stocks)
print("\nVotre portefeuille :")
for ticker, quantity in portfolio.items():
    print(f"{stocks_dict[ticker]} ({ticker}): {quantity} actions")