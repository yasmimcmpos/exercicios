# Determine the date and time one gigasecond after a certain date.
# A gigasecond is one thousand million seconds.
# If you were born on January 24th, 2015 at 22:00,
# then you would be a gigasecond old on October 2nd, 2046 at 23:46:40

from datetime import datetime, timedelta


class GigasecondCalculator:
    """
    A class to calculate the date and time exactly one gigasecond (1,000,000,000 seconds)
    after a given starting datetime.
    """

    def __init__(self, start_date: datetime) -> None:
        """
        Initializes the calculator with a starting date.

        Args:
            start_date (datetime): The initial date and time to start the calculation from.
        """
        self.start_date = start_date
        self.gigasecond = timedelta(seconds=1_000_000_000)

    def __repr__(self) -> str:
        return f"GigasecondCalculator({self.start_date})"

    def calculate(self) -> datetime:
        """
        Calculates the datetime one gigasecond after the initial date.

        Returns:
            datetime: The resulting date and time.
        """
        return self.start_date + self.gigasecond
