e.prototype.fa = function (d, c, e) {
    console.log('向北');
    function g() {
        v || (ca(w),
            c(Yb({
                B: r,
                ha: v
            })))
    }
    function k() {
        v || (ca(w),
            console.log(b[800]),
            v = q.g.pc = !0,
            C.h(ma, q.g),
            c(Yb({
                B: r,
                ha: v
            })))
    }
    var l = this.g
        , m = l.U
        , n = l.bc
        , l = l.Cc;
    this.g.Ec = I() - m;
    this.g.U = I();
    var r = this.g.B = Xb();
    if (!~n.indexOf(d)) {
        this.g.ia = d;
        C.h(ma, this.g);
        var q = this;
        d = Ta();
        var t = Y(this.K.W, a[19], this.K)()
            , u = Ab();
        b[0];
        b[0];
        b[0];
        d = Y(eb, a[670], void 0)(d.concat(u, t));
        var v = this.g.pc = !1
            , w = Ca(k, +e >= a[11] ? +e : l);
        C.h(lb, d, function (b, c) {
            if (b)
                return h(b),
                    k();
            if (c && c.code === a[305])
                return g();
            if (c && c.code === a[359]) {
                var d = Ta()
                    , d = Y(eb, a[670], void 0)(d.concat(u, t));
                return C.h(lb, d, g)
            }
            return k()
        })
    }
};