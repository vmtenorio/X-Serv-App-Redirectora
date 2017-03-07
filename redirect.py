#/usr/bin/python3

import webapp
import random


class redirect(webapp.webApp):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        randomURL = random.randint(0,100000000)
        return ("303 See Other", "<html><head><meta http-equiv='Refresh' " +
                        "content='5;url=" + str(randomURL) + "'></head>" +
                        "<body><p>Seras redireccionado en 5 segundos o si haces click " +
                        "<a href='" + str(randomURL) + "'>aqui</a></p></body></html>")
if __name__ == "__main__":
    testRedirect = redirect("localhost", 1234)
