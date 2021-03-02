#!/usr/bin/env python3

# BUILD_DIRS, TEMPLATE_DIRS, SOURCES from FLINT's CMakeLists.txt

build_dirs = [
    'aprcl', 'ulong_extras', 'long_extras', 'perm', 'fmpz', 'fmpz_vec',
    'fmpz_poly', 'fmpq_poly', 'fmpz_mat', 'fmpz_lll', 'mpfr_vec', 'mpfr_mat',
    'mpf_vec', 'mpf_mat', 'nmod_vec', 'nmod_poly', 'nmod_poly_factor', 'arith',
    'mpn_extras', 'nmod_mat', 'fmpq', 'fmpq_vec', 'fmpq_mat', 'padic',
    'fmpz_poly_q', 'fmpz_poly_mat', 'nmod_poly_mat', 'fmpz_mod_poly',
    'fmpz_mod_mat', 'fmpz_mod_poly_factor', 'fmpz_factor', 'fmpz_poly_factor',
    'fft', 'qsieve', 'double_extras', 'd_vec', 'd_mat', 'padic_poly',
    'padic_mat', 'qadic', 'fq', 'fq_vec', 'fq_mat', 'fq_poly', 'fq_poly_factor',
    'fq_nmod', 'fq_nmod_vec', 'fq_nmod_mat', 'fq_nmod_poly',
    'fq_nmod_poly_factor', 'fq_zech', 'fq_zech_vec', 'fq_zech_mat',
    'fq_zech_poly', 'fq_zech_poly_factor', 'thread_pool', 'fmpz_mod',
    'fmpz_mod_vec', 'n_poly', 'mpoly', 'fmpz_mpoly', 'fmpq_mpoly', 'nmod_mpoly',
    'fq_nmod_mpoly', 'fmpz_mod_mpoly', 'fmpz_mpoly_factor', 'fmpq_mpoly_factor',
    'nmod_mpoly_factor', 'fmpz_mod_mpoly_factor', 'fq_nmod_mpoly_factor',
    'fq_zech_mpoly', 'fq_zech_mpoly_factor', 'flintxx']

# Not built by CMake build system:
# ['fq_embed', 'fq_embed_templates', 'fq_nmod_embed', 'fq_zech_embed']

template_dirs = [
    'fq_vec_templates', 'fq_mat_templates', 'fq_poly_templates',
    'fq_poly_factor_templates', 'fq_templates']

sources = [
    'printf.c', 'fprintf.c', 'sprintf.c', 'scanf.c', 'fscanf.c', 'sscanf.c',
    'clz_tab.c', 'memory_manager.c', 'version.c', 'profiler.c',
    'thread_support.c', 'exception.c', 'hashmap.c', 'inlines.c', 'fmpz/fmpz.c']

# The auto-generated file fmpz.c will be added later.
sources.remove('fmpz/fmpz.c')

# <dirname>/meson.build
meson_subdir_tmpl = """
src_{dirname} = files({src})

headers += files({headers})

if meson.version().version_compare('>=0.55.0')
  src += src_{dirname}
else
  src_{dirname} += generated_headers
  {dirname} = static_library(
    '{dirname}',
    src_{dirname},
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += {dirname}
endif
"""

# include/flint/meson.build
meson_header = """
# Copy all header files to include/flint/, so that they can be included
# as <flint/header.h> before installation when FLINT is built as a subproject.

header_copies = []

if meson.version().version_compare('>=0.47.0')
  foreach h : headers
    header_copies += configure_file(
      input : h,
      output : '@PLAINNAME@',
      copy : true)
  endforeach
else
  foreach h : headers
    empty_conf = configuration_data()
    header_copies += configure_file(
      input : h,
      output : '@PLAINNAME@',
      configuration : empty_conf)
  endforeach
endif

install_headers(header_copies, subdir : 'flint')
"""

