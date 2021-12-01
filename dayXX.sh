#!/usr/bin/env sh


main() {
    printf -v day "%0.2d" "${1}"
    src_filename="${day}/day${day}.py"

    mkdir -p "$1"
    cat > "${src_filename}" <<EOF
#!/usr/bin/env python3


def main():
    pass


def solve1():
    pass


def solve2():
    pass


if __name__ == "__main__":
    main()

EOF

    chmod +x "${src_filename}"
}

main "$@"
