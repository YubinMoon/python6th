from urllib.request import urlopen
from html.parser import HTMLParser


class ImageParse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_list = []

    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        for name, value in attrs:
            if name == "src":
                self.image_list.append(value)


def parse_image(data):
    parser = ImageParse()
    parser.feed(data)
    data_set = set(x for x in parser.image_list)
    return data_set


def main():
    url = "https://www.google.com"
    with urlopen(url) as f:
        charset = f.headers.get_params("charset")[1][1]
        data = f.read().decode(charset)
    image_set = parse_image(data)
    print("\n>>>> Fetch Images From", url)
    print("\n".join(sorted(image_set)))


if __name__ == "__main__":
    main()
