use yew::prelude::*;
use yew_router::prelude::*;

use crate::pages::{Login, TodoListPage};
use crate::route::Route;

pub struct App {}

impl Component for App {
    type Message = ();
    type Properties = ();

    fn create(_: Self::Properties, _link: ComponentLink<Self>) -> Self {
        Self {}
    }

    fn update(&mut self, _msg: Self::Message) -> ShouldRender {
        true
    }

    fn change(&mut self, _: Self::Properties) -> ShouldRender {
        false
    }

    fn view(&self) -> Html {
        let render = Router::render(|switch: Route| match switch {
            Route::Login => html! { <Login/> },
            Route::TodoList => html! { <TodoListPage/> },
        });

        html! {
            <div class="m-auto">
                <nav>
                    <h1 class="uppercase text-4xl text-center mt-12 font-bold text-indigo-100" >{"Rust Todo List"}</h1>
                </nav>
                <div>
                    <Router<Route, ()> render=render/>
                </div>
            </div>
        }
    }
}
