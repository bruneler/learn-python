import pandas as pd
import plotly.graph_objects as go
import plotly.io as io
# import plotly.express as px

# import matplotlib.pyplot as plt

# Simple API
# Input an die API, die API gibt Output
# z.B. ein panda oder numpy instanz. Auf den API Output können nun
# API Methoden angewendet werden.

# REST API
# RE REpresentational S State T Transfer API's
# REST API's werden verwendet, um mit Webservices zu interagieren, z.B. Applikationen welche
# übers Internet aufgerufen werden.
# Set of Rules like
# 1. Kommunikation
# 2. Input oder Request
# 3. Output oder Response

# z.B REST API over HTTP
# Mein Input ist ein HTTP Request
# Der Output ist ein HTTP Response JSON File


# PyCoinGecko for CoinGecko API
# collects de BTC Price over the coingeckoAPI by id.
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()  # Creates the CoinGecko client object
bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin", vs_currency="usd", days=30)
print(type(bitcoin_data))
print(bitcoin_data)
bitcoin_price_data = bitcoin_data["prices"]  # Only the prices from the dictionary in an new dictionary

# Wir konvertieren nun das Dictionary mit der Panda Bibliothek in ein DataFrame
data = pd.DataFrame(bitcoin_price_data, columns=["TimeStamp", "Price"])
print(data)


# Das Datum ist in Unix-time. Also konvertieren wir es in ein besser lesbares Format um.
# Dazu verwenden wir die panda funktion to_datetime()
data["Date"] = pd.to_datetime(data["TimeStamp"], unit="ms")
print(data)

# Die Candlesticks dazu
candlestick_data = data.groupby(data.Date.dt.date).agg({"Price": ["min", "max", "first", "last"]})
print(candlestick_data)

# Wir nutzen plotly, um die Daten der candlesticks zu zeichnen und mit plot in einer HTML zu speichern.


fig = go.Figure(data=[go.Candlestick(x=candlestick_data.index,
                                     open=candlestick_data["Price"]["first"],
                                     high=candlestick_data["Price"]["max"],
                                     low=candlestick_data["Price"]["min"],
                                     close=candlestick_data["Price"]["last"])])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title="Date", yaxis_title="Price (USD $)",
                  title="Bitcoin Kerzenchart über die letzten 30 Tage")


# fig.show() # opens the browser shows the figure

go.Figure.write_html(fig, "bitcoin_candlestick_graph2.html")  # Variante 2 für html export
# plot(fig, filename="bitcoin_candlestick_graph.html")  # funktioniert nicht bei mir
fig.write_html("bitcoin_candlestick_graph.html")  # Variante 1 für html export.



