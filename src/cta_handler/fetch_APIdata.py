import json
import ssl
import time

import click
import requests
from requests.adapters import HTTPAdapter


@click.command()
@click.option(
    "-k",
    "--key",
    "key",
    required=True,
    nargs=1,
    type=str,
    help="CTA API key",
)
@click.option(
    "-l",
    "--line",
    "line",
    required=True,
    nargs=1,
    type=click.Choice(
        choices=[
            "red",
            "blue",
            "brown",
            "green",
            "orange",
            "pink",
            "yellow",
        ]
    ),
    help="CTA L train line API endpoint to access",
)
def main(key: str, line: str) -> None:
    pass


current_time = time.localtime()
key = ""


class SSLAdapter(HTTPAdapter):
    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs["ssl_context"] = self.ssl_context
        return super().init_poolmanager(*args, **kwargs)


context = ssl.create_default_context()
context.set_ciphers("DEFAULT:@SECLEVEL=1")

session = requests.Session()
session.mount("https://", SSLAdapter(ssl_context=context))

# max mapid requests in a url is 4
LINES = {
    "red": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40900&mapid=41190&mapid=40100&mapid=41300&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40760&mapid=40880&mapid=&41380&mapid=41200&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40540&mapid=40080&mapid=41420&mapid=41320&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41220&mapid=40650&mapid=40630&mapid=41450&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40330&mapid=41660&mapid=41090&mapid=40560&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41490&mapid=41400&mapid=41000&mapid=40190&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41230&mapid=41170&mapid=40910&mapid=40990&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40240&mapid=41430&mapid=40450&outputType=JSON",
    ],
    "blue": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40890&mapid=40820&mapid=40230&mapid=40750&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41280&mapid=41330&mapid=40550&mapid=41240&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40060&mapid=41020&mapid=40570&mapid=40670&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40590&mapid=40320&mapid=41410&mapid=40490&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40380&mapid=40370&mapid=40790&mapid=40070&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41340&mapid=40430&mapid=40350&mapid=40470&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40810&mapid=40220&mapid=40250&mapid=40920&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40970&mapid=40010&mapid=40180&mapid=40980&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40390&outputType=JSON",
    ],
    "brown": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41290&mapid=41180&mapid=40870&mapid=41010&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41480&mapid=40090&mapid=41500&mapid=41460&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41440&mapid=41310&mapid=40360&mapid=41320&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41210&mapid=40530&mapid=41220&mapid=40660&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40800&mapid=40710&mapid=40450&mapid=40730&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40040&mapid=40680&mapid=40850&outputType=JSON",
    ],
    "green": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40020&mapid=41350&mapid=40610&mapid=41260&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40280&mapid=40700&mapid=40480&mapid=40030&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41670&mapid=41070&mapid=41360&mapid=40170&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41510&mapid=41160&mapid=40380&mapid=40260&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41700&mapid=40680&mapid=40850&mapid=41400&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=41120&mapid=40300&mapid=41270&mapid=41080&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40130&mapid=40510&mapid=40720&mapid=41140&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40290&outputType=JSON",
    ],
    "orange": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40930&mapid=40960&mapid=41150&mapid=40310&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40120&mapid=41060&mapid=41130&mapid=41400&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40850&mapid=40680&mapid=41700&mapid=40260&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40380&mapid=40040&mapid=40730&outputType=JSON",
    ],
    "pink": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40580&mapid=40420&mapid=40600&mapid=40150&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40780&mapid=41040&mapid=40440&mapid=40740&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40210&mapid=40830&mapid=41030&mapid=41700&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40260&mapid=40380&mapid=40680&mapid=40850&outputType=JSON",
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40040&mapid=40350&mapid=40470&outputType=JSON",
    ],
    "yellow": [
        f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&mapid=40140&outputType=JSON"
    ],
    # tracking information for all the starting route
    "rt_start": [
        f"https://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key={key}&rt=red&rt=Blue&rt=Brn&rt=G&rt=Org&rt=P&rt=Y&outputType=JSON"
    ],
}


def fetch_data(urls):
    combined_data = []
    for url in urls:
        response = session.get(url)
        response.raise_for_status()
        combined_data.append(response.json())
    return combined_data


def save_json(line_name, data, timestamp):
    filename = f"{line_name}/{line_name}_line_{timestamp}.json"
    with open(filename, "w") as json_file:
        json.dump({"combined_data": data}, json_file, indent=4)


if __name__ == "__main__":
    while True:
        timestamp = time.strftime("%m_%d_%H:%M", time.localtime())
        for line_name, urls in LINES.items():
            data = fetch_data(urls)
            save_json(line_name, data, timestamp)
        time.sleep(300)
