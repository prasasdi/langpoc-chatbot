# Run application
Open pipenv by
```bash
pipenv shell
```
then
```bash
uvicorn app.main:app --reload
```

# Install dependencies
Compile `requirements.in` in
```bash
pip-compile requirements.in
```
then
```bash
pipenv install -r requirements.txt --pre --skip-lock
```