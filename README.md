# QR Code Generator

This is a simple QR Code Generator built with Python's `tkinter` library and styled using the `ttkbootstrap` theme. The application allows users to create custom QR codes from text input and save them as PNG files in a folder named `QrCodes`. It also provides an option to delete all saved QR codes with a single click.

![Screenshot](img/screenshot.png)

## Features

- **Generate QR Codes**: Enter any text in the input field and generate a corresponding QR code.
- **Save QR Codes**: Automatically saves generated QR codes as PNG files in the `QrCodes` folder.
- **Display QR Codes**: View the generated QR code directly within the application.
- **Delete QR Codes**: Easily delete all QR codes stored in the `QrCodes` folder with one button click.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `ttkbootstrap`
  - `Pillow`
  - `qrcode`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/QRCodeGenerator.git
   ```
   
2. **Navigate to the project directory:**
   ```bash
   cd QRCodeGenerator
   ```

3. **Install the required Python libraries:**
   ```bash
   pip install tkinter ttkbootstrap Pillow qrcode
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

1. **Open the application**: Launch the app by running the Python script.

2. **Generate a QR Code**:
   - Enter the text in the input field.
   - Click the "Generate" button.
   - The generated QR code will be displayed in the application and saved in the `QrCodes` folder.

3. **Delete All QR Codes**:
   - Click the "Delete All QR Codes" button to remove all QR codes saved in the `QrCodes` folder.

    *!Atention!* Changes in the `QrCodes` folder will be only seen after the program is closed!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
