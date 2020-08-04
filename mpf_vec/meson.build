
src_mpf_vec = files(['add.c', 'approx_equal.c', 'clear.c', 'dot.c', 'dot2.c', 'equal.c', 'init.c', 'is_zero.c', 'norm.c', 'norm2.c', 'randtest.c', 'scalar_mul_2exp.c', 'scalar_mul_mpf.c', 'set.c', 'sub.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_mpf_vec
else
  src_mpf_vec += generated_headers
  mpf_vec = static_library(
    'mpf_vec',
    src_mpf_vec,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += mpf_vec
endif
