# Data Fallacies 

This is a Streamlit app that demonstrates different data fallacies using a sample dataset of student grades and Seaborn visualizations.

[![Forks](https://img.shields.io/github/forks/hipnologo/data_fallacies)](https://github.com/hipnologo/data_fallacies/network/members)
[![Stars](https://img.shields.io/github/stars/hipnologo/data_fallacies)](https://github.com/hipnologo/data_fallacies/stargazers)
[![Issues](https://img.shields.io/github/issues/hipnologo/data_fallacies)](https://github.com/hipnologo/data_fallacies/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/hipnologo/data_fallacies)](https://github.com/hipnologo/data_fallacies/graphs/contributors)

## Installation

To install the dependencies, run:

``` pip install -r requirements.txt ```


## Usage

To run the app, run:

``` streamlit run app.py ```

This will start a local web server that you can access at `http://localhost:8501`.

## Data Fallacies

The app demonstrates the following data fallacies:

| Data Fallacy              | Description                                                                                                                                                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cherry Picking            | Selecting results that fit your claim and excluding those that don’t.                                                                                                                                                            |
| Cobra Effect              | Setting an incentive that accidentally produces the opposite result to the one intended. Also known as a Perverse Incentive.                                                                                                    |
| Sampling Bias             | Drawing conclusions from a set of data that isn’t representative of the population you’re trying to understand.                                                                                                                |
| Regression Towards the Mean | When something happens that’s unusually good or bad, it will revert back towards the average over time.                                                                                                                         |
| Overfitting               | Creating a model that’s overly tailored to the data you have and not representative of the general trend.                                                                                                                       |
| Data Dredging             | Repeatedly testing new hypotheses against the same set of data, failing to acknowledge that most correlations will be the result of chance.                                                                                      |
| False Causality           | Falsely assuming when two events appear related that one must have caused the other.                                                                                                                                              |
| Gambler’s Fallacy         | Mistakenly believing that because something has happened more frequently than usual, it’s now less likely to happen in future (and vice versa).                                                                                  |
| Simpson’s Paradox         | When a trend appears in different subsets of data but disappears or reverses when the groups are combined.                                                                                                                       |
| Publication Bias          | Interesting research findings are more likely to be published, distorting our impression of reality.                                                                                                                             |
| Survivorship Bias         | Drawing conclusions from an incomplete set of data, because that data has ‘survived’ some selection criteria.                                                                                                                    |
| Gerrymandering            | Manipulating the geographical boundaries used to group data in order to change the result.                                                                                                                                       |
| Hawthorne Effect          | The act of monitoring someone can affect their behaviour, leading to spurious findings. Also known as the Observer Effect.                                                                                                      |
| McNamara Fallacy          | Relying solely on metrics in complex situations and losing sight of the bigger picture.                                                                                                                                          |
| Danger of Summary Metrics | Only looking at summary metrics and missing big differences in the raw data.                                                                                                                                                      |

To see a demonstration of each fallacy, run the app and select a fallacy from the dropdown menu.

## Acknowledgements

This app was based on the Data Fallacies to Avoid article by [Visualcapitalist](https://www.visualcapitalist.com/here-are-15-common-data-fallacies-to-avoid). The dataset used in this app is synthetic and was created using NumPy. The plots were generated using Seaborn

## License

This app is licensed under the [MIT License](https://opensource.org/licenses/MIT).

<a href="https://www.buymeacoffee.com/hipnologod" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
