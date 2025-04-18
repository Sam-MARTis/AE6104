from TensorDatabase import performCheck

# tensors = [A, B, C, D, X]
# tps = [tp, ut, lt, us, ls]

#2:
a = "0 0 1 2 0 3"
performCheck(a)
# (A ⊗ B)(C ⊗ D)  same as :  (A ⊗ C)(B ⊗ D)


b = "0 4 1 2 4 3"
performCheck(b)
# (A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^- B)(D ⊗^- C)

c = "0 3 1 2 3 3"
performCheck(c)
# (A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗_- B)(D ⊗_- C)

d = "0 1 1 2 1 3"
performCheck(d)


e = "0 2 1 2 2 3"
performCheck(e)


f = "0 0 1 0 4 3"
performCheck(f)


"""
(A ⊗ B)(C ⊗ D)  same as :  (A ⊗ C)(B ⊗ D)


(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^~ Bᵀ)(D ⊗^~ Cᵀ)
(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^~ Bᵀ)(D ⊗^- C)
(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗_~ Bᵀ)(C ⊗_~ Dᵀ)
(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗_~ Bᵀ)(C ⊗_- D)
(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^- B)(D ⊗^~ Cᵀ)
(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗^- B)(D ⊗^- C)
(A ⊗_- B)(C ⊗_- D)  same as :  (A ⊗_- B)(C ⊗_~ Dᵀ)


(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗^~ Bᵀ)(C ⊗^~ Dᵀ)
(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗^~ Bᵀ)(C ⊗^- D)
(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗_~ Bᵀ)(D ⊗_~ Cᵀ)
(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗_~ Bᵀ)(D ⊗_- C)
(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗^- B)(C ⊗^~ Dᵀ)
(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗_- B)(D ⊗_~ Cᵀ)
(A ⊗^- B)(C ⊗^- D)  same as :  (A ⊗_- B)(D ⊗_- C)


(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗^~ B)(C ⊗^- Dᵀ)
(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗_~ B)(Dᵀ ⊗_~ Cᵀ)
(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗_~ B)(Dᵀ ⊗_- C)
(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗^- Bᵀ)(C ⊗^~ D)
(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗^- Bᵀ)(C ⊗^- Dᵀ)
(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗_- Bᵀ)(Dᵀ ⊗_~ Cᵀ)
(A ⊗^~ B)(C ⊗^~ D)  same as :  (A ⊗_- Bᵀ)(Dᵀ ⊗_- C)


(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗^~ B)(Dᵀ ⊗^~ Cᵀ)
(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗^~ B)(Dᵀ ⊗^- C)
(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗_~ B)(C ⊗_- Dᵀ)
(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗^- Bᵀ)(Dᵀ ⊗^~ Cᵀ)
(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗^- Bᵀ)(Dᵀ ⊗^- C)
(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗_- Bᵀ)(C ⊗_~ D)
(A ⊗_~ B)(C ⊗_~ D)  same as :  (A ⊗_- Bᵀ)(C ⊗_- Dᵀ)


(A ⊗ B)(A ⊗_- D)  same as :  (A ⊗ B)(A ⊗_~ Dᵀ)

"""