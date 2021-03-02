
src_fmpz_mod = files(['add.c', 'add_fmpz.c', 'addmul.c', 'ctx_clear.c', 'ctx_init.c', 'ctx_init_ui.c', 'discrete_log_pohlig_hellman.c', 'divides.c', 'equal_fmpz.c', 'inlines.c', 'inv.c', 'is_canonical.c', 'is_invertible.c', 'mul.c', 'mul_fmpz.c', 'neg.c', 'next_smooth_prime.c', 'pow_fmpz.c', 'pow_ui.c', 'rand.c', 'set_fmpz.c', 'set_modulus.c', 'set_modulus_ui.c', 'sub.c', 'sub_fmpz.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mod
else
  src_fmpz_mod += generated_headers
  fmpz_mod = static_library(
    'fmpz_mod',
    src_fmpz_mod,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mod
endif
