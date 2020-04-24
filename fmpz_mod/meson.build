
src_fmpz_mod = ['add.c', 'ctx_clear.c', 'ctx_init.c', 'discrete_log_pohlig_hellman.c', 'divides.c', 'inlines.c', 'inv.c', 'is_canonical.c', 'mul.c', 'neg.c', 'next_smooth_prime.c', 'pow_fmpz.c', 'pow_ui.c', 'set_modulus.c', 'sub.c']

src_fmpz_mod += generated_headers

headers_fmpz_mod = files([])

headers += headers_fmpz_mod

fmpz_mod = static_library(
  'fmpz_mod',
  src_fmpz_mod,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
