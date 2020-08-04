
src_fmpz_mod_mat = files(['add.c', 'clear.c', 'howell_form.c', 'init.c', 'init_set.c', 'inlines.c', 'mul.c', 'mul_classical_threaded.c', 'neg.c', 'randtest.c', 'rref.c', 'scalar_mul_fmpz.c', 'scalar_mul_si.c', 'scalar_mul_ui.c', 'sqr.c', 'strong_echelon_form.c', 'sub.c', 'trace.c', 'window_clear.c', 'window_init.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mod_mat
else
  src_fmpz_mod_mat += generated_headers
  fmpz_mod_mat = static_library(
    'fmpz_mod_mat',
    src_fmpz_mod_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mod_mat
endif
