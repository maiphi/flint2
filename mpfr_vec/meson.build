
src_mpfr_vec = files(['add.c', 'clear.c', 'equal.c', 'init.c', 'randtest.c', 'scalar_mul_2exp.c', 'scalar_mul_mpfr.c', 'scalar_product.c', 'set.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_mpfr_vec
else
  src_mpfr_vec += generated_headers
  mpfr_vec = static_library(
    'mpfr_vec',
    src_mpfr_vec,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += mpfr_vec
endif
