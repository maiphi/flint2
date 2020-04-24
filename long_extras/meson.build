
src_long_extras = ['inlines.c', 'randint.c', 'randtest.c', 'sizeinbase.c']

src_long_extras += generated_headers

headers_long_extras = files([])

headers += headers_long_extras

long_extras = static_library(
  'long_extras',
  src_long_extras,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
