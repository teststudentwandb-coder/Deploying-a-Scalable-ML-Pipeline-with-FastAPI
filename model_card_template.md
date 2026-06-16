# Model Card

The goal of this model is to predict whether an individual makes 50K+ in USD or less.

## Model Details
The model in this project is a Random Forest Classifier with the default arguments.

## Intended Use
The model was created for a school project.

## Training Data
The training data is census data from UC Irvine ML repository and was extracted from US Census database for year 1994 

## Evaluation Data
The evaluation data comes from the same 1994 Census sample

## Metrics
We used precision, recall and F1-Score to evaluate this model. The metrics came to be:
    * Precision = 0.75
    * Recall = 0.64
    * F1-score = 0.69

## Ethical Considerations
Categorical slices were evaluated to assess potential bias in this model. You can examine slice_output.txt to obtain full results. For example, there were no major biases observed between males and females but one would need to assess specific groups of interest based on the use case. 

sex: Female, Count: 2,126
Precision: 0.7410 | Recall: 0.5279 | F1: 0.6165
sex: Male, Count: 4,387
Precision: 0.7485 | Recall: 0.6562 | F1: 0.6993

## Caveats and Recommendations
The model was built on the data obtain in 1994. If it was to be used today, it would need to be retrained and the classification threshold of 50K would potentially need to be adjusted because 50K in 2026 is not the same as 50K in 1994.