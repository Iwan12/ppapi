# Copyright (c) 2010 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


{
  'variables': {
    'chromium_code': 1,  # Use higher warning level.
  },
  'target_defaults': {
    'conditions': [
      # Linux shared libraries should always be built -fPIC.
      #
      # TODO(ajwong): For internal pepper plugins, which are statically linked
      # into chrome, do we want to build w/o -fPIC?  If so, how can we express
      # that in the build system?
      ['OS=="linux" or OS=="openbsd" or OS=="freebsd" or OS=="solaris"', {
        'cflags': ['-fPIC', '-fvisibility=hidden'],

        # This is needed to make the Linux shlib build happy. Without this,
        # -fvisibility=hidden gets stripped by the exclusion in common.gypi
        # that is triggered when a shared library build is specified.
        'cflags/': [['include', '^-fvisibility=hidden$']],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'ppapi_c',
      'type': 'none',
      'all_dependent_settings': {
        'include_dirs': [
           '..',
        ],
      },
      'sources': [
        'c/pp_completion_callback.h',
        'c/pp_cursor_type.h',
        'c/pp_errors.h',
        'c/pp_event.h',
        'c/pp_file_info.h',
        'c/pp_instance.h',
        'c/pp_module.h',
        'c/pp_point.h',
        'c/pp_rect.h',
        'c/pp_resource.h',
        'c/pp_size.h',
        'c/pp_stdint.h',
        'c/pp_var.h',
        'c/pp_video.h',
        'c/ppb.h',
        'c/ppb_audio.h',
        'c/ppb_audio_config.h',
        'c/ppb_audio_trusted.h',
        'c/ppb_buffer.h',
        'c/ppb_char_set.h',
        'c/ppb_core.h',
        'c/ppb_device_context_2d.h',
        'c/ppb_directory_reader.h',
        'c/ppb_file_chooser.h',
        'c/ppb_file_io.h',
        'c/ppb_file_io_trusted.h',
        'c/ppb_file_ref.h',
        'c/ppb_file_system.h',
        'c/ppb_find.h',
        'c/ppb_font.h',
        'c/ppb_graphics_3d.h',
        'c/ppb_image_data.h',
        'c/ppb_instance.h',
        'c/ppb_opengles.h',
        'c/ppb_testing.h',
        'c/ppb_url_loader.h',
        'c/ppb_url_request_info.h',
        'c/ppb_url_response_info.h',
        'c/ppb_url_util.h',
        'c/ppb_var.h',
        'c/ppb_video_decoder.h',
        'c/ppp.h',
        'c/ppp_class.h',
        'c/ppp_graphics_3d.h',
        'c/ppp_find.h',
        'c/ppp_instance.h',
        'c/ppp_printing.h',
        'c/ppp_scrollbar.h',
        'c/ppp_widget.h',
        'c/ppp_zoom.h',
      ],
    },
    {
      'target_name': 'ppapi_cpp_objects',
      'type': 'static_library',
      'dependencies': [
        'ppapi_c'
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'cpp/audio.cc',
        'cpp/audio.h',
        'cpp/audio_config.cc',
        'cpp/audio_config.h',
        'cpp/buffer.cc',
        'cpp/buffer.h',
        'cpp/completion_callback.h',
        'cpp/core.cc',
        'cpp/core.h',
        'cpp/device_context_2d.cc',
        'cpp/device_context_2d.h',
        'cpp/directory_entry.cc',
        'cpp/directory_entry.h',
        'cpp/directory_reader.cc',
        'cpp/directory_reader.h',
        'cpp/file_chooser.cc',
        'cpp/file_chooser.h',
        'cpp/file_io.cc',
        'cpp/file_io.h',
        'cpp/file_ref.cc',
        'cpp/file_ref.h',
        'cpp/file_system.cc',
        'cpp/file_system.h',
        'cpp/font.h',
        'cpp/font.cc',
        'cpp/graphics_3d.cc',
        'cpp/graphics_3d.h',
        'cpp/image_data.cc',
        'cpp/image_data.h',
        'cpp/instance.cc',
        'cpp/instance.h',
        'cpp/module.cc',
        'cpp/module.h',
        'cpp/module_impl.h',
        'cpp/paint_manager.cc',
        'cpp/paint_manager.h',
        'cpp/paint_aggregator.cc',
        'cpp/paint_aggregator.h',
        'cpp/point.h',
        'cpp/rect.cc',
        'cpp/rect.h',
        'cpp/resource.cc',
        'cpp/resource.h',
        'cpp/scriptable_object.cc',
        'cpp/scriptable_object.h',
        'cpp/scrollbar.cc',
        'cpp/scrollbar.h',
        'cpp/size.h',
        'cpp/url_loader.cc',
        'cpp/url_loader.h',
        'cpp/url_request_info.cc',
        'cpp/url_request_info.h',
        'cpp/url_response_info.cc',
        'cpp/url_response_info.h',
        'cpp/url_util.cc',
        'cpp/url_util.h',
        'cpp/var.cc',
        'cpp/var.h',
        'cpp/video_decoder.cc',
        'cpp/video_decoder.h',
        'cpp/widget.cc',
        'cpp/widget.h',
      ],
      'conditions': [
        ['OS=="win"', {
          'msvs_guid': 'AD371A1D-3459-4E2D-8E8A-881F4B83B908',
          'msvs_settings': {
            'VCCLCompilerTool': {
              'AdditionalOptions': ['/we4244'],  # implicit conversion, possible loss of data
            },
          },
        }],
        ['OS=="linux"', {
          'cflags': ['-Wextra', '-pedantic'],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'WARNING_CFLAGS': ['-Wextra', '-pedantic'], 
           },
        }]
      ],
    },
    {
      'target_name': 'ppapi_cpp',
      'type': 'static_library',
      'dependencies': [
        'ppapi_c',
        'ppapi_cpp_objects',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'cpp/module_embedder.h',
        'cpp/ppp_entrypoints.cc',
      ],
      'conditions': [
        ['OS=="win"', {
          'msvs_guid': '057E7FA0-83C0-11DF-8395-0800200C9A66',
        }],
        ['OS=="linux"', {
          'cflags': ['-Wextra', '-pedantic'],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'WARNING_CFLAGS': ['-Wextra', '-pedantic'],
           },
        }]
      ],
    },
    {
      'target_name': 'ppapi_example_skeleton',
      'type': 'none',
      'dependencies': [
        'ppapi_cpp',
      ],
      'export_dependent_setting': ['ppapi_cpp'],
      'direct_dependent_settings': {
        'product_name': '>(_target_name)',
        'conditions': [
          ['OS=="win"', {
            'type': 'shared_library',
            'msvs_guid': 'EE00E36E-9E8C-4DFB-925E-FBE32CEDB91B',
            'sources': [
              'example/example.rc',
            ],
            'run_as': {
              'action': [
                '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)chrome<(EXECUTABLE_SUFFIX)',
                '--register-pepper-plugins=$(TargetPath);application/x-ppapi-example',
                'file://$(ProjectDir)/example/example.html',
              ],
            },
          }],
          ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
            'type': 'shared_library',
            'cflags': ['-fvisibility=hidden'],
            # -gstabs, used in the official builds, causes an ICE. Simply remove
            # it.
            'cflags!': ['-gstabs'],
          }],
          ['OS=="mac"', {
            'type': 'loadable_module',
            'mac_bundle': 1,
            'product_extension': 'plugin',
            'xcode_settings': {
              'INFOPLIST_FILE': 'example/Info.plist',
            },
            'sources+': [
              'example/Info.plist'
            ],
          }],
        ],
        # See README for instructions on how to run and debug on the Mac.
        #'conditions' : [
        #  ['OS=="mac"', {
        #    'target_name' : 'Chromium',
        #    'type' : 'executable',
        #    'xcode_settings' : {
        #      'ARGUMENTS' : '--renderer-startup-dialog --internal-pepper --no-sandbox file://${SRCROOT}/test_page.html'
        #    },
        #  }],
        #],
      },
    },
    {
      'target_name': 'ppapi_example',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'example/example.cc',
      ],
    },
    #{
    #  'target_name': 'ppapi_example_device_context_2d',
    #  'dependencies': [
    #    'ppapi_example_skeleton',
    #  ],
    #  'sources': [
    #    'examples/2d/device_context_2d_example.c',
    #  ],
    #},
    {
      'target_name': 'ppapi_example_paint_manager',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/2d/paint_manager_example.cc',
      ],
    },
    {
      'target_name': 'ppapi_example_scroll',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/2d/scroll.cc',
      ],
    },
    {
      'target_name': 'ppapi_example_audio',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/audio/audio.cc',
      ],
    },
    {
      'target_name': 'ppapi_example_file_chooser',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/file_chooser/file_chooser.cc',
      ],
    },
    {
      'target_name': 'ppapi_example_simple_font',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/font/simple_font.cc',
      ],
    },
    {
      'target_name': 'ppapi_example_c_stub',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/stub/stub.c',
      ],
    },
    {
      'target_name': 'ppapi_example_cc_stub',
      'dependencies': [
        'ppapi_example_skeleton',
      ],
      'sources': [
        'examples/stub/stub.cc',
      ],
    },
    {
      'target_name': 'ppapi_tests',
      'type': 'loadable_module',
      'sources': [
        # Common test files.
        'tests/test_case.cc',
        'tests/test_case.h',
        'tests/test_instance.cc',
        'tests/test_instance.h',

        # Test cases.
        'tests/test_buffer.cc',
        'tests/test_buffer.h',
        'tests/test_char_set.cc',
        'tests/test_char_set.h',
        'tests/test_device_context_2d.cc',
        'tests/test_device_context_2d.h',
        'tests/test_file_ref.cc',
        'tests/test_file_ref.h',
        'tests/test_image_data.cc',
        'tests/test_image_data.h',
        'tests/test_paint_aggregator.cc',
        'tests/test_paint_aggregator.h',
        'tests/test_scrollbar.cc',
        'tests/test_scrollbar.h',
        'tests/test_url_loader.cc',
        'tests/test_url_loader.h',
        'tests/test_url_util.cc',
        'tests/test_url_util.h',
      ],
      'dependencies': [
        'ppapi_cpp'
      ],
      'conditions': [
        ['OS=="win"', {
          'defines': [
            '_CRT_SECURE_NO_DEPRECATE',
            '_CRT_NONSTDC_NO_WARNINGS',
            '_CRT_NONSTDC_NO_DEPRECATE',
            '_SCL_SECURE_NO_DEPRECATE',
          ],
        }],
        ['OS=="mac"', {
          'mac_bundle': 1,
          'product_name': 'ppapi_tests',
          'product_extension': 'plugin',
        }],
      ],
    },
  ],
}
