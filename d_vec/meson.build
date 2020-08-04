
src_d_vec = files(['add.c', 'approx_equal.c', 'clear.c', 'dot.c', 'dot_heuristic.c', 'dot_thrice.c', 'equal.c', 'init.c', 'is_approx_zero.c', 'is_zero.c', 'norm.c', 'randtest.c', 'set.c', 'sub.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_d_vec
else
  src_d_vec += generated_headers
  d_vec = static_library(
    'd_vec',
    src_d_vec,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += d_vec
endif
