# DIRBUSTER-X

DIRBUSTER-X is a simple Python-based directory busting tool that helps in discovering hidden directories and files on a web server. It utilizes a wordlist to make HTTP requests and checks for the existence of directories or files based on the responses.

## Features

- **Directory Fuzzing**: Uses a wordlist to test various directory names.
- **Animated Console Output**: Displays an animated startup message for a dynamic user experience.
- **Status Reporting**: Outputs directories or files that respond with a 200 HTTP status code.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/dirbuster-x.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd dirbuster-x
   ```
3. **Install Required Packages**:
   Ensure you have Python installed. Install the required package using pip:
   ```bash
   pip install requests
   ```
## Usage
1. **Run the Script**:
   ```bash
   python dirbuster_x.py
   ```
   
2. **Input Required Information:**

**• URL**: Enter the URL of the target web server.
**• Wordlist Path**: Provide the path to the wordlist file.

3. **Example:**

   ```bash
    Enter the URL: http://example.com
    Enter the path of the wordlist: /path/to/wordlist.txt
   ```
## Wordlist Format
The wordlist should contain one word per line. For example:

  ```bash
  admin
  login
  dashboard
  ```
## Error Handling
**• File Not Found:** If the wordlist file does not exist, an error message will be displayed.
**• Other Errors:** Any other issues encountered during execution will be reported.

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please reach out to amachauhan0047@gmail.com.

## Author
Aman Chauhan

