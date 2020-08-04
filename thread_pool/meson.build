
src_thread_pool = files(['clear.c', 'get_size.c', 'give_back.c', 'init.c', 'request.c', 'restore_affinity.c', 'set_affinity.c', 'set_size.c', 'wait.c', 'wake.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_thread_pool
else
  src_thread_pool += generated_headers
  thread_pool = static_library(
    'thread_pool',
    src_thread_pool,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += thread_pool
endif
