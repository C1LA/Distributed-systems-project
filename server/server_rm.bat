@echo off

rem Dynamically remove relevant server (3,4,5,6)
curl -X DELETE -H "Content-Type: application/json" -d "{\"n\": 1, \"hostnames\": [\"1\"]}" http://localhost:5000/rm