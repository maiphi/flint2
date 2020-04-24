
src_fmpz_mod_mat = ['add.c', 'clear.c', 'howell_form.c', 'init.c', 'init_set.c', 'inlines.c', 'mul.c', 'mul_classical_threaded.c', 'neg.c', 'randtest.c', 'rref.c', 'scalar_mul_fmpz.c', 'scalar_mul_si.c', 'scalar_mul_ui.c', 'sqr.c', 'strong_echelon_form.c', 'sub.c', 'trace.c', 'window_clear.c', 'window_init.c']

src_fmpz_mod_mat += generated_headers

headers_fmpz_mod_mat = files([])

headers += headers_fmpz_mod_mat

fmpz_mod_mat = static_library(
  'fmpz_mod_mat',
  src_fmpz_mod_mat,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
