
src_mpfr_mat = ['clear.c', 'equal.c', 'init.c', 'mul_classical.c', 'randtest.c', 'set.c', 'swap.c', 'zero.c']

src_mpfr_mat += generated_headers

headers_mpfr_mat = files([])

headers += headers_mpfr_mat

mpfr_mat = static_library(
  'mpfr_mat',
  src_mpfr_mat,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
