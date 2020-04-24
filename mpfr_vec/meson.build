
src_mpfr_vec = ['add.c', 'clear.c', 'equal.c', 'init.c', 'randtest.c', 'scalar_mul_2exp.c', 'scalar_mul_mpfr.c', 'scalar_product.c', 'set.c', 'zero.c']

src_mpfr_vec += generated_headers

headers_mpfr_vec = files([])

headers += headers_mpfr_vec

mpfr_vec = static_library(
  'mpfr_vec',
  src_mpfr_vec,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
