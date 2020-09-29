use yew::events::{Event, InputData};
use yew::prelude::*;
use yew::services::ConsoleService;

pub enum Msg {}

pub struct TodoList {
    state: State,
    link: ComponentLink<Self>,
}

struct State {}

impl Component for TodoList {
    type Message = Msg;
    type Properties = ();

    fn create(_: Self::Properties, link: ComponentLink<Self>) -> Self {
        Self {
            state: State {},
            link,
        }
    }

    fn update(&mut self, msg: Self::Message) -> ShouldRender {
        match msg {}

        true
    }

    fn change(&mut self, _: Self::Properties) -> ShouldRender {
        true
    }

    fn view(&self) -> Html {
        let items = ["item1", "item2"];

        let rendered_items = items.iter().map(|item| {
            html! {
                <div class="shadow-lg bg-indigo-400 rounded mt-3">
                    <label class="items-center flex h-12">
                        <input type="checkbox" class="form-checkbox h-6 w-6 mt-1 ml-3 rounded"/>
                        <span class="ml-4 text-xl">{"adf"}</span>
                        <button class="bg-indigo-100 hover:bg-indigo-200 py-2 px-4 rounded ml-auto">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M3 6v18h18v-18h-18zm5 14c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/></svg>
                        </button>
                    </label>
                </div>
            }
        }).collect::<Html>();

        html! {
        <div class="row mt-8">
            <div class="col s12">
                {rendered_items}
            </div>
        </div>
        }
    }
}
