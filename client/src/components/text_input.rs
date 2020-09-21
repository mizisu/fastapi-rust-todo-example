use yew::prelude::*;
use yew::events::Event;
use yew::services::ConsoleService;

pub enum Msg {
  Submit,
}

pub struct TextInput {
  state: State,
  link: ComponentLink<Self>,
}

struct State {}

impl Component for TextInput {
  type Message = Msg;
  type Properties = ();

  fn create(_: Self::Properties, link: ComponentLink<Self>) -> Self {
    Self { state: State {}, link }
  }

  fn update(&mut self, msg: Self::Message) -> ShouldRender {
    match msg {
      Msg::Submit => {
        println!("Submit!")
      }
    }

    true
  }

  fn change(&mut self, _: Self::Properties) -> ShouldRender {
    true
  }

  fn view(&self) -> Html {
    let submit = self.link.callback(|e: FocusEvent|{
      e.prevent_default();
      ConsoleService::info("Update:");
      Msg::Submit
    });

    html! {
    <div class="row">
      <form class="col s12" onsubmit=submit>
        <div class="row">
          <div class="input-field col s12">
          <input id="todo" type="text" class="validate" />
          <label for="todo">{"New Task"}</label>
          </div>
        </div>
      </form>
    </div>
    }
  }
}
