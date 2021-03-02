
src_fmpz_mpoly_factor = files(['add.c', 'bpoly.c', 'bpoly_factor.c', 'clear.c', 'cmp.c', 'compression.c', 'eval.c', 'expand.c', 'factor.c', 'factor_bound_si.c', 'factor_content.c', 'factor_squarefree.c', 'fit_length.c', 'gcd_algo.c', 'gcd_brown.c', 'gcd_zippel.c', 'gcd_zippel2.c', 'get_set_is_fmpz_poly.c', 'get_set_lead0.c', 'init.c', 'inlines.c', 'irred_wang.c', 'irred_zassenhaus.c', 'irred_zippel.c', 'lcc_kaltofen.c', 'lcc_wang.c', 'mpoly_hlift.c', 'mpoly_pfrac.c', 'mpolyl.c', 'mpolyv.c', 'print_pretty.c', 'realloc.c', 'set.c', 'sort.c', 'tpoly.c', 'tuple.c', 'gcd_brown_threaded.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mpoly_factor
else
  src_fmpz_mpoly_factor += generated_headers
  fmpz_mpoly_factor = static_library(
    'fmpz_mpoly_factor',
    src_fmpz_mpoly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mpoly_factor
endif
