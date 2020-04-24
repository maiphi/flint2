
src_double_extras = ['inlines.c', 'is_nan.c', 'lambertw.c', 'log2.c', 'randtest.c', 'randtest_signed.c', 'randtest_special.c']

src_double_extras += generated_headers

headers_double_extras = files([])

headers += headers_double_extras

double_extras = static_library(
  'double_extras',
  src_double_extras,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
