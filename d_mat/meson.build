
src_d_mat = files(['approx_equal.c', 'clear.c', 'equal.c', 'init.c', 'inlines.c', 'is_approx_zero.c', 'is_zero.c', 'mul_classical.c', 'one.c', 'print.c', 'randtest.c', 'set.c', 'swap.c', 'transpose.c', 'zero.c', 'gso.c', 'qr.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_d_mat
else
  src_d_mat += generated_headers
  d_mat = static_library(
    'd_mat',
    src_d_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += d_mat
endif
