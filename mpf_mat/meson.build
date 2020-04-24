
src_mpf_mat = ['approx_equal.c', 'clear.c', 'equal.c', 'gso.c', 'init.c', 'inlines.c', 'is_zero.c', 'mul.c', 'one.c', 'print.c', 'qr.c', 'randtest.c', 'set.c', 'swap.c', 'zero.c']

src_mpf_mat += generated_headers

headers_mpf_mat = files([])

headers += headers_mpf_mat

mpf_mat = static_library(
  'mpf_mat',
  src_mpf_mat,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
