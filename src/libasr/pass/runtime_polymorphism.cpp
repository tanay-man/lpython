#include <libasr/asr.h>
#include <libasr/containers.h>
#include <libasr/exception.h>
#include <libasr/asr_utils.h>
#include <libasr/asr_verify.h>
#include <libasr/pass/visit_runtime_polymorphism.h>
#include <libasr/pass/pass_utils.h>

#include <vector>
#include <utility>

namespace LCompilers {

class AddVtable : public ASR::ASRPassBaseWalkVisitor<AddVtable>
{
    private:
        Allocator& al;
    public:
    AddVtable(Allocator& al_) :
        al(al_) { }
    
    void visit_Struct(const ASR::Struct_t & x ) {
        size_t fn_num = x.n_member_functions;
    }

};

void pass_add_vtable(Allocator &al,
    ASR::TranslationUnit_t &unit,
    const LCompilers::PassOptions& /*pass_options*/) {
    AddVtable v(al);
    v.visit_TranslationUnit(unit);
    PassUtils::UpdateDependenciesVisitor w(al);
    w.visit_TranslationUnit(unit);
}


} // namespace LCompilers
