
src_mpn_extras = ['debug.c', 'divides.c', 'divrem_preinv1.c', 'divrem_preinvn.c', 'factor_trial.c', 'factor_trial_tree.c', 'fmms1.c', 'gcd_full.c', 'mod_preinvn.c', 'mulmod_2expp1_basecase.c', 'mulmod_preinv1.c', 'mulmod_preinvn.c', 'preinv1.c', 'preinvn.c', 'remove_2exp.c', 'remove_power.c']

src_mpn_extras += generated_headers

headers_mpn_extras = files([])

headers += headers_mpn_extras

mpn_extras = static_library(
  'mpn_extras',
  src_mpn_extras,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
