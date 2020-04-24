
src_d_vec = ['add.c', 'approx_equal.c', 'clear.c', 'dot.c', 'dot_heuristic.c', 'dot_thrice.c', 'equal.c', 'init.c', 'is_approx_zero.c', 'is_zero.c', 'norm.c', 'randtest.c', 'set.c', 'sub.c', 'zero.c']

src_d_vec += generated_headers

headers_d_vec = files([])

headers += headers_d_vec

d_vec = static_library(
  'd_vec',
  src_d_vec,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
