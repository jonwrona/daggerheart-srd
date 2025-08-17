#!/usr/bin/env python3
"""Add source field to all Daggerheart YAML frontmatter"""

import os
from pathlib import Path

def add_source_to_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # Skip if no YAML frontmatter or source already exists
        if not content.strip().startswith('---') or 'source:' in content:
            return False
        
        lines = content.split('\n')
        yaml_end_index = -1
        
        # Find the closing --- of YAML frontmatter
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                yaml_end_index = i
                break
        
        if yaml_end_index == -1:
            return False
        
        # Insert source field before the closing ---
        lines.insert(yaml_end_index, 'source: "Daggerheart SRD - Adversaries"')
        
        # Write back to file
        new_content = '\n'.join(lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f'Error processing {file_path.name}: {e}')
        return False

def main():
    adversaries_dir = Path(r'C:\NextCloud\Obsidian\Gaming\daggerheart-srd\adversaries')
    md_files = list(adversaries_dir.glob('*.md'))
    
    updated = 0
    skipped = 0
    
    print(f"Processing {len(md_files)} files...")
    
    for file_path in sorted(md_files):
        if add_source_to_file(file_path):
            updated += 1
            print(f'Updated: {file_path.name}')
        else:
            skipped += 1
    
    print(f'\nSUMMARY:')
    print(f'   Updated: {updated}')
    print(f'   Skipped: {skipped}')
    print(f'   Total: {len(md_files)}')

if __name__ == "__main__":
    main()
