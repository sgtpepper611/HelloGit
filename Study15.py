import os
 
PROJECT_DIR = 'C:¥python-sgt'
SETTINGS_FILE = 'settings_ini'
 
print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))
