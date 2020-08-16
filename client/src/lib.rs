mod pages;

use pages::Login;
use wasm_bindgen::prelude::*;
use yew::prelude::*;

#[wasm_bindgen(start)]
pub fn run_app() {
    App::<Login>::new().mount_to_body();
}