meson_root_tmpl = """
project(
  'flint',
  'c',
  version : 'git',
  license : 'LGPL 2.1',
  default_options : [
    'c_std=c11',
    'buildtype=release',
    'warning_level=1'])

# warning_level=0 doesn't exist in old Meson versions
override_warning_level = 'warning_level=1'

c_compiler = meson.get_compiler('c')

deps = [
  dependency('zlib', static : get_option('static')),
  dependency('threads', static : get_option('static'))]

# On some systems, gmp doesn't provide a pkg-config file.
gmp_dep = dependency('gmp', required : false, static : get_option('static'))
if not gmp_dep.found()
  gmp_dep = c_compiler.find_library('gmp', required : true, static : get_option('static'))
endif
deps += gmp_dep

# The same with mpfr.
mpfr_dep = dependency('mpfr', required : false, static : get_option('static'))
if not mpfr_dep.found()
  mpfr_dep = c_compiler.find_library('mpfr', required : true, static : get_option('static'))
endif
deps += mpfr_dep

if get_option('static')
  m_dep = c_compiler.find_library('m', required : false, static : true)
else
  m_dep = c_compiler.find_library('m', required : false)
endif
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
config_h = configure_file(output : 'flint-config.h', configuration : conf_data)

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

compiler_options = ['-Wno-unused-but-set-variable', '-funroll-loops', '-mpopcnt']
# -fno-fat-lto-objects for gcc is the default, if supported.
add_project_arguments('-Dflint_EXPORTS', language : 'c')
if not get_option('buildtype').startswith('debug')
  add_project_arguments('-DNDEBUG', language : 'c')
endif
foreach opt : compiler_options
  if c_compiler.has_argument(opt)
    add_project_arguments(opt, language : 'c')
  endif
endforeach

include_dir = include_directories('.')

src = files({sources})

src += fmpz_c

headers = files({headers})

headers += generated_headers_install

subdirs = {subdirs}
subdir_static_libs = []
foreach dirname : subdirs
  subdir(dirname)
endforeach
subdir('include/flint')

# Make sure the headers are copied to include/flint.
# If FLINT is built as a subproject, we need to copy the headers
# to include/flint in the build directory, so that the superproject
# finds them before they are installed.
src += header_copies
src += generated_headers

if meson.version().version_compare('>=0.55.0')
  # Meson 0.55 uses response files to circumvent command line length limits.
  if get_option('static')
    flint = static_library(
      'flint',
      src,
      dependencies : deps,
      override_options : [override_warning_level],
      install : true)
  else
    flint = library(
      'flint',
      src,
      dependencies : deps,
      override_options : [override_warning_level],
      install : true)
  endif
else
  # Use a workaround to avoid hitting command line length limits.
  # This way it is only possible to build a shared library.
  flint = shared_library(
    'flint',
    src,
    link_whole : subdir_static_libs,
    dependencies : deps,
    override_options : [override_warning_level],
    install : true)
endif

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

if meson.version().version_compare('>=0.54.0')
  meson.override_dependency('flint', flint_dep)
endif
"""

meson_options = """
option('static', type : 'boolean', value : false, yield : true,
       description : 'Use static dependencies.')
"""

import sys
import os
import argparse

parser = argparse.ArgumentParser(
    description='Meson build system generator for FLINT')

default_flint_dir = '.'
parser.add_argument(
    'flint_dir',
    nargs='?',
    default=default_flint_dir,
    help='The FLINT directory to generate the build system for (default: "' +
        default_flint_dir + '")')
parser.add_argument(
    'target_dir',
    nargs='?',
    default=None,
    help='The target directory to write the Meson build files to' +
        ' (default: same as flint_dir). Will be created if it doesn\'t exist,' +
        ' but not recursively.')

args = parser.parse_args()

flint_dir = args.flint_dir
target_dir = args.target_dir
if target_dir is None:
    target_dir = args.flint_dir

if not os.path.isdir(flint_dir):
    print('ERROR: FLINT directory "' + flint_dir + '" doesn\'t exist',
          file=sys.stderr)
    sys.exit(1)

for dirname in build_dirs + template_dirs:
    if not os.path.isdir(os.path.join(flint_dir, dirname)):
        print('ERROR: FLINT subdirectory "' + dirname + '" doesn\'t exist',
              file=sys.stderr)
        sys.exit(1)

if not os.path.isdir(target_dir):
    os.mkdir(target_dir)
if not os.path.isdir(os.path.join(target_dir, 'include')):
    os.mkdir(os.path.join(target_dir, 'include'))
if not os.path.isdir(os.path.join(target_dir, 'include', 'flint')):
    os.mkdir(os.path.join(target_dir, 'include', 'flint'))

with open(os.path.join(target_dir, 'meson.build'), 'w') as fh:
    headers = [f for f in os.listdir(flint_dir) if f.endswith('.h')]
    fh.write(meson_root_tmpl.format(
        sources=sources,
        headers=headers,
        subdirs=build_dirs + template_dirs))

with open(os.path.join(target_dir, 'include', 'flint', 'meson.build'), 'w') as fh:
    fh.write(meson_header)

with open(os.path.join(target_dir, 'meson_options.txt'), 'w') as fh:
    fh.write(meson_options)

for dirname in build_dirs + template_dirs:
    if not os.path.isdir(os.path.join(target_dir, dirname)):
        os.mkdir(os.path.join(target_dir, dirname))
    src = [f for f in os.listdir(os.path.join(flint_dir, dirname))
           if f.endswith('.c')]
    headers = [f for f in os.listdir(os.path.join(flint_dir, dirname))
               if f.endswith('.h')]
    meson_src = meson_subdir_tmpl.format(
        dirname=dirname, src=src, headers=headers)
    with open(os.path.join(target_dir, dirname, 'meson.build'), 'w') as fh:
        fh.write(meson_src)
