# Autogenerated on: 10/11/19 09:11:11

import ida_bytes
import ida_fixup
import ida_ida
import ida_idaapi
import ida_idp
import ida_kernwin
import ida_nalt
import ida_name
import ida_segment
import ida_ua
from idc import *

def Compile(file): return CompileEx(file, 1)
def OpOffset(ea, base): return op_plain_offset(ea, -1, base)
def OpNum(ea): return op_num(ea, -1)
def OpChar(ea): return op_chr(ea, -1)
def OpSegment(ea): return op_seg(ea, -1)
def OpDec(ea): return op_dec(ea, -1)
def OpAlt1(ea, str): return op_man(ea, 0, str)
def OpAlt2(ea, str): return op_man(ea, 1, str)
def StringStp(x): return set_inf_attr(INF_STRLIT_BREAK, x)
def LowVoids(x): return set_inf_attr(INF_LOW_OFF, x)
def HighVoids(x): return set_inf_attr(INF_HIGH_OFF, x)
def TailDepth(x): return set_inf_attr(INF_MAXREF, x)
def Analysis(x): return set_flag(INF_GENFLAGS, INFFL_AUTO, x)
def Comments(x): return set_flag(INF_CMTFLAG, SW_ALLCMT, x)
def Voids(x): return set_flag(INF_OUTFLAGS, OFLG_SHOW_VOID, x)
def XrefShow(x): return set_inf_attr(INF_XREFNUM, x)
def Indent(x): return set_inf_attr(INF_INDENT, x)
def CmtIndent(x): return set_inf_attr(INF_COMMENT, x)
def AutoShow(x): return set_flag(INF_OUTFLAGS, OFLG_SHOW_AUTO, x)
def MinEA(): return get_inf_attr(INF_MIN_EA)
def MaxEA(): return get_inf_attr(INF_MAX_EA)
def StartEA(): return get_inf_attr(INF_START_EA)
def set_start_cs(x): return set_inf_attr(INF_START_CS, x)
def set_start_ip(x): return set_inf_attr(INF_START_IP, x)
def auto_make_code(x): return auto_mark_range(x, (x)+1, AU_CODE);
def AddConst(enum_id, name, value): return add_enum_member(enum_id, name, value, -1)
def AddStruc(index, name): return add_struc(index, name, 0)
def AddUnion(index, name): return add_struc(index, name, 1)
def OpStroff(ea, n, strid): return op_stroff(ea, n, strid, 0)
def OpEnum(ea, n, enumid): return op_enum(ea, n, enumid, 0)
def DelConst(id, v, mask): return del_enum_member(id, v, 0, mask)
def GetConst(id, v, mask): return get_enum_member(id, v, 0, mask)
def AnalyseRange(sEA, eEA): return plan_and_wait(sEA, eEA)
def AnalyseArea(sEA, eEA): return plan_and_wait(sEA, eEA)
def AnalyzeArea(sEA, eEA): return plan_and_wait(sEA, eEA)
def MakeStruct(ea, name): return create_struct(ea, -1, name)
def Name(ea): return get_name(ea, ida_name.GN_VISIBLE)
def GetTrueName(ea): return get_name(ea)
def MakeName(ea, name): return set_name(ea, name, SN_CHECK)
def GetFrame(ea): return get_func_attr(ea, FUNCATTR_FRAME)
def GetFrameLvarSize(ea): return get_func_attr(ea, FUNCATTR_FRSIZE)
def GetFrameRegsSize(ea): return get_func_attr(ea, FUNCATTR_FRREGS)
def GetFrameArgsSize(ea): return get_func_attr(ea, FUNCATTR_ARGSIZE)
def GetFunctionFlags(ea): return get_func_attr(ea, FUNCATTR_FLAGS)
def SetFunctionFlags(ea, flags): return set_func_attr(ea, FUNCATTR_FLAGS, flags)
def SegCreate(a1, a2, base, use32, align, comb): return AddSeg(a1, a2, base, use32, align, comb)
def SegDelete(ea, flags): return del_segm(ea, flags)
def SegBounds(ea, startea, endea, flags): return set_segment_bounds(ea, startea, endea, flags)
def SegRename(ea, name): return set_segm_name(ea, name)
def SegClass(ea, klass): return set_segm_class(ea, klass)
def SegAddrng(ea, bitness): return set_segm_addressing(ea, bitness)
def SegDefReg(ea, reg, value): return set_default_sreg_value(ea, reg, value)
def Comment(ea): return get_cmt(ea, 0)
def RptCmt(ea): return get_cmt(ea, 1)
def MakeByte(ea): return create_data(ea, FF_BYTE, 1, ida_idaapi.BADADDR)
def MakeWord(ea): return create_data(ea, FF_WORD, 2, ida_idaapi.BADADDR)
def MakeDword(ea): return create_data(ea, FF_DWORD, 4, ida_idaapi.BADADDR)
def MakeQword(ea): return create_data(ea, FF_QWORD, 8, ida_idaapi.BADADDR)
def MakeOword(ea): return create_data(ea, FF_OWORD, 16, ida_idaapi.BADADDR)
def MakeYword(ea): return create_data(ea, FF_YWORD, 32, ida_idaapi.BADADDR)
def MakeFloat(ea): return create_data(ea, FF_FLOAT, 4, ida_idaapi.BADADDR)
def MakeDouble(ea): return create_data(ea, FF_DOUBLE, 8, ida_idaapi.BADADDR)
def MakePackReal(ea): return create_data(ea, FF_PACKREAL, 10, ida_idaapi.BADADDR)
def MakeTbyte(ea): return create_data(ea, FF_TBYTE, 10, ida_idaapi.BADADDR)
def MakeCustomData(ea, size, dtid, fid): return create_data(ea, FF_CUSTOM, size, dtid|((fid)<<16))
def SetReg(ea, reg, value): return split_sreg_range(ea, reg, value, SR_user)
def SegByName(segname): return selector_by_name(segname)
def MK_FP(seg, off): return to_ea(seg, off)
def toEA(seg, off): return to_ea(seg, off)
def MakeCode(ea): return create_insn(ea)
def MakeNameEx(ea, name, flags): return set_name(ea, name, flags)
def MakeArray(ea, nitems): return make_array(ea, nitems)
def MakeData(ea, flags, size, tid): return create_data(ea, flags, size, tid)
def GetRegValue(name): return get_reg_value(name)
def SetRegValue(value, name): return set_reg_value(value, name)
def Byte(ea): return get_wide_byte(ea)
def Word(ea): return get_wide_word(ea)
def Dword(ea): return get_wide_dword(ea)
def Qword(ea): return get_qword(ea)
def LocByName(name): return get_name_ea_simple(name)
def ScreenEA(): return get_screen_ea()
def GetTinfo(ea): return get_tinfo(ea)
def OpChr(ea, n): return op_chr(ea, n)
def OpSeg(ea, n): return op_seg(ea, n)
def OpNumber(ea, n): return op_num(ea, n)
def OpDecimal(ea, n): return op_dec(ea, n)
def OpOctal(ea, n): return op_oct(ea, n)
def OpBinary(ea, n): return op_bin(ea, n)
def OpHex(ea, n): return op_hex(ea, n)
def OpAlt(ea, n, str): return op_man(ea, n, str)
def OpSign(ea, n): return toggle_sign(ea, n)
def OpNot(ea, n): return toggle_bnot(ea, n)
def OpEnumEx(ea, n, enumid, serial): return op_enum(ea, n, enumid, serial)
def OpStroffEx(ea, n, strid, delta): return op_stroff(ea, n, strid, delta)
def OpStkvar(ea, n): return op_stkvar(ea, n)
def OpFloat(ea, n): return op_flt(ea, n)
def OpOffEx(ea, n, reftype, target, base, tdelta): return op_offset(ea, n, reftype, target, base, tdelta)
def OpOff(ea, n, base): return op_plain_offset(ea, n, base)
def MakeStructEx(ea, size, strname): return create_struct(ea, size, strname)
def Jump(ea): return jumpto(ea)
def GenerateFile(type, file_handle, ea1, ea2, flags): return gen_file(type, file_handle, ea1, ea2, flags)
def GenFuncGdl(outfile, title, ea1, ea2, flags): return gen_flow_graph(outfile, title, ea1, ea2, flags)
def GenCallGdl(outfile, title, flags): return gen_simple_call_chart(outfile, title, flags)
def IdbByte(ea): return get_db_byte(ea)
def DbgByte(ea): return read_dbg_byte(ea)
def DbgWord(ea): return read_dbg_word(ea)
def DbgDword(ea): return read_dbg_dword(ea)
def DbgQword(ea): return read_dbg_qword(ea)
def DbgRead(ea, size): return read_dbg_memory(ea, size)
def DbgWrite(ea, data): return write_dbg_memory(ea, data)
def PatchDbgByte(ea, value): return patch_dbg_byte(ea, value)
def PatchByte(ea, value): return patch_byte(ea, value)
def PatchWord(ea, value): return patch_word(ea, value)
def PatchDword(ea, value): return patch_dword(ea, value)
def PatchQword(ea, value): return patch_qword(ea, value)
def SetProcessorType(processor, level): return set_processor_type(processor, level)
def SetTargetAssembler(asmidx): return set_target_assembler(asmidx)
def Batch(mode): return batch(mode)
def SetSegDefReg(ea, reg, value): return set_default_sreg_value(ea, reg, value)
def GetReg(ea, reg): return get_sreg(ea, reg)
def SetRegEx(ea, reg, value, tag): return split_sreg_range(ea, reg, value, tag)
def AskStr(defval, prompt): return ida_kernwin.ask_str(defval, 0, prompt)
def AskFile(for_saving, mask, prompt): return ida_kernwin.ask_file(for_saving, mask, prompt)
def AskAddr(defval, prompt): return ida_kernwin.ask_addr(defval, prompt)
def AskLong(defval, prompt): return ida_kernwin.ask_long(defval, prompt)
def AskSeg(defval, prompt): return ask_seg(defval, prompt)
def AskIdent(defval, prompt): return ida_kernwin.ask_str(defval, ida_kernwin.HIST_IDENT, prompt)
def AskYN(defval, prompt): return ask_yn(defval, prompt)
Warning=ida_kernwin.warning
Fatal=ida_kernwin.error
def DeleteAll(): return delete_all_segments()
def AddSegEx(startea, endea, sel, use32, align, comb, flags): return add_segm_ex(startea, endea, sel, use32, align, comb, flags)
def SetSegBounds(ea, startea, endea, flags): return set_segment_bounds(ea, startea, endea, flags)
def RenameSeg(ea, name): return set_segm_name(ea, name)
def SetSegClass(ea, klass): return set_segm_class(ea, klass)
def SetSegAddressing(ea, bitness): return set_segm_addressing(ea, bitness)
def SetSegmentAttr(segea, attr, value): return set_segm_attr(segea, attr, value)
def GetSegmentAttr(segea, attr): return get_segm_attr(segea, attr)
def SetStorageType(startEA, endEA, stt): return set_storage_type(startEA, endEA, stt)
def MoveSegm(ea, to, flags): return move_segm(ea, to, flags)
def RebaseProgram(delta, flags): return rebase_program(delta, flags)
def GetNsecStamp(): return get_nsec_stamp()
def LocByNameEx(From, name): return get_name_ea(From, name)
def SegByBase(base): return get_segm_by_sel(base)
def GetCurrentLine(): return get_curline()
def SelStart(): return read_selection_start()
def SelEnd(): return read_selection_end()
def FirstSeg(): return get_first_seg()
def NextSeg(ea): return get_next_seg(ea)
def SegName(ea): return get_segm_name(ea)
def CommentEx(ea, repeatable): return get_cmt(ea, repeatable)
def AltOp(ea, n): return get_forced_operand(ea, n)
def GetDisasmEx(ea, flags): return generate_disasm_line(ea, flags)
def GetMnem(ea): return print_insn_mnem(ea)
def GetOpType(ea, n): return get_operand_type(ea, n)
def GetOperandValue(ea, n): return get_operand_value(ea, n)
def DecodeInstruction(ea): return ida_ua.decode_insn(ea)
def NextAddr(ea): return next_addr(ea)
def PrevAddr(ea): return prev_addr(ea)
def NextNotTail(ea): return next_not_tail(ea)
def PrevNotTail(ea): return prev_not_tail(ea)
def ItemHead(ea): return get_item_head(ea)
def ItemEnd(ea): return get_item_end(ea)
def ItemSize(ea): return get_item_size(ea)
def AnalyzeRange(sEA, eEA): return plan_and_wait(sEA, eEA)
def ExecIDC(input): return exec_idc(input)
def Eval(expr): return eval(expr)
def Exit(code): return qexit(code)
def Checkpoint(num): return test_checkpoint(num)
def GetTestId(): return get_test_id()
def FindVoid(ea, flag): return find_suspop(ea, flag)
def FindCode(ea, flag): return find_code(ea, flag)
def FindData(ea, flag): return find_data(ea, flag)
def FindUnexplored(ea, flag): return find_unknown(ea, flag)
def FindExplored(ea, flag): return find_defined(ea, flag)
def FindImmediate(ea, flag, value): return find_imm(ea, flag, value)
def AddCodeXref(From, To, flowtype): return add_cref(From, To, flowtype)
def DelCodeXref(From, To, undef): return del_cref(From, To, undef)
def Rfirst(From): return get_first_cref_from(From)
def RfirstB(To): return get_first_cref_to(To)
def Rnext(From, current): return get_next_cref_from(From, current)
def RnextB(To, current): return get_next_cref_to(To, current)
def Rfirst0(From): return get_first_fcref_from(From)
def RfirstB0(To): return get_first_fcref_to(To)
def Rnext0(From, current): return get_next_fcref_from(From, current)
def RnextB0(To, current): return get_next_fcref_to(To, current)
def Dfirst(From): return get_first_dref_from(From)
def Dnext(From, current): return get_next_dref_from(From, current)
def DfirstB(To): return get_first_dref_to(To)
def DnextB(To, current): return get_next_dref_to(To, current)
def XrefType(): return get_xref_type()
def AutoUnmark(start, end, queuetype): return auto_unmark(start, end, queuetype)
def AutoMark2(start, end, queuetype): return auto_mark_range(start, end, queuetype)
def SetSelector(sel, value): return set_selector(sel, value)
def AskSelector(sel): return sel2para(sel)
def ask_selector(sel): return sel2para(sel)
def FindSelector(val): return find_selector(val)
def DelSelector(sel): return del_selector(sel)
def MakeFunction(start, end): return add_func(start, end)
def DelFunction(ea): return del_func(ea)
def SetFunctionEnd(ea, end): return set_func_end(ea, end)
def NextFunction(ea): return get_next_func(ea)
def PrevFunction(ea): return get_prev_func(ea)
def GetFunctionAttr(ea, attr): return get_func_attr(ea, attr)
def SetFunctionAttr(ea, attr, value): return set_func_attr(ea, attr, value)
def GetFunctionName(ea): return get_func_name(ea)
def GetFunctionCmt(ea, repeatable): return get_func_cmt(ea, repeatable)
def SetFunctionCmt(ea, cmt, repeatable): return set_func_cmt(ea, cmt, repeatable)
def ChooseFunction(title): return choose_func(title)
def GetFuncOffset(ea): return get_func_off_str(ea)
def MakeLocal(start, end, location, name): return define_local_var(start, end, location, name)
def FindFuncEnd(ea): return find_func_end(ea)
def GetFrameSize(ea): return get_frame_size(ea)
def MakeFrame(ea, lvsize, frregs, argsize): return set_frame_size(ea, lvsize, frregs, argsize)
def GetSpd(ea): return get_spd(ea)
def GetSpDiff(ea): return get_sp_delta(ea)
def DelStkPnt(func_ea, ea): return del_stkpnt(func_ea, ea)
def AddAutoStkPnt2(func_ea, ea, delta): return add_auto_stkpnt(func_ea, ea, delta)
def RecalcSpd(cur_ea): return recalc_spd(cur_ea)
def GetMinSpd(func_ea): return get_min_spd_ea(func_ea)
def GetFchunkAttr(ea, attr): return get_fchunk_attr(ea, attr)
def SetFchunkAttr(ea, attr, value): return set_fchunk_attr(ea, attr, value)
def GetFchunkReferer(ea, idx): return get_fchunk_referer(ea, idx)
def NextFchunk(ea): return get_next_fchunk(ea)
def PrevFchunk(ea): return get_prev_fchunk(ea)
def AppendFchunk(funcea, ea1, ea2): return append_func_tail(funcea, ea1, ea2)
def RemoveFchunk(funcea, tailea): return remove_fchunk(funcea, tailea)
def SetFchunkOwner(tailea, funcea): return set_tail_owner(tailea, funcea)
def FirstFuncFchunk(funcea): return first_func_chunk(funcea)
def NextFuncFchunk(funcea, tailea): return next_func_chunk(funcea, tailea)
def GetEntryPointQty(): return get_entry_qty()
def AddEntryPoint(ordinal, ea, name, makecode): return add_entry(ordinal, ea, name, makecode)
def GetEntryName(ordinal): return get_entry_name(ordinal)
def GetEntryOrdinal(index): return get_entry_ordinal(index)
def GetEntryPoint(ordinal): return get_entry(ordinal)
def RenameEntryPoint(ordinal, name): return rename_entry(ordinal, name)
def GetNextFixupEA(ea): return get_next_fixup_ea(ea)
def GetPrevFixupEA(ea): return get_prev_fixup_ea(ea)
def GetFixupTgtType(ea): return get_fixup_target_type(ea)
def GetFixupTgtFlags(ea): return get_fixup_target_flags(ea)
def GetFixupTgtSel(ea): return get_fixup_target_sel(ea)
def GetFixupTgtOff(ea): return get_fixup_target_off(ea)
def GetFixupTgtDispl(ea): return get_fixup_target_dis(ea)
def SetFixup(ea, type, targetsel, targetoff, displ): return set_fixup(ea, type, targetsel, targetoff, displ)
def DelFixup(ea): return del_fixup(ea)
def MarkPosition(ea, lnnum, x, y, slot, comment): return put_bookmark(ea, lnnum, x, y, slot, comment)
def GetMarkedPos(slot): return get_bookmark(slot)
def GetMarkComment(slot): return get_bookmark_desc(slot)
def GetStrucQty(): return get_struc_qty()
def GetFirstStrucIdx(): return get_first_struc_idx()
def GetLastStrucIdx(): return get_last_struc_idx()
def GetNextStrucIdx(index): return get_next_struc_idx(index)
def GetPrevStrucIdx(index): return get_prev_struc_idx(index)
def GetStrucIdx(id): return get_struc_idx(id)
def GetStrucId(index): return get_struc_by_idx(index)
def GetStrucIdByName(name): return get_struc_id(name)
def GetStrucName(id): return get_struc_name(id)
def GetStrucComment(id, repeatable): return get_struc_cmt(id, repeatable)
def GetStrucSize(id): return get_struc_size(id)
def GetMemberQty(id): return get_member_qty(id)
def GetStrucPrevOff(id, offset): return get_prev_offset(id, offset)
def GetStrucNextOff(id, offset): return get_next_offset(id, offset)
def GetFirstMember(id): return get_first_member(id)
def GetLastMember(id): return get_last_member(id)
def GetMemberOffset(id, member_name): return get_member_offset(id, member_name)
def GetMemberName(id, member_offset): return get_member_name(id, member_offset)
def GetMemberComment(id, member_offset, repeatable): return get_member_cmt(id, member_offset, repeatable)
def GetMemberSize(id, member_offset): return get_member_size(id, member_offset)
def GetMemberFlag(id, member_offset): return get_member_flag(id, member_offset)
def GetMemberStrId(id, member_offset): return get_member_strid(id, member_offset)
def GetMemberId(id, member_offset): return get_member_id(id, member_offset)
def AddStrucEx(index, name, is_union): return add_struc(index, name, is_union)
def IsUnion(id): return is_union(id)
def DelStruc(id): return del_struc(id)
def SetStrucIdx(id, index): return set_struc_idx(id, index)
def SetStrucName(id, name): return set_struc_name(id, name)
def SetStrucComment(id, comment, repeatable): return set_struc_cmt(id, comment, repeatable)
def SetStrucAlign(sid, shift): return set_struc_align(sid, shift)
AddStrucMember=add_struc_member
def DelStrucMember(id, member_offset): return del_struc_member(id, member_offset)
def SetMemberName(id, member_offset, name): return set_member_name(id, member_offset, name)
SetMemberType=set_member_type
def SetMemberComment(id, member_offset, comment, repeatable): return set_member_cmt(id, member_offset, comment, repeatable)
def ExpandStruc(id, offset, delta, recalc): return expand_struc(id, offset, delta, recalc)
def GetVxdFuncName(vxdnum, fnnum): return get_vxd_func_name(vxdnum, fnnum)
def SetLineNumber(ea, lnnum): return set_source_linnum(ea, lnnum)
def GetLineNumber(ea): return get_source_linnum(ea)
def DelLineNumber(ea): return del_source_linnum(ea)
def AddSourceFile(ea1, uea2, filename): return add_sourcefile(ea1, uea2, filename)
def GetSourceFile(ea): return get_sourcefile(ea)
def DelSourceFile(ea): return del_sourcefile(ea)
def CreateArray(name): return create_array(name)
def GetArrayId(name): return get_array_id(name)
def RenameArray(id, newname): return rename_array(id, newname)
def DeleteArray(id): return delete_array(id)
def SetArrayLong(id, idx, value): return set_array_long(id, idx, value)
def SetArrayString(id, idx, str): return set_array_string(id, idx, str)
def GetArrayElement(tag, id, idx): return get_array_element(tag, id, idx)
def DelArrayElement(tag, id, idx): return del_array_element(tag, id, idx)
def GetFirstIndex(tag, id): return get_first_index(tag, id)
def GetNextIndex(tag, id, idx): return get_next_index(tag, id, idx)
def GetLastIndex(tag, id): return get_last_index(tag, id)
def GetPrevIndex(tag, id, idx): return get_prev_index(tag, id, idx)
def SetHashLong(id, idx, value): return set_hash_long(id, idx, value)
def SetHashString(id, idx, value): return set_hash_string(id, idx, value)
def GetHashLong(id, idx): return get_hash_long(id, idx)
def GetHashString(id, idx): return get_hash_string(id, idx)
def DelHashElement(id, idx): return del_hash_string(id, idx)
def GetFirstHashKey(id): return get_first_hash_key(id)
def GetNextHashKey(id, idx): return get_next_hash_key(id, idx)
def GetLastHashKey(id): return get_last_hash_key(id)
def GetPrevHashKey(id, idx): return get_prev_hash_key(id, idx)
def GetEnumQty(): return get_enum_qty()
def GetnEnum(idx): return getn_enum(idx)
def GetEnumIdx(enum_id): return get_enum_idx(enum_id)
def GetEnum(name): return get_enum(name)
def GetEnumName(enum_id): return get_enum_name(enum_id)
def GetEnumCmt(enum_id, repeatable): return get_enum_cmt(enum_id, repeatable)
def GetEnumSize(enum_id): return get_enum_size(enum_id)
def GetEnumWidth(enum_id): return get_enum_width(enum_id)
def GetEnumFlag(enum_id): return get_enum_flag(enum_id)
def GetConstByName(name): return get_enum_member_by_name(name)
def GetConstValue(const_id): return get_enum_member_value(const_id)
def GetConstBmask(const_id): return get_enum_member_bmask(const_id)
def GetConstEnum(const_id): return get_enum_member_enum(const_id)
def GetConstEx(enum_id, value, serial, bmask): return get_enum_member(enum_id, value, serial, bmask)
def GetFirstBmask(enum_id): return get_first_bmask(enum_id)
def GetLastBmask(enum_id): return get_last_bmask(enum_id)
def GetNextBmask(enum_id, value): return get_next_bmask(enum_id, value)
def GetPrevBmask(enum_id, value): return get_prev_bmask(enum_id, value)
def GetFirstConst(enum_id, bmask): return get_first_enum_member(enum_id, bmask)
def GetLastConst(enum_id, bmask): return get_last_enum_member(enum_id, bmask)
def GetNextConst(enum_id, value, bmask): return get_next_enum_member(enum_id, value, bmask)
def GetPrevConst(enum_id, value, bmask): return get_prev_enum_member(enum_id, value, bmask)
def GetConstName(const_id): return get_enum_member_name(const_id)
def GetConstCmt(const_id, repeatable): return get_enum_member_cmt(const_id, repeatable)
def AddEnum(idx, name, flag): return add_enum(idx, name, flag)
def DelEnum(enum_id): return del_enum(enum_id)
def SetEnumIdx(enum_id, idx): return set_enum_idx(enum_id, idx)
def SetEnumName(enum_id, name): return set_enum_name(enum_id, name)
def SetEnumCmt(enum_id, cmt, repeatable): return set_enum_cmt(enum_id, cmt, repeatable)
def SetEnumFlag(enum_id, flag): return set_enum_flag(enum_id, flag)
def SetEnumWidth(enum_id, width): return set_enum_width(enum_id, width)
def SetEnumBf(enum_id, flag): return set_enum_bf(enum_id, flag)
def AddConstEx(enum_id, name, value, bmask): return add_enum_member(enum_id, name, value, bmask)
def DelConstEx(enum_id, value, serial, bmask): return del_enum_member(enum_id, value, serial, bmask)
def SetConstName(const_id, name): return set_enum_member_name(const_id, name)
def SetConstCmt(const_id, cmt, repeatable): return set_enum_member_cmt(const_id, cmt, repeatable)
def IsBitfield(enum_id): return is_bf(enum_id)
def SetBmaskName(enum_id, bmask, name): return set_bmask_name(enum_id, bmask, name)
def GetBmaskName(enum_id, bmask): return get_bmask_name(enum_id, bmask)
def SetBmaskCmt(enum_id, bmask, cmt, repeatable): return set_bmask_cmt(enum_id, bmask, cmt, repeatable)
def GetBmaskCmt(enum_id, bmask, repeatable): return get_bmask_cmt(enum_id, bmask, repeatable)
def GetLongPrm(offset): return get_inf_attr(offset)
def GetShortPrm(offset): return get_inf_attr(offset)
def GetCharPrm(offset): return get_inf_attr(offset)
def SetLongPrm(offset, value): return set_inf_attr(offset, value)
def SetShortPrm(offset, value): return set_inf_attr(offset, value)
def SetCharPrm(offset, value): return set_inf_attr(offset, value)
def ChangeConfig(directive): return process_config_line(directive)
def AddHotkey(hotkey, idcfunc): return add_idc_hotkey(hotkey, idcfunc)
def DelHotkey(hotkey): return del_idc_hotkey(hotkey)
def GetInputFile(): return get_root_filename()
def GetInputFilePath(): return get_input_file_path()
def SetInputFilePath(path): return set_root_filename(path)
def GetInputFileSize(): return retrieve_input_file_size()
def Exec(command): return call_system(command)
def Sleep(milliseconds): return qsleep(milliseconds)
def GetIdaDirectory(): return idadir()
def GetIdbPath(): return get_idb_path()
def GetInputMD5(): return retrieve_input_file_md5()
def GetInputSHA256(): return retrieve_input_file_sha256()
def OpHigh(ea, n, target): return op_offset_high16(ea, n, target)
def MakeAlign(ea, count, align): return create_align(ea, count, align)
def Demangle(name, disable_mask): return demangle_name(name, disable_mask)
def SetManualInsn(ea, insn): return set_manual_insn(ea, insn)
def GetManualInsn(ea): return get_manual_insn(ea)
def SetArrayFormat(ea, flags, litems, align): return set_array_params(ea, flags, litems, align)
def LoadTil(name): return add_default_til(name)
def Til2Idb(idx, type_name): return import_type(idx, type_name)
def GetMaxLocalType(): return get_ordinal_qty()
def SetLocalType(ordinal, input, flags): return set_local_type(ordinal, input, flags)
def GetLocalTinfo(ordinal): return get_local_tinfo(ordinal)
def GetLocalTypeName(ordinal): return get_numbered_type_name(ordinal)
def PrintLocalTypes(ordinals, flags): return print_decls(ordinals, flags)
def SetStatus(status): return set_ida_state(status)
def Refresh(): return refresh_idaview_anyway()
def RefreshLists(): return refresh_choosers()
def RunPlugin(name, arg): return load_and_run_plugin(name, arg)
def ApplySig(name): return plan_to_apply_idasgn(name)
def GetStringType(ea): return get_str_type(ea)
def GetOriginalByte(ea): return get_original_byte(ea)
def GetFpNum(ea, n): return get_fpnum(ea, n)
def HideRange(start, end, description, header, footer, color): return add_hidden_range(start, end, description, header, footer, color)
def SetHiddenRange(ea, visible): return update_hidden_range(ea, visible)
def DelHiddenRange(ea): return del_hidden_range(ea)
def GetType(ea): return get_type(ea)
def GuessType(ea): return guess_type(ea)
def ParseType(input, flags): return parse_decl(input, flags)
def GetColor(ea, what): return get_color(ea, what)
def SetColor(ea, what, color): return set_color(ea, what, color)
def GetBptQty(): return get_bpt_qty()
def GetBptEA(n): return get_bpt_ea(n)
def GetBptAttr(ea, bptattr): return get_bpt_attr(ea, bptattr)
def SetBptAttr(ea, bptattr, value): return set_bpt_attr(ea, bptattr, value)
def SetBptCndEx(ea, cnd, is_lowcnd): return set_bpt_cond(ea, cnd, is_lowcnd)
def SetBptCnd(ea, cnd): return set_bpt_cond(ea, cnd)
def AddBptEx(ea, size, bpttype): return add_bpt(ea, size, bpttype)
def AddBpt(ea): return add_bpt(ea)
def DelBpt(ea): return del_bpt(ea)
def EnableBpt(ea, enable): return enable_bpt(ea, enable)
def CheckBpt(ea): return check_bpt(ea)
def LoadDebugger(dbgname, use_remote): return load_debugger(dbgname, use_remote)
def StartDebugger(path, args, sdir): return start_process(path, args, sdir)
def StopDebugger(): return exit_process()
def PauseProcess(): return suspend_process()
def GetProcessQty(): return get_processes().size
def GetProcessPid(idx): return get_processes()[idx].pid
def GetProcessName(idx): return get_processes()[idx].name
def AttachProcess(pid, event_id): return attach_process(pid, event_id)
def DetachProcess(): return detach_process()
def GetThreadQty(): return get_thread_qty()
def GetThreadId(idx): return getn_thread(idx)
def GetCurrentThreadId(): return get_current_thread()
def SelectThread(tid): return select_thread(tid)
def SuspendThread(tid): return suspend_thread(tid)
def ResumeThread(tid): return resume_thread(tid)
def GetFirstModule(): return get_first_module()
def GetNextModule(base): return get_next_module(base)
def GetModuleName(base): return get_module_name(base)
def GetModuleSize(base): return get_module_size(base)
def StepInto(): return step_into()
def StepOver(): return step_over()
def RunTo(ea): return run_to(ea)
def StepUntilRet(): return step_until_ret()
def GetDebuggerEvent(wfne, timeout): return wait_for_next_event(wfne, timeout)
def GetProcessState(): return get_process_state()
def SetDebuggerOptions(opt): return set_debugger_options(opt)
def SetRemoteDebugger(hostname, password, portnum): return set_remote_debugger(hostname, password, portnum)
def GetDebuggerEventCondition(): return get_debugger_event_cond()
def SetDebuggerEventCondition(condition): return set_debugger_event_cond(condition)
def GetEventId(): return get_event_id()
def GetEventPid(): return get_event_pid()
def GetEventTid(): return get_event_tid()
def GetEventEa(): return get_event_ea()
def IsEventHandled(): return is_event_handled()
def GetEventModuleName(): return get_event_module_name()
def GetEventModuleBase(): return get_event_module_base()
def GetEventModuleSize(): return get_event_module_size()
def GetEventExitCode(): return get_event_exit_code()
def GetEventInfo(): return get_event_info()
def GetEventBptHardwareEa(): return get_event_bpt_hea()
def GetEventExceptionCode(): return get_event_exc_code()
def GetEventExceptionEa(): return get_event_exc_ea()
def GetEventExceptionInfo(): return get_event_exc_info()
def CanExceptionContinue(): return can_exc_continue()
def RefreshDebuggerMemory(): return refresh_debugger_memory()
def TakeMemorySnapshot(only_loader_segs): return take_memory_snapshot(only_loader_segs)
def EnableTracing(trace_level, enable): return enable_tracing(trace_level, enable)
def GetStepTraceOptions(): return get_step_trace_options()
def SetStepTraceOptions(options): return set_step_trace_options(options)
def GetExceptionQty(): return get_exception_qty()
def GetExceptionCode(idx): return get_exception_code(idx)
def GetExceptionName(code): return get_exception_name(code)
def GetExceptionFlags(code): return get_exception_flags(code)
def DefineException(code, name, desc, flags): return define_exception(code, name, desc, flags)
def SetExceptionFlags(code, flags): return set_exception_flags(code, flags)
def ForgetException(code): return forget_exception(code)
def IsString(var): return value_is_string(var)
def IsLong(var): return value_is_long(var)
def IsFloat(var): return value_is_float(var)
def IsObject(var): return value_is_object(var)
def IsFunc(var): return value_is_func(var)
def IsPvoid(var): return value_is_pvoid(var)
def IsInt64(var): return value_is_int64(var)
def GetCustomDataType(name): return find_custom_data_type(name)
def GetCustomDataFormat(name): return find_custom_data_format(name)
def BeginTypeUpdating(utp): return begin_type_updating(utp)
def EndTypeUpdating(utp): return end_type_updating(utp)
def FormatCData(outvec, value, type, options, info): return format_cdata(outvec, value, type, options, info)
def ValidateNames(): return validate_idb_names()
def SegAlign(ea, alignment): return set_segm_attr(ea, SEGATTR_ALIGN, alignment)
def SegComb(ea, comb): return set_segm_attr(ea, SEGATTR_COMB, comb)
def MakeComm(ea, cmt): return set_cmt(ea, cmt, 0)
def MakeRptCmt(ea, cmt): return set_cmt(ea, cmt, 1)
def MakeUnkn(ea, flags): return del_items(ea, flags)
def MakeUnknown(ea, size, flags): return del_items(ea, flags, size)
def LineA(ea, n): return get_extra_cmt(ea, E_PREV + (n))
def LineB(ea, n): return get_extra_cmt(ea, E_NEXT + (n))
def ExtLinA(ea, n, line): return update_extra_cmt(ea, E_PREV + (n), line)
def ExtLinB(ea, n, line): return update_extra_cmt(ea, E_NEXT + (n), line)
def DelExtLnA(ea, n): return del_extra_cmt(ea, E_PREV + (n))
def DelExtLnB(ea, n): return del_extra_cmt(ea, E_NEXT + (n))
def SetSpDiff(ea, delta): return add_user_stkpnt(ea, delta)
def AddUserStkPnt(ea, delta): return add_user_stkpnt(ea, delta)
def NameEx(From, ea): return get_name(ea, ida_name.GN_VISIBLE | calc_gtn_flags(From, ea))
def GetTrueNameEx(From, ea): return get_name(ea, calc_gtn_flags(From, ea))
Message=msg
UMessage=msg
def DelSeg(ea, flags): return del_segm(ea, flags)
def Wait(): return auto_wait()
def LoadTraceFile(filename): return load_trace_file(filename)
def SaveTraceFile(filename, description): return save_trace_file(filename, description)
def CheckTraceFile(filename): return is_valid_trace_file(filename)
def DiffTraceFile(filename): return diff_trace_file(filename)
def SetTraceDesc(filename, description): return get_trace_file_desc(filename, description)
def GetTraceDesc(filename): return set_trace_file_desc(filename)
def GetMaxTev(): return get_tev_qty()
def GetTevEa(tev): return get_tev_ea(tev)
def GetTevType(tev): return get_tev_type(tev)
def GetTevTid(tev): return get_tev_tid(tev)
def GetTevRegVal(tev, reg): return get_tev_reg(tev, reg)
def GetTevRegMemQty(tev): return get_tev_mem_qty(tev)
def GetTevRegMem(tev, idx): return get_tev_mem(tev, idx)
def GetTevRegMemEa(tev, idx): return get_tev_mem_ea(tev, idx)
def GetTevCallee(tev): return get_call_tev_callee(tev)
def GetTevReturn(tev): return get_ret_tev_return(tev)
def GetBptTevEa(tev): return get_bpt_tev_ea(tev)
def ArmForceBLJump(ea): return force_bl_jump(ea)
def ArmForceBLCall(ea): return force_bl_call(ea)
def StepBack(): return step_back()
def SetCurrentTev(event): return set_current_tev(event)
def GetCurrentTev(): return get_current_tev()
def BochsCommand(cmd): return send_dbg_command(cmd)
def SendGDBMonitor(cmd): return send_dbg_command(cmd)
def WinDbgCommand(cmd): return send_dbg_command(cmd)
def SetAppcallOptions(x): return set_inf_attr(INF_APPCALL_OPTIONS, x)
def GetAppcallOptions(): return get_inf_attr(INF_APPCALL_OPTIONS)
AF2_ANORET=ida_ida.AF_ANORET
AF2_CHKUNI=ida_ida.AF_CHKUNI
AF2_DATOFF=ida_ida.AF_DATOFF
AF2_DOCODE=ida_ida.AF_DOCODE
AF2_DODATA=ida_ida.AF_DODATA
AF2_FTAIL=ida_ida.AF_FTAIL
AF2_HFLIRT=ida_ida.AF_HFLIRT
AF2_JUMPTBL=ida_ida.AF_JUMPTBL
AF2_PURDAT=ida_ida.AF_PURDAT
AF2_REGARG=ida_ida.AF_REGARG
AF2_SIGCMT=ida_ida.AF_SIGCMT
AF2_SIGMLT=ida_ida.AF_SIGMLT
AF2_STKARG=ida_ida.AF_STKARG
AF2_TRFUNC=ida_ida.AF_TRFUNC
AF2_VERSP=ida_ida.AF_VERSP
AF_ASCII=ida_ida.AF_STRLIT
ASCF_AUTO=ida_ida.STRF_AUTO
ASCF_COMMENT=ida_ida.STRF_COMMENT
ASCF_GEN=ida_ida.STRF_GEN
ASCF_SAVECASE=ida_ida.STRF_SAVECASE
ASCF_SERIAL=ida_ida.STRF_SERIAL
ASCSTR_C=ida_nalt.STRTYPE_C
ASCSTR_LEN2=STRTYPE_LEN2
ASCSTR_LEN4=STRTYPE_LEN4
ASCSTR_PASCAL=ida_nalt.STRTYPE_PASCAL
ASCSTR_TERMCHR=ida_nalt.STRTYPE_TERMCHR
ASCSTR_ULEN2=ida_nalt.STRTYPE_LEN2_16
ASCSTR_ULEN4=ida_nalt.STRTYPE_LEN4_16
ASCSTR_UNICODE=ida_nalt.STRTYPE_C_16
BeginEA=StartEA
DOUNK_SIMPLE=DELIT_SIMPLE
DOUNK_EXPAND=DELIT_EXPAND
DOUNK_DELNAMES=DELIT_DELNAMES
DelHiddenArea=DelHiddenRange
FF_ASCI=FF_STRLIT
FF_DWRD=FF_DWORD
FF_OWRD=FF_OWORD
FF_QWRD=FF_QWORD
FF_STRU=FF_STRUCT
FF_TBYT=FF_TBYTE
FF_VAR=0x00080000
FIXUP_BYTE=ida_fixup.FIXUP_OFF8
FIXUP_CREATED=ida_fixup.FIXUPF_CREATED
FIXUP_EXTDEF=ida_fixup.FIXUPF_EXTDEF
FIXUP_REL=ida_fixup.FIXUPF_REL
FIXUP_SELFREL=0
FIXUP_UNUSED=ida_fixup.FIXUPF_UNUSED
GetFlags=get_full_flags
HideArea=HideRange
ResumeProcess=resume_process
def isEnabled(ea): return ida_bytes.is_mapped(ea)
def hasValue(F): return has_value(F)
def isByte(F): return is_byte(F)
def isWord(F): return is_word(F)
def isDwrd(F): return is_dword(F)
def isQwrd(F): return is_qword(F)
def isOwrd(F): return is_oword(F)
def isTbyt(F): return is_tbyte(F)
def isFloat(F): return is_float(F)
def isDouble(F): return is_double(F)
def isASCII(F): return is_strlit(F)
def isStruct(F): return is_struct(F)
def isAlign(F): return is_align(F)
def isChar0(F): return is_char0(F)
def isChar1(F): return is_char1(F)
def isCode(F): return is_code(F)
def isData(F): return is_data(F)
def isDefArg0(F): return is_defarg0(F)
def isDefArg1(F): return is_defarg1(F)
def isEnum0(F): return is_enum0(F)
def isEnum1(F): return is_enum1(F)
def isFlow(F): return is_flow(F)
def isHead(F): return is_head(F)
def isLoaded(F): return is_loaded(F)
def isOff0(F): return is_off0(F)
def isOff1(F): return is_off1(F)
def isPackReal(F): return is_pack_real(F)
def isSeg0(F): return is_seg0(F)
def isSeg1(F): return is_seg1(F)
def isStkvar0(F): return is_stkvar0(F)
def isStkvar1(F): return is_stkvar1(F)
def isStroff0(F): return is_stroff0(F)
def isStroff1(F): return is_stroff1(F)
def isTail(F): return is_tail(F)
def isUnknown(F): return is_unknown(F)
SEGDEL_KEEP=ida_segment.SEGMOD_KEEP
SEGDEL_PERM=ida_segment.SEGMOD_KILL
SEGDEL_SILENT=ida_segment.SEGMOD_SILENT
SETPROC_ALL=ida_idp.SETPROC_LOADER_NON_FATAL
SETPROC_COMPAT=ida_idp.SETPROC_IDB
SETPROC_FATAL=ida_idp.SETPROC_LOADER
INF_CHANGE_COUNTER=INF_DATABASE_CHANGE_COUNT
INF_LOW_OFF=INF_LOWOFF
INF_HIGH_OFF=INF_HIGHOFF
INF_START_PRIVRANGE=INF_PRIVRANGE_START_EA
INF_END_PRIVRANGE=INF_PRIVRANGE_END_EA
INF_TYPE_XREFS=INF_TYPE_XREFNUM
INF_REFCMTS=INF_REFCMTNUM
INF_XREFS=INF_XREFFLAG
INF_NAMELEN=INF_MAX_AUTONAME_LEN
INF_SHORT_DN=INF_SHORT_DEMNAMES
INF_LONG_DN=INF_LONG_DEMNAMES
INF_CMTFLAG=INF_CMTFLG
INF_BORDER=INF_LIMITER
INF_BINPREF=INF_BIN_PREFIX_SIZE
INF_COMPILER=INF_CC_ID
INF_MODEL=INF_CC_CM
INF_SIZEOF_INT=INF_CC_SIZE_I
INF_SIZEOF_BOOL=INF_CC_SIZE_B
INF_SIZEOF_ENUM=INF_CC_SIZE_E
INF_SIZEOF_ALGN=INF_CC_DEFALIGN
INF_SIZEOF_SHORT=INF_CC_SIZE_S
INF_SIZEOF_LONG=INF_CC_SIZE_L
INF_SIZEOF_LLONG=INF_CC_SIZE_LL
INF_SIZEOF_LDBL=INF_CC_SIZE_LDBL
REF_VHIGH=ida_nalt.V695_REF_VHIGH
REF_VLOW=ida_nalt.V695_REF_VLOW
def GetOpnd(ea, n): return print_operand(ea, n)
def patch_long(ea, value): return patch_dword(ea, value)
def python_on(): return load_and_run_plugin("idapython", 3)
def RunPythonStatement(stmt): return exec_python(stmt)
