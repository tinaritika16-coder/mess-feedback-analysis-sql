## Deployment
Streamlit app can be deployed locally using streamlit run app.py

## Weekly Retraining & Maintenance

The machine learning models in this project will be retrained every week using updated mess feedback data.
Weekly retraining ensures that model predictions remain accurate with fresh data patterns.

Each retraining session will include:
- Generating new feedback data using `data_generator.py`
- Updating the SQL database
- Retraining models with `train_model.py`
- Saving updated model files (locally)
- Logging the maintenance in this section
- Pushing commits to GitHub to show retraining history

### Maintenance Log

- **08 Feb 2026:** Initial training & GitHub setup  
- **15 Feb 2026:** Weekly retraining completed (updated models)  
- **22 Feb 2026:** Weekly retraining completed (updated models)  


