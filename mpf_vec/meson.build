
src_mpf_vec = ['add.c', 'approx_equal.c', 'clear.c', 'dot.c', 'dot2.c', 'equal.c', 'init.c', 'is_zero.c', 'norm.c', 'norm2.c', 'randtest.c', 'scalar_mul_2exp.c', 'scalar_mul_mpf.c', 'set.c', 'sub.c', 'zero.c']

src_mpf_vec += generated_headers

headers_mpf_vec = files([])

headers += headers_mpf_vec

mpf_vec = static_library(
  'mpf_vec',
  src_mpf_vec,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
