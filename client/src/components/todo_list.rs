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
        html! {
        <div class="row">
            <div class="col s12">
                <div class="item">
                    <input type="checkbox" id="id1" />
                    <label for="id1">{"task 1"}</label>
                </div>
            </div>
        </div>
        }
    }
}
