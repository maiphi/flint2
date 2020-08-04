
src_fmpz_factor = files(['append.c', 'append_ui.c', 'clear.c', 'concat.c', 'ecm.c', 'ecm_add.c', 'ecm_addmod.c', 'ecm_clear.c', 'ecm_double.c', 'ecm_init.c', 'ecm_mul_montgomery_ladder.c', 'ecm_select_curve.c', 'ecm_stage_I.c', 'ecm_stage_II.c', 'ecm_submod.c', 'expand.c', 'expand_iterative.c', 'expand_multiexp.c', 'extend_factor_ui.c', 'factor.c', 'factor_no_trial.c', 'factor_pp1.c', 'factor_si.c', 'factor_smooth.c', 'factor_trial.c', 'factor_trial_range.c', 'fit_length.c', 'init.c', 'inlines.c', 'pollard_brent.c', 'pollard_brent_single.c', 'print.c', 'refine.c', 'set_length.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_factor
else
  src_fmpz_factor += generated_headers
  fmpz_factor = static_library(
    'fmpz_factor',
    src_fmpz_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_factor
endif
