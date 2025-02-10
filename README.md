# Markdown Converter

## Overview

The Markdown Converter is a desktop application designed to facilitate the conversion of Markdown text into various formats, including HTML, ODT (LibreOffice), and DOCX (Word). Built using Python and the Tkinter library, this application provides a user-friendly graphical user interface (GUI) that simplifies the conversion process. It leverages the `pypandoc` library to handle the conversion logic, ensuring compatibility with multiple output formats.

## Features

- **Markdown to HTML Conversion**: Convert Markdown text to HTML and preview the result directly within the application.
- **Markdown to ODT/DOCX Conversion**: Convert Markdown text to ODT or DOCX formats and save the output to a file.
- **Copy to Clipboard**: Easily copy the converted HTML text to the clipboard for quick sharing or integration into other applications.
- **Clear Input**: Clear the input text box with a single click, enhancing usability.


## Technical Details

### Architecture

The application follows a modular architecture, separating the GUI components from the conversion logic to promote code maintainability and scalability.

- **GUI Components**: Built using Tkinter and ttk for a modern and responsive user interface.
- **Conversion Logic**: Handled by the `pypandoc` library, which acts as a wrapper for Pandoc, a universal document converter.

### Dependencies

- **Python 3.x**: The application is developed and tested using Python 3.x.
- **Tkinter**: The standard Python interface to the Tk GUI toolkit, used for creating the graphical user interface.
- **pypandoc**: A Python wrapper for Pandoc, used for converting Markdown text to other formats.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/c-r-lewis/md-converter.git
   cd markdown-converter
   ```

2. **Install Dependencies**:
   ```bash
   pip install pypandoc
   ```

3. **Run the Application**:
   ```bash
   python markdown_converter.py
   ```

### Usage

1. **Paste Markdown Text**: Enter or paste your Markdown text into the input text box.
2. **Select Output Format**: Choose the desired output format from the dropdown menu (HTML, ODT, DOCX).
3. **Convert Text**: Click the "Convert Text" button to convert the Markdown text to the selected format.
   - For HTML, the converted text will be displayed in the output box.
   - For ODT and DOCX, you will be prompted to save the converted file to your desired location.
4. **Copy to Clipboard**: Use the "Copy to Clipboard" button to copy the converted HTML text.
5. **Clear Input**: Use the "Clear Input" button to clear the input text box.


### Acknowledgments

- This application uses the `pypandoc` library for converting Markdown text to other formats.
- The Tkinter library is used for creating the graphical user interface.

