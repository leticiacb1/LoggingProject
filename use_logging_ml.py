import logging
import numpy as np


class BaselineModel:
    """
    Baseline model. Return average value!
    """

    def __init__(self):
        self.model = None
        self.pred = None

    def fit(self, X, y):
        """
        Fit the model.
        """
        if len(y) < 30:
            logging.warning("y is small!")
        logging.info("Fitting model...")
        self.pred = np.average(y)

    def predict(self, X):
        """
        Predict the value.
        """
        return self.pred


def test_baseline_model():
    """
    Test if BaselineModel returns the correct value.
    """
    X = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([1, 2])
    model = BaselineModel()
    model.fit(X, y)

    # The average of [1,2] is 1.5!
    assert model.predict(X) == 1.5


def config_logging():
    """
    Configure Logging
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-18s %(name)-8s %(levelname)-8s %(message)s",
        datefmt="%y-%m-%d %H:%M",
        filename="baseline.log",
        filemode="a",
    )

    logging.basicConfig(level=logging.NOTSET)


if __name__ == "__main__":
    config_logging()
    test_baseline_model()
    
    # See logs in baseline.log file
