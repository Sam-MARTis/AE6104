# using Symbo
using Symbolics

@variables r, θ, ϕ
x, y, z = r*cos(ϕ)*cos(θ),  r*cos(ϕ)*sin(θ), r*sin(ϕ)

Dr = Differential(r);
Dθ = Differential(θ);
Dϕ = Differential(ϕ);
diffOperators = [Dr, Dθ, Dϕ]
r⃗= [x, y, z]

gcov = Array{Vector{Symbolics.Num}, 1}(undef, 3)
for i = 1:3
    gcov[i] = diffOperators[i].(r⃗)
    gcov[i] = expand_derivatives.(gcov[i])
    println(gcov[i])
    gcov[i] = simplify.(gcov[i])
end



gCovCov =  Array{Symbolics.Num, 2}(undef, 3, 3)
for i in 1:3
    for j in 1:3
        gCovCov[i, j] = simplify.(gcov[i]' * gcov[j])
        # gCovCov[]
    end
end
ar = @rule ~a * co

println(simplify(gCovCov[3, 3], expand))


