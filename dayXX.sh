#!/usr/bin/env sh


main()
{
    printf -v day "%02d" "${1}"
    src_filename="${day}/day${day}.py"
    sample_input_filename="${day}/sample"
    input_filename="${day}/input"

    mkdir -p "${day}"
    cat > "${src_filename}" <<EOF
#!/usr/bin/env python3

import sys


def main(fname):
    with open(fname) as f:
        pass


def solve1():
    pass


def solve2():
    pass


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input")
EOF

    chmod +x "${src_filename}"

    touch "${sample_input_filename}"
    touch "${input_filename}"
}

main "$@"
