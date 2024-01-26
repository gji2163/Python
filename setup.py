from distutils.core import setup
import py2exe

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [
        {'script': "WebNovel.py",
         "icon_resources": [(1, "ico.ico")]
         }],
    zipfile = None,
)
