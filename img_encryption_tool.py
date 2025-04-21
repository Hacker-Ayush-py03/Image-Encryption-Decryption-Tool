from PIL import Image

def process_image(input_path, output_path, key, mode):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    # Create a copy of pixel data to avoid overwriting during swapping
    original_pixels = [pixels[x, y] for y in range(height) for x in range(width)]

    for y in range(height):
        for x in range(width):
            idx = y * width + x
            swap_x = width - 1 - x
            swap_idx = y * width + swap_x

            if mode == 'encrypt':
                # XOR original pixel at swap position
                r, g, b = original_pixels[swap_idx]
                r_enc = r ^ key
                g_enc = g ^ key
                b_enc = b ^ key
                pixels[x, y] = (r_enc, g_enc, b_enc)
            elif mode == 'decrypt':
                # XOR original pixel at swap position
                r, g, b = original_pixels[swap_idx]
                r_dec = r ^ key
                g_dec = g ^ key
                b_dec = b ^ key
                pixels[x, y] = (r_dec, g_dec, b_dec)
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'")

    img.save(output_path)
    print(f"Image {mode}ed and saved to {output_path}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python3 img_encryption_tool.py <encrypt|decrypt> <input_image> <output_image> <key>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    try:
        key = int(sys.argv[4])
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Key must be an integer between 0 and 255.")
        sys.exit(1)

    process_image(input_file, output_file, key, mode)
