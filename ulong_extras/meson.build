
src_ulong_extras = ['cbrt.c', 'cbrt_binary_search.c', 'cbrt_chebyshev_approximation.c', 'cbrt_estimate.c', 'cbrt_newton_iteration.c', 'cbrtrem.c', 'cleanup_primes.c', 'clog.c', 'compute_primes.c', 'discrete_log_bsgs.c', 'div2_preinv.c', 'divrem2_precomp.c', 'divrem2_preinv.c', 'euler_phi.c', 'factor.c', 'factor_SQUFOF.c', 'factor_ecm.c', 'factor_ecm_add.c', 'factor_ecm_double.c', 'factor_ecm_mul_montgomery_ladder.c', 'factor_ecm_select_curve.c', 'factor_ecm_stage_I.c', 'factor_ecm_stage_II.c', 'factor_insert.c', 'factor_lehman.c', 'factor_one_line.c', 'factor_partial.c', 'factor_pollard_brent.c', 'factor_power235.c', 'factor_pp1.c', 'factor_trial.c', 'factor_trial_partial.c', 'factor_trial_range.c', 'factorial_fast_mod2_preinv.c', 'factorial_mod2_preinv.c', 'flog.c', 'gcd.c', 'gcdinv.c', 'inlines.c', 'is_oddprime_binary.c', 'is_oddprime_small.c', 'is_perfect_power.c', 'is_perfect_power235.c', 'is_prime.c', 'is_prime_pocklington.c', 'is_prime_pseudosquare.c', 'is_probabprime.c', 'is_probabprime_BPSW.c', 'is_probabprime_fermat.c', 'is_probabprime_fibonacci.c', 'is_probabprime_lucas.c', 'is_square.c', 'is_squarefree.c', 'is_strong_probabprime2_preinv.c', 'is_strong_probabprime_precomp.c', 'jacobi.c', 'll_mod_preinv.c', 'lll_mod_preinv.c', 'mod2_precomp.c', 'mod2_preinv.c', 'mod_precomp.c', 'moebius_mu.c', 'mulmod_precomp.c', 'mulmod_precomp_shoup.c', 'mulmod_preinv.c', 'nextprime.c', 'nth_prime.c', 'nth_prime_bounds.c', 'pow.c', 'powmod2_preinv.c', 'powmod2_ui_preinv.c', 'powmod_precomp.c', 'powmod_ui_preinv.c', 'prime_inverses_arr_readonly.c', 'prime_pi.c', 'prime_pi_bounds.c', 'primes_arr_readonly.c', 'primes_clear.c', 'primes_extend_small.c', 'primes_init.c', 'primes_jump_after.c', 'primes_sieve_range.c', 'primitive_root_prime.c', 'randbits.c', 'randint.c', 'randlimb.c', 'randprime.c', 'randtest.c', 'remove.c', 'remove2_precomp.c', 'revbin.c', 'root.c', 'root_estimate.c', 'rootrem.c', 'sizeinbase.c', 'sqrt.c', 'sqrtmod.c', 'sqrtmod_primepow.c', 'sqrtmodn.c', 'sqrtrem.c', 'xgcd.c']

src_ulong_extras += generated_headers

headers_ulong_extras = files([])

headers += headers_ulong_extras

ulong_extras = static_library(
  'ulong_extras',
  src_ulong_extras,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
