# Create and activate virtual environment, then install requirements
python -m venv .venv
Write-Output "To activate the venv run: .\.venv\Scripts\Activate.ps1"
pip install --upgrade pip
pip install -r requirements.txt
