@echo off
chcp 65001 > nul
echo ========================================================
echo    토목기사 5개년 기출·해설 CBT 웹 서버 시작기
echo ========================================================
echo.
echo 웹 서버를 시작하는 중입니다...
start http://localhost:8080
python server.py
pause
