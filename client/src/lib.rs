mod pages;

use wasm_bindgen::prelude::*;
use yew::prelude::*;


#[wasm_bindgen(start)]
pub fn run_app() {
    App::<>::new().mount_to_body();
}
