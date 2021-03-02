
src_fq_zech_mpoly = files(['add.c', 'combine_like_terms.c', 'ctx_change_modulus.c', 'ctx_clear.c', 'ctx_init.c', 'derivative.c', 'divides.c', 'divides_monagan_pearce.c', 'divrem.c', 'divrem_monagan_pearce.c', 'equal.c', 'evaluate_all.c', 'evaluate_one.c', 'fit_length.c', 'fit_length_reset_bits.c', 'fprint_pretty.c', 'gcd.c', 'gcd_cofactors.c', 'gen.c', 'get_coeff_vars_ui.c', 'get_set_fq_nmod_mpoly.c', 'get_set_nmod_mpoly.c', 'init.c', 'is_canonical.c', 'is_fq_zech.c', 'is_one.c', 'lead_coeff_vars.c', 'make_monic.c', 'mpolyu.c', 'mul.c', 'mul_johnson.c', 'neg.c', 'pow_rmul.c', 'repack_bits.c', 'scalar_addmul_fq_zech.c', 'scalar_mul_fq_zech.c', 'set.c', 'set_fq_zech.c', 'set_ui.c', 'sort_terms.c', 'sub.c', 'sub_fq_zech.c', 'univar.c', 'pow_ui.c', 'clear.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fq_zech_mpoly
else
  src_fq_zech_mpoly += generated_headers
  fq_zech_mpoly = static_library(
    'fq_zech_mpoly',
    src_fq_zech_mpoly,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fq_zech_mpoly
endif
