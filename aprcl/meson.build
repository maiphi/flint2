
src_aprcl = files(['config_gauss.c', 'config_jacobi.c', 'f_table.c', 'is_mul_coprime.c', 'is_prime_aprcl.c', 'is_prime_divisors_in_residue.c', 'is_prime_final_division.c', 'is_prime_gauss.c', 'is_prime_jacobi.c', 'unity_zp_add.c', 'unity_zp_aut.c', 'unity_zp_aut_inv.c', 'unity_zp_auxiliary_routine.c', 'unity_zp_coeff_add.c', 'unity_zp_coeff_inc.c', 'unity_zp_coeff_set.c', 'unity_zp_copy.c', 'unity_zp_equal.c', 'unity_zp_init.c', 'unity_zp_is_unity.c', 'unity_zp_jacobi_sum.c', 'unity_zp_mul.c', 'unity_zp_mul11.c', 'unity_zp_mul2.c', 'unity_zp_mul3.c', 'unity_zp_mul5.c', 'unity_zp_mul7.c', 'unity_zp_mul_scalar.c', 'unity_zp_pow.c', 'unity_zp_pow_2k.c', 'unity_zp_pow_select_k.c', 'unity_zp_pow_sliding.c', 'unity_zp_print.c', 'unity_zp_reduce_cyclotomic.c', 'unity_zp_set_zero.c', 'unity_zp_sqr.c', 'unity_zp_sqr11.c', 'unity_zp_sqr2.c', 'unity_zp_sqr3.c', 'unity_zp_sqr5.c', 'unity_zp_sqr7.c', 'unity_zp_swap.c', 'unity_zpq_add.c', 'unity_zpq_clear.c', 'unity_zpq_coeff_add.c', 'unity_zpq_coeff_set.c', 'unity_zpq_copy.c', 'unity_zpq_equal.c', 'unity_zpq_gauss_sum.c', 'unity_zpq_gauss_sum_character_pow.c', 'unity_zpq_init.c', 'unity_zpq_is_p_unity.c', 'unity_zpq_mul.c', 'unity_zpq_mul_unity_p.c', 'unity_zpq_pow.c', 'unity_zpq_scalar_mul_fmpz.c', 'unity_zpq_scalar_mul_ui.c', 'unity_zpq_swap.c', 'utility.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_aprcl
else
  src_aprcl += generated_headers
  aprcl = static_library(
    'aprcl',
    src_aprcl,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += aprcl
endif
