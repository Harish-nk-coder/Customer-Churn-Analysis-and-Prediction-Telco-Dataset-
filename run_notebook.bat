@echo off
echo ========================================
echo Starting Jupyter Notebook...
echo ========================================
echo.
echo The notebook will open in your browser.
echo Close this window to stop the server.
echo.
cd /d "%~dp0"
python -m jupyter notebook Churn_Prediction_Colab.ipynb
pause

