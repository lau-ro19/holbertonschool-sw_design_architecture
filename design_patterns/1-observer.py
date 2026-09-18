#!/usr/bin/env python3
"""Module implementing the Observer pattern with NewsSubject and observers."""


class NewsSubject:
    """Subject that broadcasts news events to subscribed observers."""

    def __init__(self):
        """Initialize the subject with an empty observer dictionary."""
        self._observers = {}

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to specific topics."""
        self._observers[observer] = topics

    def unsubscribe(self, observer):
        """Unsubscribe an observer from the subject."""
        if observer in self._observers:
            del self._observers[observer]

    def notify(self, topic, data):
        """Notify all observers interested in the given topic."""
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs events."""

    def update(self, topic, data):
        """Receive and print log event."""
        print("log:{}={}".format(topic, data))


class EmailObserver:
    """Observer that sends email notifications."""

    def update(self, topic, data):
        """Receive and print email event."""
        print("email:{}={}".format(topic, data))


class SmsObserver:
    """Observer that sends SMS notifications."""

    def update(self, topic, data):
        """Receive and print SMS event."""
        print("sms:{}={}".format(topic, data))


def main():
    """Main function to test the observer notification system."""
    news = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    news.subscribe(log_obs, topics={"sports", "breaking"})
    news.subscribe(email_obs, topics=None)
    news.subscribe(sms_obs, topics={"breaking"})

    news.notify("weather", "rain")
    news.notify("sports", "goal")
    news.notify("breaking", "alert")


if __name__ == "__main__":
    main()
    