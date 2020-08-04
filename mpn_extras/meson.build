
src_mpn_extras = files(['debug.c', 'divides.c', 'divrem_preinvn.c', 'factor_trial.c', 'gcd_full.c', 'mod_preinvn.c', 'mulmod_2expp1_basecase.c', 'mulmod_preinvn.c', 'preinv1.c', 'preinvn.c', 'remove_2exp.c', 'remove_power.c', 'divrem_preinv1.c', 'factor_trial_tree.c', 'fmms1.c', 'mulmod_preinv1.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_mpn_extras
else
  src_mpn_extras += generated_headers
  mpn_extras = static_library(
    'mpn_extras',
    src_mpn_extras,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += mpn_extras
endif
