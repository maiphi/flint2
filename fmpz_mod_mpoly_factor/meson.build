
src_fmpz_mod_mpoly_factor = files(['bpoly_factor_smprime.c', 'bpoly_hlift.c', 'clear.c', 'cmp.c', 'compression.c', 'eval.c', 'expand.c', 'factor.c', 'factor_content.c', 'factor_squarefree.c', 'fit_length.c', 'fmpz_mod_bpoly.c', 'fmpz_mod_mat_extras.c', 'fmpz_mod_poly_extras.c', 'fmpz_mod_poly_vec.c', 'fmpz_mod_pow_cache.c', 'gcd_algo.c', 'gcd_brown.c', 'gcd_hensel.c', 'gcd_zippel.c', 'gcd_zippel2.c', 'get_set_lead0.c', 'interp.c', 'irred_smprime_wang.c', 'irred_smprime_zassenhaus.c', 'irred_smprime_zippel.c', 'lcc_wang.c', 'mpoly_hlift.c', 'mpoly_hlift_zippel.c', 'mpoly_pfrac.c', 'mpolyn.c', 'mpolyn_divides.c', 'mpolyu.c', 'mpolyv.c', 'polyu3_mod_hlift.c', 'polyun.c', 'print_pretty.c', 'realloc.c', 'set_nmod_mpoly_factor.c', 'sort.c', 'stack.c', 'zip_helpers.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mod_mpoly_factor
else
  src_fmpz_mod_mpoly_factor += generated_headers
  fmpz_mod_mpoly_factor = static_library(
    'fmpz_mod_mpoly_factor',
    src_fmpz_mod_mpoly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mod_mpoly_factor
endif
