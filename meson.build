
project(
  'flint',
  'c',
  version : 'git',
  license : 'LGPL 2.1',
  default_options : [
    'c_std=c11',
    'buildtype=release',
    'default_library=shared',
    'warning_level=0'])

if get_option('arch') != ''
  add_project_arguments('-march=' + get_option('arch'), language : 'c')
endif

c_compiler = meson.get_compiler('c')

deps = [dependency('zlib'), dependency('mpfr'), dependency('threads')]

# On some systems, gmp doesn't provide a pkg-config file.
gmp_dep = dependency('gmp', required : false)
if not gmp_dep.found()
  gmp_dep = c_compiler.find_library('gmp', required : true)
endif
deps += gmp_dep

m_dep = c_compiler.find_library('m', required : false)
if m_dep.found()
  deps += m_dep
endif

# NOTE: We only set preprocessor definitions that are actually used
# in FLINT's source code.

conf_data = configuration_data()
conf_data.set('HAVE_TLS', 1)
# TODO: What does HAVE_PTHREAD do?
# It's unset by the original CMake build system on my Linux machines.
# conf_data.set(HAVE_PTHREAD, 1)
conf_data.set10('HAVE_CPU_SET_T', build_machine.system() == 'linux')
conf_data.set('FLINT_REENTRANT', 1)
conf_data.set('FLINT_DLL', true)
config_h = configure_file(output : 'config.h', configuration : conf_data)

if c_compiler.sizeof('void *') == 8
  bits = '64'
else
  bits = '32'
endif

if meson.version().version_compare('>=0.47.0')
  # No need to distinguish MEMORY_MANAGER options; all input files are the same.
  fmpz_conversions_h = configure_file(
    input : 'fmpz-conversions-reentrant.in',
    output : 'fmpz-conversions.h',
    copy : true)
  # TODO: Does 'reentrant' work on all our target platforms?
  fmpz_c = configure_file(
    input : 'fmpz/link/fmpz_reentrant.c',
    output : 'fmpz.c',
    copy : true)
  fft_tuning_h = configure_file(
    input : 'fft_tuning' + bits + '.in',
    output : 'fft_tuning.h',
    copy : true)
else
  # Use an empty configuration data object to copy files,
  # because the copy option is only available in Meson >=0.47.
  empty_conf = configuration_data()
  fmpz_conversions_h = configure_file(
    input : 'fmpz-conversions-reentrant.in',
    output : 'fmpz-conversions.h',
    configuration : empty_conf)
  empty_conf = configuration_data()
  fmpz_c = configure_file(
    input : 'fmpz/link/fmpz_reentrant.c',
    output : 'fmpz.c',
    configuration : empty_conf)
  empty_conf = configuration_data()
  fft_tuning_h = configure_file(
    input : 'fft_tuning' + bits + '.in',
    output : 'fft_tuning.h',
    configuration : empty_conf)
endif

python = import('python').find_installation('python3')

python_code = '''
import sys
with open(sys.argv[1], 'r') as fh_in:
    with open(sys.argv[2], 'w') as fh_out:
        for line in fh_in:
            if line:
                print(line.replace(' ', ',').strip() + ',', file=fh_out)
'''

cpimport_h = custom_target(
  'CPimport.h',
  output : 'CPimport.h',
  input : 'qadic/CPimport.txt',
  command : [python, '-c', python_code, '@INPUT@', '@OUTPUT@'],
)

# add generated_headers to source lists to ensure their creation
generated_headers_install = [config_h, fft_tuning_h, fmpz_conversions_h]
generated_headers_noinstall = [cpimport_h]
generated_headers = generated_headers_install + generated_headers_noinstall

compiler_options = ['-funroll-loops', '-mpopcnt']
if get_option('lto')
  compiler_options += '-flto'
endif
# -fno-fat-lto-objects for gcc is the default, if supported.
add_project_arguments('-Dflint_EXPORTS', language : 'c')
add_project_arguments('-DNDEBUG', language : 'c')
foreach opt : compiler_options
  if c_compiler.has_argument(opt)
    add_project_arguments(opt, language : 'c')
  endif
endforeach
if '-flto' in compiler_options and c_compiler.has_link_argument('-flto')
  add_project_link_arguments('-flto', language : 'c')
endif

include_dir = include_directories('.')

src = ['printf.c', 'fprintf.c', 'sprintf.c', 'scanf.c', 'fscanf.c', 'sscanf.c', 'clz_tab.c', 'memory_manager.c', 'version.c', 'profiler.c', 'thread_support.c', 'exception.c', 'hashmap.c', 'inlines.c']

src += fmpz_c

