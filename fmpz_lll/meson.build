
src_fmpz_lll = files(['advance_check_babai.c', 'advance_check_babai_heuristic_d.c', 'babai.c', 'check_babai.c', 'check_babai_heuristic.c', 'check_babai_heuristic_d.c', 'context_init.c', 'context_init_default.c', 'd_lll.c', 'heuristic_dot.c', 'is_reduced.c', 'is_reduced_d.c', 'is_reduced_d_with_removal.c', 'is_reduced_mpfr.c', 'is_reduced_mpfr_with_removal.c', 'is_reduced_with_removal.c', 'lll.c', 'lll_d.c', 'lll_d_heuristic.c', 'lll_d_heuristic_with_removal.c', 'lll_d_with_removal.c', 'lll_d_with_removal_knapsack.c', 'lll_mpf.c', 'lll_mpf2.c', 'lll_mpf2_with_removal.c', 'lll_mpf_with_removal.c', 'lll_with_removal.c', 'lll_with_removal_ulll.c', 'mpf2_lll.c', 'randtest.c', 'shift.c', 'storjohann_ulll.c', 'wrapper.c', 'wrapper_with_removal.c', 'wrapper_with_removal_knapsack.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_lll
else
  src_fmpz_lll += generated_headers
  fmpz_lll = static_library(
    'fmpz_lll',
    src_fmpz_lll,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_lll
endif
