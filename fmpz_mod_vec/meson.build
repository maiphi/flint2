
src_fmpz_mod_vec = files(['dot.c', 'mul.c', 'neg.c', 'scalar_div_fmpz_mod.c', 'scalar_mul_fmpz_mod.c', 'set_fmpz_vec.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mod_vec
else
  src_fmpz_mod_vec += generated_headers
  fmpz_mod_vec = static_library(
    'fmpz_mod_vec',
    src_fmpz_mod_vec,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mod_vec
endif
