
src_fmpz_mod_mpoly = files(['ctx_clear.c', 'ctx_init.c', 'interp.c', 'mpolyn_gcd_brown.c', 'mpolyn_mpolyun.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mod_mpoly
else
  src_fmpz_mod_mpoly += generated_headers
  fmpz_mod_mpoly = static_library(
    'fmpz_mod_mpoly',
    src_fmpz_mod_mpoly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mod_mpoly
endif
