from html.parser import HTMLParser
from typing import Optional


class LinkExtractor(HTMLParser):
    """Simple HTML parser to extract the URL link from the client redirection
    response."""

    link: Optional[str] = None

    def handle_starttag(self, tag: str, attr: list[str]):
        if tag.lower() == "a" and "href" in (k.lower() for k, v in attr):
            self.link = next(v for k, v in attr if k == "href")
