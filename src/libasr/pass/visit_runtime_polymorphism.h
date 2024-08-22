#ifndef LIBASR_PASS_ADD_VTABLE_H
#define LIBASR_PASS_ADD_VTABLE_H

#include <libasr/asr.h>
#include <libasr/utils.h>

namespace LCompilers {

    void pass_add_vtable(Allocator &al, ASR::TranslationUnit_t &unit,
                                const PassOptions &pass_options);

} // namespace LCompilers

#endif // LIBASR_PASS_ADD_VTABLE_H
