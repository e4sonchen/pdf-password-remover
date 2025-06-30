@echo off
chcp 65001 >nul
echo ====================================
echo        PDF密碼移除工具
echo ====================================
echo.

cd /d "%~dp0"

if not exist ".venv" (
    echo 正在設置Python環境...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    pip install PyPDF2
) else (
    call .venv\Scripts\activate.bat
)

echo 啟動PDF密碼移除工具...
echo.
python remove_pdf_password.py

echo.
echo 按任意鍵退出...
pause >nul
