# Process this file with autoconf to produce a configure script.
AC_INIT(libreiser4/libreiser4.c)
AC_CANONICAL_HOST
AC_PREREQ(2.50)

AH_TEMPLATE([PACKAGE], [Define this to be the name of the package.])
AH_TEMPLATE([VERSION], [Define to the version of the package.])

AH_TEMPLATE([ENABLE_DEBUG], [Define for enable debug info.])
AH_TEMPLATE([HAVE_LIBUUID], [Define for enable libuuid using.])
AH_TEMPLATE([HAVE_LIBREADLINE], [Define for enable libreadline using.])

AH_TEMPLATE([LIBREISER4_MAX_INTERFACE_VERSION], [Define to the max interface version.])
AH_TEMPLATE([LIBREISER4_MIN_INTERFACE_VERSION], [Define to the min interface version.])

LIBREISER4_MAJOR_VERSION=1
LIBREISER4_MINOR_VERSION=2
LIBREISER4_MICRO_VERSION=2

LIBREISER4_INTERFACE_AGE=0
LIBREISER4_BINARY_AGE=0
LIBREISER4_VERSION=$LIBREISER4_MAJOR_VERSION.$LIBREISER4_MINOR_VERSION.$LIBREISER4_MICRO_VERSION

LT_RELEASE=$LIBREISER4_MAJOR_VERSION.$LIBREISER4_MINOR_VERSION

LT_CURRENT=`expr $LIBREISER4_MICRO_VERSION - $LIBREISER4_INTERFACE_AGE`
LT_REVISION=$LIBREISER4_INTERFACE_AGE
LT_AGE=`expr $LIBREISER4_BINARY_AGE - $LIBREISER4_INTERFACE_AGE`

AC_SUBST(LT_RELEASE)
AC_SUBST(LT_CURRENT)
AC_SUBST(LT_REVISION)
AC_SUBST(LT_AGE)

PACKAGE=reiser4progs
VERSION=$LIBREISER4_VERSION

AM_INIT_AUTOMAKE($PACKAGE, $VERSION)
AM_CONFIG_HEADER(config.h)
AM_MAINTAINER_MODE

AC_DEFINE_UNQUOTED(LIBREISER4_MAX_INTERFACE_VERSION, $LIBREISER4_BINARY_AGE)
AC_DEFINE_UNQUOTED(LIBREISER4_MIN_INTERFACE_VERSION, $LIBREISER4_INTERFACE_AGE)

