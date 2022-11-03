items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

print(int(wallet.strip('$')))

basket = []

for key, value in items_purchase.items()

for item in items_purchase:
    if item.strip('$') < int(wallet.strip)