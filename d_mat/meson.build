
src_d_mat = ['approx_equal.c', 'clear.c', 'equal.c', 'gso.c', 'init.c', 'inlines.c', 'is_approx_zero.c', 'is_zero.c', 'mul_classical.c', 'one.c', 'print.c', 'qr.c', 'randtest.c', 'set.c', 'swap.c', 'transpose.c', 'zero.c']

src_d_mat += generated_headers

headers_d_mat = files([])

headers += headers_d_mat

d_mat = static_library(
  'd_mat',
  src_d_mat,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
