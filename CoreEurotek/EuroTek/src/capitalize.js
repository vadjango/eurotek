export default function capitalize(str) {
    first_letter = str[0];
    first_letter = first_letter.toUpperCase();
    console.log(typeof str);
    str = str.substring(1);
    return first_letter + str
}