headers = files(['NTL-interface.h', 'aprcl.h', 'arith.h', 'arithxx.h', 'd_mat.h', 'd_vec.h', 'double_extras.h', 'exception.h', 'fft.h', 'flint.h', 'flintxx.h', 'fmpq.h', 'fmpq_mat.h', 'fmpq_matxx.h', 'fmpq_mpoly.h', 'fmpq_poly.h', 'fmpq_polyxx.h', 'fmpq_vec.h', 'fmpqxx.h', 'fmpz.h', 'fmpz_factor.h', 'fmpz_factorxx.h', 'fmpz_lll.h', 'fmpz_mat.h', 'fmpz_matxx.h', 'fmpz_mod.h', 'fmpz_mod_mat.h', 'fmpz_mod_mpoly.h', 'fmpz_mod_poly.h', 'fmpz_mod_poly_factor.h', 'fmpz_mod_poly_factorxx.h', 'fmpz_mod_polyxx.h', 'fmpz_mpoly.h', 'fmpz_poly.h', 'fmpz_poly_factor.h', 'fmpz_poly_factorxx.h', 'fmpz_poly_mat.h', 'fmpz_poly_matxx.h', 'fmpz_poly_q.h', 'fmpz_poly_qxx.h', 'fmpz_polyxx.h', 'fmpz_vec.h', 'fmpz_vecxx.h', 'fmpzxx.h', 'fq.h', 'fq_embed.h', 'fq_embed_templates.h', 'fq_mat.h', 'fq_mat_templates.h', 'fq_nmod.h', 'fq_nmod_embed.h', 'fq_nmod_mat.h', 'fq_nmod_mpoly.h', 'fq_nmod_poly.h', 'fq_nmod_poly_factor.h', 'fq_nmod_vec.h', 'fq_poly.h', 'fq_poly_factor.h', 'fq_poly_factor_templates.h', 'fq_poly_templates.h', 'fq_templates.h', 'fq_vec.h', 'fq_vec_templates.h', 'fq_zech.h', 'fq_zech_embed.h', 'fq_zech_mat.h', 'fq_zech_poly.h', 'fq_zech_poly_factor.h', 'fq_zech_vec.h', 'gettimeofday.h', 'gmpcompat.h', 'hashmap.h', 'long_extras.h', 'longlong.h', 'mpf_mat.h', 'mpf_vec.h', 'mpfr_mat.h', 'mpfr_vec.h', 'mpn_extras.h', 'mpoly.h', 'nmod_mat.h', 'nmod_matxx.h', 'nmod_mpoly.h', 'nmod_poly.h', 'nmod_poly_factor.h', 'nmod_poly_mat.h', 'nmod_poly_matxx.h', 'nmod_polyxx.h', 'nmod_vec.h', 'nmod_vecxx.h', 'padic.h', 'padic_mat.h', 'padic_matxx.h', 'padic_poly.h', 'padic_polyxx.h', 'padicxx.h', 'perm.h', 'permxx.h', 'profiler.h', 'qadic.h', 'qadicxx.h', 'qsieve.h', 'templates.h', 'thread_pool.h', 'thread_support.h', 'ulong_extras.h'])

headers += generated_headers_install

subdirs = ['aprcl', 'ulong_extras', 'long_extras', 'perm', 'fmpz', 'fmpz_vec', 'fmpz_poly', 'fmpq_poly', 'fmpz_mat', 'fmpz_lll', 'mpfr_vec', 'mpfr_mat', 'mpf_vec', 'mpf_mat', 'nmod_vec', 'nmod_poly', 'nmod_poly_factor', 'arith', 'mpn_extras', 'nmod_mat', 'fmpq', 'fmpq_vec', 'fmpq_mat', 'padic', 'fmpz_poly_q', 'fmpz_poly_mat', 'nmod_poly_mat', 'fmpz_mod_poly', 'fmpz_mod_mat', 'fmpz_mod_poly_factor', 'fmpz_factor', 'fmpz_poly_factor', 'fft', 'qsieve', 'double_extras', 'd_vec', 'd_mat', 'padic_poly', 'padic_mat', 'qadic', 'fq', 'fq_vec', 'fq_mat', 'fq_poly', 'fq_poly_factor', 'fq_nmod', 'fq_nmod_vec', 'fq_nmod_mat', 'fq_nmod_poly', 'fq_nmod_poly_factor', 'fq_zech', 'fq_zech_vec', 'fq_zech_mat', 'fq_zech_poly', 'fq_zech_poly_factor', 'thread_pool', 'fmpz_mod', 'mpoly', 'fmpz_mpoly', 'fmpq_mpoly', 'nmod_mpoly', 'fq_nmod_mpoly', 'fmpz_mod_mpoly', 'flintxx', 'fq_vec_templates', 'fq_mat_templates', 'fq_poly_templates', 'fq_poly_factor_templates', 'fq_templates']
foreach dirname : subdirs
  subdir(dirname)
endforeach
subdir('include/flint')

# Make sure the headers are copied to include/flint.
src += header_copies
src += generated_headers_noinstall

subdir_static_libs = [aprcl, ulong_extras, long_extras, perm, fmpz, fmpz_vec, fmpz_poly, fmpq_poly, fmpz_mat, fmpz_lll, mpfr_vec, mpfr_mat, mpf_vec, mpf_mat, nmod_vec, nmod_poly, nmod_poly_factor, arith, mpn_extras, nmod_mat, fmpq, fmpq_vec, fmpq_mat, padic, fmpz_poly_q, fmpz_poly_mat, nmod_poly_mat, fmpz_mod_poly, fmpz_mod_mat, fmpz_mod_poly_factor, fmpz_factor, fmpz_poly_factor, fft, qsieve, double_extras, d_vec, d_mat, padic_poly, padic_mat, qadic, fq, fq_vec, fq_mat, fq_poly, fq_poly_factor, fq_nmod, fq_nmod_vec, fq_nmod_mat, fq_nmod_poly, fq_nmod_poly_factor, fq_zech, fq_zech_vec, fq_zech_mat, fq_zech_poly, fq_zech_poly_factor, thread_pool, fmpz_mod, mpoly, fmpz_mpoly, fmpq_mpoly, nmod_mpoly, fq_nmod_mpoly, fmpz_mod_mpoly, flintxx, fq_vec_templates, fq_mat_templates, fq_poly_templates, fq_poly_factor_templates, fq_templates]

flint = shared_library(
    'flint',
    src,
    link_whole : subdir_static_libs,
    dependencies : deps,
    override_options : ['warning_level=0'],
    install : true)

pkg = import('pkgconfig')
pkg.generate(
  flint,
  filebase : 'flint',
  name : 'FLINT',
  description : 'Fast Library for Number Theory')

# Dependency object to be used if FLINT is built as a subproject:
flint_dep = declare_dependency(
  include_directories : include_directories('include'),
  dependencies : deps,
  link_with : flint)
