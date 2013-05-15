# -*- mode: python -*-
a = Analysis(['RegChek.py'],
             pathex=['/home/inblueswithu/Downloads/pyinstaller-2.0'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'RegChek'),
          debug=True,
          strip=None,
          upx=True,
          console=True )
