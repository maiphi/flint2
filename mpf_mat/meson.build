
src_mpf_mat = files(['approx_equal.c', 'clear.c', 'equal.c', 'gso.c', 'init.c', 'inlines.c', 'is_zero.c', 'mul.c', 'one.c', 'print.c', 'qr.c', 'randtest.c', 'set.c', 'swap.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_mpf_mat
else
  src_mpf_mat += generated_headers
  mpf_mat = static_library(
    'mpf_mat',
    src_mpf_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += mpf_mat
endif
