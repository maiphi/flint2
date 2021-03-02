
src_fq_zech_mpoly_factor = files(['bpoly.c', 'bpoly_factor_smprime.c', 'bpoly_hlift.c', 'clear.c', 'eval.c', 'factor.c', 'fit_length.c', 'get_set_is_fq_nmod_poly.c', 'get_set_lead0.c', 'init.c', 'irred_smprime_wang.c', 'irred_smprime_zassenhaus.c', 'irred_smprime_zippel.c', 'lcc_wang.c', 'mpoly_hlift.c', 'mpoly_pfrac.c', 'mpoly_univar.c', 'mpolyv.c', 'polyu.c', 'polyu3_hlift.c', 'polyun.c', 'print_pretty.c', 'realloc.c', 'tpoly.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_zech_mpoly_factor
else
  src_fq_zech_mpoly_factor += generated_headers
  fq_zech_mpoly_factor = static_library(
    'fq_zech_mpoly_factor',
    src_fq_zech_mpoly_factor,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_zech_mpoly_factor
endif
