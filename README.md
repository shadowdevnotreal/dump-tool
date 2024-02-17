![file-xQ5DoiGL7zbPC7wbL0i6Imls](https://github.com/shadowdevnotreal/dump-tool/assets/43219706/261f0dad-5262-4d71-a51c-3a28fb02424c)



# File Search Tool with GUI

This script provides a powerful file searching capability with an interactive graphical user interface, making it accessible for users who prefer GUIs over traditional command-line tools. It leverages Zenity for user inputs and selections, and `aha` for converting grep output to colored HTML, enhancing the readability of search results.

## Features

- **Interactive GUI**: Utilizes Zenity to offer a series of dialog boxes for:
  - Selecting files or directories to search within.
  - Entering the search term.
  - Choosing output formatting (colored or plain text).
  - Specifying the output file name.
- **Recursive Search**: Performs a recursive search for the specified term within files or directories, ensuring thorough content examination.
- **Flexible Output Formatting**: Offers the option to choose between colored HTML output and plain text, catering to different user preferences and needs.
- **Output File Customization**: Allows users to define the name and location of the output file where the search results will be saved.
- **Immediate Results Viewing**: Provides an option to open the output file in the default web browser immediately after the search operation, facilitating quick access to the results.

## Dependencies

- **Zenity**: For the graphical interface dialogs.
- **aha**: For converting grep output to colored HTML (optional based on user choice).
- **grep** and **find**: For searching within files and directories.

## Installation

Ensure you have Zenity, grep, and find installed on your system. If `aha` is not installed, the script attempts to install it using `pip3`. It's recommended to have Python3 and pip installed for this automatic installation to succeed.

## Usage

1. Make the script executable by running `chmod +x dumptool.sh`.
2. Execute the script by running `./dumptool.sh`.
3. Follow the GUI prompts to select your search criteria and output preferences.

## Contributing

Contributions to enhance the script's functionality or to add new features are welcome. Please feel free to fork the repository and submit a pull request.

## License

This script is released under the MIT License. See the LICENSE file for more details.
