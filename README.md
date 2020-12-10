# image-stego
Least Significant Bit Steganography with Python and Pillow

## Usage
1. Clone the git repository and navigate into its directory.
```console
git clone https://github.com/JosCla/SimpleSoko && cd SimpleSoko
```
2. Run the program.
- For encryption:
```console
python3 lsb-stego.py
```
- For decryption:
```console
python3 de-lsb-stego.py
```
3. Follow the directions provided by the program.
- Encryption will ask where the initial image is, what to hide in it, and where to put the final image.
- Decryption will ask where the image with a hidden message is, and how many bytes of information to look for.
