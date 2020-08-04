
src_mpfr_mat = files(['clear.c', 'equal.c', 'init.c', 'mul_classical.c', 'randtest.c', 'set.c', 'swap.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_mpfr_mat
else
  src_mpfr_mat += generated_headers
  mpfr_mat = static_library(
    'mpfr_mat',
    src_mpfr_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += mpfr_mat
endif
