
src_fq_nmod_mpoly_factor = files(['append.c', 'clear.c', 'cmp.c', 'compression.c', 'eval.c', 'expand.c', 'factor.c', 'factor_content.c', 'factor_squarefree.c', 'fit_length.c', 'get_set_is_fq_nmod_poly.c', 'get_set_lead0.c', 'init.c', 'inlines.c', 'irred_lgprime.c', 'irred_smprime_wang.c', 'irred_smprime_zassenhaus.c', 'irred_smprime_zippel.c', 'lcc_wang.c', 'mpoly_hlift.c', 'mpoly_pfrac.c', 'mpolyv.c', 'n_bpoly_fq.c', 'n_bpoly_fq_factor_lgprime.c', 'n_bpoly_fq_factor_smprime.c', 'n_bpoly_hlift.c', 'polyu.c', 'polyu3_hlift.c', 'polyun.c', 'print_pretty.c', 'realloc.c', 'set.c', 'sort.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_nmod_mpoly_factor
else
  src_fq_nmod_mpoly_factor += generated_headers
  fq_nmod_mpoly_factor = static_library(
    'fq_nmod_mpoly_factor',
    src_fq_nmod_mpoly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_nmod_mpoly_factor
endif
