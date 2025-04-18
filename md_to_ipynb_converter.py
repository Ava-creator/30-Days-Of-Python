import os
import subprocess

def convert_md_to_ipynb(root_dir):
    """
    Walk through root_dir recursively, convert all .md files to .ipynb using notedown.
    The output .ipynb file will be saved in the same directory as the .md file.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                md_path = os.path.join(dirpath, filename)
                ipynb_filename = filename[:-3] + '.ipynb'
                ipynb_path = os.path.join(dirpath, ipynb_filename)
                print(f"Converting {md_path} to {ipynb_path}...")
                try:
                    # Run notedown command: notedown input.md > output.ipynb
                    with open(ipynb_path, 'w', encoding='utf-8') as out_file:
                        subprocess.run(['notedown', md_path], stdout=out_file, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {md_path}: {e}")

if __name__ == '__main__':
    # Replace '.' with your target directory if needed
    target_directory = '.'
    convert_md_to_ipynb(target_directory)