# Macro for checking libaal
AC_DEFUN([AC_CHECK_LIBAAL],
[

AC_CHECK_LIB($1, aal_device_open, ,
	[AC_MSG_ERROR([lib$1 not found; install libaal available at \
http://www.namesys.com/snapshots])]
$4)

# Check for headers and library
AC_CHECK_HEADER(aal/libaal.h, ,
    	[AC_MSG_ERROR([<aal/libaal.h> not found])] 
$4)

AC_MSG_CHECKING(for lib$1 version = $2)

AC_TRY_LINK_FUNC(libaal_version,,
    	AC_MSG_RESULT(failed)
    	AC_MSG_ERROR([lib$1 can't execute test]))

# Get major, minor, and micro version from arg MINIMUM-VERSION
libaal_config_major_version=`echo $2 | \
    sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\1/'`
libaal_config_minor_version=`echo $2 | \
    sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\2/'`
libaal_config_micro_version=`echo $2 | \
    sed 's/\([[0-9]]*\).\([[0-9]]*\).\([[0-9]]*\)/\3/'`

OLD_CFLAGS=$CFLAGS
CFLAGS="$CFLAGS -static"
    
# Compare MINIMUM-VERSION with libaal version
AC_TRY_RUN([
#include <stdio.h>
#include <stdlib.h>
#include <aal/libaal.h>

int main() {
    	const char *version;    
    	int major, minor, micro;
	
    	if (!(version = libaal_version()))
		exit(1);
		
    	if (sscanf(version, "%d.%d.%d", &major, &minor, &micro) != 3) {
		printf("%s, bad version string\n", version);
		exit(1);
    	}
	
    	if ((major >= $libaal_config_major_version) &&
		((major == $libaal_config_major_version) && 
		(minor >= $libaal_config_minor_version)) &&
		((major == $libaal_config_major_version) && 
		(minor == $libaal_config_minor_version) && 
		(micro >= $libaal_config_micro_version))) 
    	{
		return 0;
    	}

    	printf("\nAn old version of libaal (%s) was found.\n",
		version);

    	printf("You need a libaal of the version %d.%d.%d or newer.\n", 
		$libaal_config_major_version, $libaal_config_minor_version, 
		$libaal_config_micro_version);

    	printf("You can get it at http://www.namesys.com/snapshots\n");
    	return 1;
}
], 
    	AC_MSG_RESULT(yes),
    	AC_MSG_RESULT(no) ; $4,
    	[echo $ac_n "cross compiling; assumed OK... $ac_c"])

CFLAGS=$OLD_CFLAGS

# Execute ACTION-IF-FOUND
$3])

AC_ARG_WITH(libaal,
	[  --with-libaal            prefix of where libaal was installed], ,
)

LIBS=""
CFLAGS="$CFLAGS"

if test x$with_libaal != x; then
    	LIBS="-L$with_libaal/lib"
	LDFLAGS="$LDFLAGS -L$with_libaal/lib"
    	CFLAGS="$CFLAGS -I$with_libaal/include"
    	CPPFLAGS="-I$with_libaal/include"
fi

AC_ARG_WITH(uuid,
    	[  --with-uuid              support uuid generating and checking], ,
        	with_uuid=yes
)

# Check for libuuid
if test "$with_uuid" = yes; then
    	OLD_LIBS="$LIBS"
    	LIBS=""
    	AC_CHECK_LIB(uuid, uuid_generate, ,
		AC_MSG_WARN(libuuid could not be found which is required \
for the --with-uuid
		)
		with_uuid=no
    	)

    	UUID_LIBS="$LIBS"
    	LIBS="$OLD_LIBS"
fi

AC_SUBST(UUID_LIBS)

AC_ARG_WITH(readline,
    	[  --with-readline          support fancy command line editing], ,
        	with_readline=yes
)

PROGS_LIBS=""

# Check for readline
if test "x$with_readline" = xyes; then
    	OLD_LIBS="$LIBS"
    	LIBS=""
    	AC_CHECK_LIB(readline, readline, ,
	    	AC_MSG_WARN(GNU Readline could not be found which is required \
for the --with-readline
	    	)
	    	with_readline=no,
	    	-lncurses
    	)
    	PROGS_LIBS="$PROGS_LIBS $LIBS"
    	LIBS="$OLD_LIBS"
fi

# Check for ncurses
if test "x$with_readline" = xyes; then
	OLD_LIBS="$LIBS"
	LIBS=""
	AC_SEARCH_LIBS(tgetent, ncurses, 
		PROGS_LIBS="$PROGS_LIBS $LIBS",
		AC_MSG_WARN(ncurses could not be found which is required for the \
--with-readline option (which is enabled by default).
		)
		with_readline=no
	)
	LIBS="$OLD_LIBS"
fi

AM_ENABLE_SHARED

PROGS_LDFLAGS=""

AC_ARG_ENABLE(full-static,
    	[  --enable-full-static     build all static], ,
		enable_full_static=no
)
if test x$enable_full_static = xyes; then
	PROGS_LDFLAGS=-all-static
fi

AC_ARG_ENABLE(part-static,
    	[  --enable-part-static     build all static but libc ], ,
		enable_part_static=no
)
if test x$enable_part_static = xyes; then
	PROGS_LDFLAGS="-Wl,-lc,-static -static"
fi

AC_ARG_ENABLE(Werror,
    	[  --enable-Werror          enable build with gcc -Werror ], ,
		enable_Werror=no
)

AC_ARG_ENABLE(debug, 
    	[  --enable-debug           enable asserts and debug information ], , 
		enable_debug=no
)

AC_ARG_ENABLE(libminimal,
    	[  --disable-libminimal     disable minimal footprint library ], ,
        	enable_libminimal=yes
)

AC_ARG_ENABLE(symlinks,
    	[  --disable-symlinks       disable symlinks support in minimal library ], ,
        	enable_symlinks=yes
)

AC_ARG_ENABLE(special,
    	[  --disable-special        disable special files support in minimal library ], ,
        	enable_special=yes
)

AC_ARG_ENABLE(r5_hash,
    	[  --disable-r5-hash        disable r5 hash plugin in minimal library ], ,
        	enable_r5_hash=yes
)

AC_ARG_ENABLE(fnv1_hash,
    	[  --disable-fnv1-hash      disable fnv1 hash plugin in minimal library ], ,
        	enable_fnv1_hash=yes
)

AC_ARG_ENABLE(rupasov_hash,
    	[  --disable-rupasov-hash   disable rupasov hash plugin in minimal library ], ,
        	enable_rupasov_hash=yes
)

AC_ARG_ENABLE(tea_hash,
    	[  --disable-tea-hash       disable tea hash plugin in minimal library ], ,
        	enable_tea_hash=yes
)

AC_ARG_ENABLE(deg_hash,
    	[  --enable-deg-hash        enable degenerate hash plugin in minimal library ], ,
        	enable_deg_hash=no
)

AC_ARG_ENABLE(short_keys,
    	[  --disable-short-keys     disable short keys in minimal library ], ,
        	enable_short_keys=yes
)

AC_ARG_ENABLE(large_keys,
    	[  --disable-large-keys     disable large keys in minimal library ], ,
        	enable_large_keys=yes
)

AC_ARG_ENABLE(dot_o_fibre,
	      [  --disable-dot_o_fibre     disable dot_o_fibre plugin in minimal library ], ,
        	enable_dot_o_fibre=yes
)

AC_ARG_ENABLE(ext_1_fibre,
	      [  --disable-ext_1_fibre     disable ext_1_fibre plugin in minimal library ], ,
        	enable_ext_1_fibre=yes
)

AC_ARG_ENABLE(ext_3_fibre,
	      [  --disable-ext_3_fibre     disable ext_3_fibre plugin in minimal library ], ,
        	enable_ext_3_fibre=yes
)

AC_ARG_ENABLE(lexic_fibre,
	      [  --disable-lexic_fibre     disable lexic_fibre plugin in minimal library ], ,
        	enable_lexic_fibre=yes
)


# Checks for programs.
AC_PROG_CC
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_RANLIB
AC_PROG_AWK

MINIMAL_CFLAGS=""
GENERIC_CFLAGS=""

# make libc threadsafe (not required for us for awhile, but useful other users of
# libreiser4)
GENERIC_CFLAGS="$GENERIC_CFLAGS -D_REENTRANT"

AM_PROG_LIBTOOL

if test "$with_uuid" = yes; then
    	AC_CHECK_HEADERS(uuid/uuid.h, ,
		AC_MSG_WARN(The headers for libuuid could not be found which \
are required for the --with-uuid option.
		)
    	)
fi

if test "x$with_readline" = xyes; then
    	AC_CHECK_HEADERS(readline/readline.h readline/history.h, ,
		AC_MSG_WARN(The headers for GNU Readline could not be found which \
are required for the --with-readline option.
		)
    	)
fi

# Checks for header files.
AC_HEADER_DIRENT
AC_HEADER_STDC
AC_CHECK_HEADERS([printf.h errno.h fcntl.h mntent.h stdint.h stdlib.h \
string.h sys/ioctl.h sys/mount.h sys/vfs.h unistd.h])

# Checks for typedefs, structures and compiler characteristics.
AC_C_BIGENDIAN

# Checks for library functions.
if test "x$with_readline" = xyes; then
    	OLD_LIBS="$LIBS"
    	LIBS="$LIBS $PROGS_LIBS"
    	AC_CHECK_FUNCS(rl_completion_matches)
    	LIBS="$OLD_LIBS"
fi

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_C_INLINE
AC_TYPE_SIZE_T
AC_CHECK_MEMBERS([struct stat.st_rdev])

# Checks for library functions.
AC_PROG_GCC_TRADITIONAL
AC_FUNC_STAT
AC_CHECK_FUNCS([register_printf_function statfs getmntent hasmntopt memset strerror \
strtol time uname sysconf])

# The options -falign-* are supported by gcc 3.0 or later.
# Probably it is sufficient to only check for -falign-loops.
AC_CACHE_CHECK([whether -falign-loops works], [falign_loop_flag_cv_], [
  	saved_CPPFLAGS="$CPPFLAGS"
  	CPPFLAGS="-falign-loops=1"
  	AC_TRY_COMPILE(, , [falign_loop_flag_cv_=yes], [falign_loop_flag_cv_=no])
  	CPPFLAGS="$saved_CPPFLAGS"
])

# Checking for compiler warning options
AC_CACHE_CHECK([whether -Wuninitialized works], [uninitialized_cv_], [
  	saved_CPPFLAGS="$CPPFLAGS"
  	CPPFLAGS="-O1 -Wuninitialized"
  	AC_TRY_COMPILE(, , [uninitialized_cv_=yes], [uninitialized_cv_=no])
  	CPPFLAGS="$saved_CPPFLAGS"
])
 
AC_CACHE_CHECK([whether -Wno-unused-parameter works], [no_unused_parameter_cv_], [
  	saved_CPPFLAGS="$CPPFLAGS"
  	CPPFLAGS="-Wno-unused-parameter"
  	AC_TRY_COMPILE(, , [no_unused_parameter_cv_=yes], [no_unused_parameter_cv_=no])
  	CPPFLAGS="$saved_CPPFLAGS"
])
 
AC_CACHE_CHECK([whether -Wredundant-decls works], [redundant_decls_cv_], [
  	saved_CPPFLAGS="$CPPFLAGS"
  	CPPFLAGS="-Wredundant-decls"
  	AC_TRY_COMPILE(, , [redundant_decls_cv_=yes], [redundant_decls_cv_=no])
  	CPPFLAGS="$saved_CPPFLAGS"
])

if test "x$with_readline" = xyes && test "x$redundant_decls" == xyes; then
  	saved_CPPFLAGS="$CPPFLAGS"
  	CPPFLAGS="-Werror -Wredundant-decls"

 	AC_MSG_CHECKING(whether -Wredundant-decls works with readline.h)

  	AC_TRY_COMPILE([
#include <stdio.h> 
#include <readline/readline.h>
	], ,[
		redundant_decls=yes; 
		AC_MSG_RESULT(yes)
	], [
		redundant_decls=no; 
		AC_MSG_RESULT(no)
	])
  	CPPFLAGS="$saved_CPPFLAGS"
fi
 
# Force no alignment to save space.
if test "x$falign_loop_flag_cv_" = xyes; then
  	ALIGN_FLAGS="-falign-jumps=1 -falign-loops=1 -falign-functions=1 \
-falign-labels=1 -fno-inline -fstrength-reduce"
else
  	ALIGN_FLAGS="-malign-jumps=1 -malign-loops=1 -malign-functions=1"
fi

# Check for large file
AC_SYS_LARGEFILE

if test x${ac_cv_sys_file_offset_bits} = xno; then
	AC_MSG_WARN(Can't detect right _FILE_OFFSET_BITS. Will be forced to 64bit.)
	ac_cv_sys_file_offset_bits=64
fi

GENERIC_CFLAGS="$GENERIC_CFLAGS -D_FILE_OFFSET_BITS=${ac_cv_sys_file_offset_bits}"

AC_CHECK_SIZEOF(off_t, 64, [
	#include <stdio.h>
	#include <sys/types.h>
	#include <unistd.h>
])

OLD_LIBS="$LIBS"
AC_CHECK_LIBAAL(aal, 1.0.6, ,exit)
AAL_LIBS="$LIBS"
LIBS="$OLD_LIBS"

AC_SUBST(AAL_LIBS)

if test x$enable_libminimal = xyes; then
    	OLD_LIBS="$LIBS"
    	AC_CHECK_LIBAAL(aal-minimal, 1.0.6, ,exit)
    	AAL_MINIMAL_LIBS="$LIBS"
    	LIBS="$OLD_LIBS"

    	AC_SUBST(AAL_MINIMAL_LIBS)

    	if test x$enable_symlinks = xyes; then
		SYMLINKS_CFLAGS="-DENABLE_SYMLINKS"
    	fi

    	if test x$enable_special = xyes; then
		SPECIAL_CFLAGS="-DENABLE_SPECIAL"
    	fi

    	if test x$enable_r5_hash = xyes; then
		R5_HASH_CFLAGS="-DENABLE_R5_HASH"
    	fi

    	if test x$enable_fnv1_hash = xyes; then
		FNV1_HASH_CFLAGS="-DENABLE_FNV1_HASH"
    	fi

    	if test x$enable_rupasov_hash = xyes; then
		RUPASOV_HASH_CFLAGS="-DENABLE_RUPASOV_HASH"
    	fi

    	if test x$enable_tea_hash = xyes; then
		TEA_HASH_CFLAGS="-DENABLE_TEA_HASH"
    	fi

    	if test x$enable_deg_hash = xyes; then
		DEG_HASH_CFLAGS="-DENABLE_DEG_HASH"
    	fi

    	if test x$enable_short_keys = xyes; then
		SHORT_KEYS_CFLAGS="-DENABLE_SHORT_KEYS"
    	fi

    	if test x$enable_large_keys = xyes; then
		LARGE_KEYS_CFLAGS="-DENABLE_LARGE_KEYS"
   	fi

	if test x$enable_large_keys != xyes -a x$enable_short_keys != xyes; then
		echo
		echo Both LARGE and SHORT keys cannot be disabled at the same time.
		exit 1;
	fi
	
	if test x$enable_dot_o_fibre = xyes; then
		FIBRE_FLAGS="$FIBRE_FLAGS -DENABLE_DOT_O_FIBRE"
   	fi
	
	if test x$enable_ext_1_fibre = xyes; then
		FIBRE_FLAGS="$FIBRE_FLAGS -DENABLE_EXT_1_FIBRE"
   	fi
	
	if test x$enable_ext_3_fibre = xyes; then
		FIBRE_FLAGS="$FIBRE_FLAGS -DENABLE_EXT_3_FIBRE"
   	fi
	
	if test x$enable_lexic_fibre = xyes; then
		FIBRE_FLAGS="$FIBRE_FLAGS -DENABLE_LEXIC_FIBRE"
   	fi

#	if test x$enable_dot_o_fibre != xyes -a x$enable_ext_1_fibre != xyes -a \
#		x$enable_ext_3_fibre != xyes -a x$enable_lexic_fibre; then
#		echo
#		echo All fibre plugins cannot be disabled at the same time.
#		exit 1;
#	fi

    	MINIMAL_CFLAGS="$MINIMAL_CFLAGS -DENABLE_MINIMAL $SYMLINKS_CFLAGS $SPECIAL_CFLAGS \
$R5_HASH_CFLAGS $FNV1_HASH_CFLAGS $RUPASOV_HASH_CFLAGS $TEA_HASH_CFLAGS $DEG_HASH_CFLAGS \
$ALIGN_FLAGS $LARGE_KEYS_CFLAGS $SHORT_KEYS_CFLAGS $FIBRE_FLAGS"
fi

GENERIC_CFLAGS="$GENERIC_CFLAGS -DENABLE_SYMLINKS -DENABLE_SPECIAL -DENABLE_R5_HASH \
-DENABLE_FNV1_HASH -DENABLE_RUPASOV_HASH -DENABLE_TEA_HASH -DENABLE_DEG_HASH \
-DENABLE_LARGE_KEYS -DENABLE_SHORT_KEYS -DENABLE_DOT_O_FIBRE -DENABLE_EXT_1_FIBRE \
-DENABLE_EXT_3_FIBRE -DENABLE_LEXIC_FIBRE"

CFLAGS="$CFLAGS -W -Wall"

if test x$enable_debug = xyes; then
    	GENERIC_CFLAGS="$GENERIC_CFLAGS -O1 -g"
    	MINIMAL_CFLAGS="$MINIMAL_CFLAGS -O1 -g"
else
    	GENERIC_CFLAGS="$GENERIC_CFLAGS -O3"
    	MINIMAL_CFLAGS="$MINIMAL_CFLAGS -Os"

    	if test x$uninitialized = xyes; then
       		CFLAGS="$CFLAGS -Wuninitialized"
    	fi
fi

if test x$no_unused_parameter = xyes; then
    	CFLAGS="$CFLAGS -Wno-unused-parameter"
else
    	CFLAGS="$CFLAGS -Wno-unused"
fi

if test x$redundant_decls = xyes; then
    	CFLAGS="$CFLAGS -Wredundant-decls"
fi

if test x$enable_Werror = xyes; then
    	CFLAGS="$CFLAGS -Werror"
fi

AM_CONDITIONAL(ENABLE_MINIMAL, test x$enable_libminimal = xyes)

if test x$enable_debug = xyes; then
    	AC_DEFINE(ENABLE_DEBUG)
fi

AC_SUBST(PROGS_LIBS)
AC_SUBST(MINIMAL_CFLAGS)
AC_SUBST(GENERIC_CFLAGS)
AC_SUBST(PROGS_LDFLAGS)

AC_OUTPUT([
    	Makefile
    	include/Makefile
    	include/aux/Makefile
    	include/misc/Makefile
    	include/reiser4/Makefile
    	include/repair/Makefile
    	libmisc/Makefile
    	libaux/Makefile
    	libreiser4/Makefile
    	librepair/Makefile
    	plugin/Makefile
    	plugin/format/Makefile
    	plugin/format/format40/Makefile
    	plugin/alloc/Makefile
    	plugin/alloc/alloc40/Makefile
    	plugin/journal/Makefile
    	plugin/journal/journal40/Makefile
    	plugin/oid/Makefile
    	plugin/oid/oid40/Makefile
    	plugin/node/Makefile
    	plugin/node/node40/Makefile
	plugin/node/node41/Makefile
   	plugin/key/Makefile
    	plugin/key/key_common/Makefile
    	plugin/key/key_short/Makefile
    	plugin/key/key_large/Makefile
    	plugin/item/Makefile
    	plugin/item/body40/Makefile
    	plugin/item/nodeptr40/Makefile
    	plugin/item/stat40/Makefile
    	plugin/item/cde40/Makefile
    	plugin/item/tail40/Makefile
    	plugin/item/plain40/Makefile
    	plugin/item/ctail40/Makefile
    	plugin/item/extent40/Makefile
    	plugin/item/bbox40/Makefile
    	plugin/object/Makefile
    	plugin/object/obj40/Makefile
    	plugin/object/dir40/Makefile
    	plugin/object/reg40/Makefile
    	plugin/object/sym40/Makefile
    	plugin/object/spl40/Makefile
    	plugin/object/ccreg40/Makefile
    	plugin/policy/Makefile
    	plugin/policy/tails/Makefile
    	plugin/policy/extents/Makefile
    	plugin/policy/smart/Makefile
    	plugin/hash/Makefile
    	plugin/hash/r5_hash/Makefile
    	plugin/hash/tea_hash/Makefile
    	plugin/hash/deg_hash/Makefile
    	plugin/hash/rupasov_hash/Makefile
    	plugin/hash/fnv1_hash/Makefile
	plugin/fibre/Makefile
	plugin/fibre/lexic_fibre/Makefile
	plugin/fibre/dot_o_fibre/Makefile
	plugin/fibre/ext_1_fibre/Makefile
	plugin/fibre/ext_3_fibre/Makefile
    	plugin/sdext/Makefile
    	plugin/sdext/sdext_unix/Makefile
    	plugin/sdext/sdext_lw/Makefile
    	plugin/sdext/sdext_lt/Makefile
    	plugin/sdext/sdext_symlink/Makefile
    	plugin/sdext/sdext_flags/Makefile
	plugin/sdext/sdext_plug/Makefile
	plugin/sdext/sdext_crypto/Makefile
	plugin/compress/Makefile
    	progs/Makefile
    	progs/mkfs/Makefile
    	progs/fsck/Makefile
    	progs/debugfs/Makefile
    	progs/measurefs/Makefile
    	demos/Makefile
    	doc/Makefile
    	reiser4progs.spec
])

echo
echo Type \'make\' to compile reiser4progs and \'make install\' to install it.
