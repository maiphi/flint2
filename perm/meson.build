
src_perm = ['inlines.c', 'parity.c', 'randtest.c']

src_perm += generated_headers

headers_perm = files([])

headers += headers_perm

perm = static_library(
  'perm',
  src_perm,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
