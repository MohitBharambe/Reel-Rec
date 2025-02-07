@echo off
setlocal 
echo.
echo :::Reel-Rec Easy Installation Script:::

echo.
echo Reel-Rec requires MySQL and TMDB API credentials to be installed. 

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    exit /b 1
)

mysql --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: MySQL is not installed or not in PATH.
    exit /b 1
)

echo Enter the following details to proceed with the installation.
echo.
set /p MYSQL_USER=Enter MySQL username: 
set /p MYSQL_PASSWORD=Enter MySQL password: 
set /p BEARER_TOKEN=Enter TMDB API bearer token:

echo.
echo :::Installation Started:::
echo Creating virtual environment...
python -m venv .venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment.
    echo Run 'python -m venv .venv' to create the virtual environment & re run the script.
    exit /b 1
)
    

call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Error: Failed to activate virtual environment.
)


echo Installing dependencies, please wait...
echo This may take a few minutes.
python -m pip install -r requirements.txt > nul 2>&1  
if %errorlevel% neq 0 (
    echo Error: Failed to install required dependencies.
    exit /b 1
)

echo.
echo Creating database...
mysql -u %MYSQL_USER% -p%MYSQL_PASSWORD% -e "create database reel_rec;" > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Failed to create database, please check your MySQL credentials.
    exit /b 1
)

for /f "delims=" %%k in ('python -c "import secrets as s; print(s.token_urlsafe(32))"') do set SECRET_KEY=%%k

(
echo SECRET_KEY= '%SECRET_KEY%'
echo MYSQL_USER= '%MYSQL_USER%'
echo MYSQL_PASSWORD= '%MYSQL_PASSWORD%'
echo bearer_token= '%BEARER_TOKEN%'
) > .env

echo.
echo Generating model files...
echo This may take a few minutes. Hold on.
jupyter nbconvert --to notebook --execute Model\algorithm.ipynb > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Failed to generate model files, please check Jupyter Notebook installation.
    exit /b 1
)

echo.
echo Applying migrations...
python manage.py makemigrations > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Failed to make migrations.
    exit /b 1
)
python manage.py migrate > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Failed to apply migrations.
    exit /b 1
)

echo.
echo :::Installation was Successful!:::

echo.
set /p START=Do you want to Launch Reel-Rec? (y/n): 
if /i "%START%"=="y" (
    start "" http://127.0.0.1:8000/
    python manage.py runserver
    if %errorlevel% neq 0 (
        echo Error: Failed to start the application.
        exit /b 1
    )
) else (
    echo You can start Reel-Rec later by running 'python manage.py runserver'.
)
    exit /b 0

endlocal