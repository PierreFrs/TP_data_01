#! /bin/bash

echo "Begin the installation of the backup system"
echo "Creating necessary directories..."
mkdir -p ../logs
mkdir -p ../data
mkdir -p ../data/archives
mkdir -p ../data/backup
mkdir -p ../data/mock_data
mkdir -p ../data/reports
mkdir -p ../data/reports/daily
mkdir -p ../data/reports/html
mkdir -p ../data/reports/json
mkdir -p ../data/work

echo "Giving execution rights to scripts..."
chmod 755 ./analyze.py ./archive.sh ./backup.sh ./daily_report.py ./watch.sh

echo "verifyng python3 installation..."
if command -v python3 &> /dev/null; then
    echo "Python3 is already installed: $(python3 --version)"

    echo "Checking for required Python packages..."
    if python3 -c "import pandas" &> /dev/null; then
        echo "Pandas is already installed..."
    else
        echo "Installing Pandas..."
        pip install pandas
    fi

    PYTHON_OK=true

else
    echo "Python3 is not installed on this system."
    read -pr "Do you want to install Python3? (Y/N): " confirm
    
    if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
        echo "Installing Python3..."
        
        # Install based on system
        if command -v apt-get &> /dev/null; then
            sudo apt-get update && sudo apt-get install -y python3 python3-pip
        elif command -v yum &> /dev/null; then
            sudo yum install -y python3 python3-pip
        elif command -v brew &> /dev/null; then
            brew install python3
        else
            echo "Please install Python3 manually for your system."
            exit 1
        fi
        
        echo "Installing required Python packages..."
        pip3 install pandas
        
        echo "Python3 installed successfully!"
        PYTHON_OK=true
    else
        echo "Python3 is required for this system. Installation cancelled."
        exit 1
    fi
fi

if [[ $PYTHON_OK == true ]]; then
    echo "Creating test_files..."
    touch "../data/mock_data/test.csv"
    touch "../data/mock_data/test.txt"

    echo "'then','exercise','duty','we','mouse','slide'
    'she','spread','about','everything','meat','touch'
    'with','result','answer','map','how','telephone'
    'upper','strange','mother','joy','pilot','throughout'
    'without','simple','too','room','popular','pilot'
    'tip','western','four','molecular','locate','neck'
    'poem','development','gulf','forgot','purple','deer'" > "../data/mock_data/test.csv"
    echo "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." > "../data/mock_data/test.txt"

    cp "../data/mock_data/test.csv" "../data/work/"
    cp "../data/mock_data/test.txt" "../data/work/"

    echo "Installation completed successfully!"
    echo "Test files created in ../data/work/ directory"
    echo "You can start the program by typing './startup.sh' in the installation directory."
else
    echo "Installation failed due to Python3 requirements."
    exit 1
fi