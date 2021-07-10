from cx_Freeze import setup, Executable


executables = [Executable('main.py', target_name='VkCheckCommunityBot.exe')]


excludes = ['pygame', 'unittest', 'tkinter', 'numpy', 'concurrent', 'distutils']

include_files = ['.env', 'sessions']


options = {'build_exe': {
      'include_msvcr': True,
      'excludes': excludes,
      'include_files': include_files,
      }
}


setup(name='VkCheckCommunityBot',
      version='1.0',
      description='чекаем паблик',
      executables=executables,
      options=options
      )
