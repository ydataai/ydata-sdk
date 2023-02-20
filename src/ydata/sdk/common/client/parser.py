from html.parser import HTMLParser


class LinkExtractor(HTMLParser):

    link = False
    data = []

    def handle_starttag(self, tag: str, attr: list[str]):
        if tag.lower() == "a" and "href" in (k.lower() for k, v in attr):
            self.link = next(v for k, v in attr if k == "href")
