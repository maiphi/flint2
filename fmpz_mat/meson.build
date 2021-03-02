
src_fmpz_mat = files(['CRT_ui.c', 'add.c', 'can_solve_multi_mod_den.c', 'charpoly_berkowitz.c', 'charpoly_modular.c', 'chol_d.c', 'clear.c', 'col_partition.c', 'concat_horizontal.c', 'concat_vertical.c', 'content.c', 'det.c', 'det_bareiss.c', 'det_bound.c', 'det_cofactor.c', 'det_divisor.c', 'det_modular.c', 'det_modular_accelerated.c', 'det_modular_given_divisor.c', 'equal.c', 'fflu.c', 'find_pivot_any.c', 'find_pivot_smallest.c', 'fprint.c', 'fread.c', 'get_d_mat.c', 'get_d_mat_transpose.c', 'get_mpf_mat.c', 'get_nmod_mat.c', 'gram.c', 'hadamard.c', 'hnf.c', 'hnf_classical.c', 'hnf_minors.c', 'hnf_minors_transform.c', 'hnf_modular.c', 'hnf_modular_eldiv.c', 'hnf_pernet_stein.c', 'hnf_transform.c', 'hnf_xgcd.c', 'howell_form_mod.c', 'init.c', 'init_set.c', 'inlines.c', 'inv.c', 'is_hadamard.c', 'is_in_hnf.c', 'is_in_rref_with_rank.c', 'is_in_snf.c', 'is_one.c', 'is_reduced.c', 'is_reduced_gram.c', 'is_reduced_gram_with_removal.c', 'is_reduced_with_removal.c', 'is_zero.c', 'kronecker_product.c', 'lll_original.c', 'lll_storjohann.c', 'max_bits.c', 'minpoly_modular.c', 'mul.c', 'mul_classical.c', 'mul_classical_inline.c', 'mul_multi_mod.c', 'mul_strassen.c', 'multi_CRT_ui.c', 'multi_mod_ui.c', 'neg.c', 'next_col_van_hoeij.c', 'nullspace.c', 'one.c', 'pow.c', 'randajtai.c', 'randbits.c', 'randdet.c', 'randintrel.c', 'randntrulike.c', 'randntrulike2.c', 'randops.c', 'randpermdiag.c', 'randrank.c', 'randsimdioph.c', 'randtest.c', 'randtest_unsigned.c', 'rank.c', 'rank_small_inplace.c', 'rref.c', 'rref_fflu.c', 'rref_mod.c', 'rref_mul.c', 'scalar_addmul_fmpz.c', 'scalar_addmul_nmod_mat_fmpz.c', 'scalar_addmul_nmod_mat_ui.c', 'scalar_addmul_si.c', 'scalar_addmul_ui.c', 'scalar_divexact_fmpz.c', 'scalar_divexact_si.c', 'scalar_divexact_ui.c', 'scalar_mod_fmpz.c', 'scalar_mul_2exp.c', 'scalar_mul_fmpz.c', 'scalar_mul_si.c', 'scalar_mul_ui.c', 'scalar_smod.c', 'scalar_submul_fmpz.c', 'scalar_submul_si.c', 'scalar_submul_ui.c', 'scalar_tdiv_q_2exp.c', 'set.c', 'set_nmod_mat.c', 'set_nmod_mat_unsigned.c', 'similarity.c', 'snf.c', 'snf_diagonal.c', 'snf_iliopoulos.c', 'snf_kannan_bachem.c', 'solve.c', 'solve_bound.c', 'solve_cramer.c', 'solve_dixon.c', 'solve_dixon_den.c', 'solve_fflu.c', 'solve_fflu_precomp.c', 'solve_multi_mod_den.c', 'sqr.c', 'sqr_bodrato.c', 'strong_echelon_form_mod.c', 'sub.c', 'swap.c', 'trace.c', 'transpose.c', 'window_clear.c', 'window_init.c', 'zero.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz_mat
else
  src_fmpz_mat += generated_headers
  fmpz_mat = static_library(
    'fmpz_mat',
    src_fmpz_mat,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz_mat
endif
