
src_fmpz_mod_mpoly = ['ctx_clear.c', 'ctx_init.c', 'interp.c', 'mpolyn_gcd_brown.c', 'mpolyn_mpolyun.c']

src_fmpz_mod_mpoly += generated_headers

headers_fmpz_mod_mpoly = files([])

headers += headers_fmpz_mod_mpoly

fmpz_mod_mpoly = static_library(
  'fmpz_mod_mpoly',
  src_fmpz_mod_mpoly,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
