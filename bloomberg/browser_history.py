"""
    Question asked: Create a class for Browser history where it should have a URL visit function and display
    of Browser History visited. The only change here is that if a user is revisting any url,
    it should appear on top and previous entry should be deleted.

    Sample Test Case:

    Input :
    Insert("www.google.com")
    Insert("www.bing.com")
    Insert("www.facebook.com")
    Display()
    Insert("www.google.com")
    Insert("www.bloomberg.com")
    Display()
    Output:

    Display 1:
    www.facebook.com
    www.bing.com
    www.google.com

    Display 2:
    www.bloomberg.com
    www.google.com
    www.facebook.com
    www.bing.com
"""


class BrowserHistory:
    def __init__(self):
        self.history = {}

    def insert(self, url):
        if url in self.history:
            del self.history[url]
        self.history[url] = True

    def display(self):
        return list(reversed(self.history.keys()))


if __name__ == '__main__':
    browser = BrowserHistory()
    print(browser.insert("www.google.com"))
    print(browser.insert("www.bing.com"))
    print(browser.insert("www.facebook.com"))
    print(browser.display())
    print(browser.insert("www.google.com"))
    print(browser.insert("www.bloomberg.com"))
    print(browser.display())
