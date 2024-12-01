from typing import Dict


class DataStream:

    def __init__(self) -> None:
        """Initilaizes the DataStream object"""
        self.last_printed: Dict[str, int] = {}

    def should_output_data_str(self, timestamp: str, data_string: str) -> bool:
        """
        Checks if a data string should be printed based on the timestamp and on the given 5 seconds rule

        Args
        ----
        timestamp: int
            The timestamp of the incoming data string
        data_str: str
            The data string

        Returns
        -------
        bool:
            True if the data string should be printed, False otherwise
        """
        last_printed_time = self.last_printed.get(data_string)

        if last_printed_time is None or timestamp >= last_printed_time + 5:
            self.last_printed[data_string] = timestamp
            return True
        else:
            return False


data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=1, data_string="world"))
print(data_stream.should_output_data_str(timestamp=5, data_string="world"))
