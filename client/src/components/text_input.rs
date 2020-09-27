use yew::prelude::*;
use yew::events::{Event, ChangeData};
use yew::services::ConsoleService;

pub enum Msg {
  Submit,
  ValueUpdate(String),
}

pub struct TextInput {
  state: State,
  link: ComponentLink<Self>,
}

struct State {
  value: String,
}

impl Component for TextInput {
  type Message = Msg;
  type Properties = ();

  fn create(_: Self::Properties, link: ComponentLink<Self>) -> Self {
    Self { state: State {
      value: "".to_string(),
    }, link }
  }

  fn update(&mut self, msg: Self::Message) -> ShouldRender {
    match msg {
      Msg::Submit => {
        println!("Submit!")
      },
      Msg::ValueUpdate(value) => {
        self.state.value = value;
        ConsoleService::log(&format!("{}", &self.state.value));
      }
    }

    true
  }

  fn change(&mut self, _: Self::Properties) -> ShouldRender {
    true
  }

  fn view(&self) -> Html {
    let onsubmit = self.link.callback(|e: FocusEvent|{
      e.prevent_default();
      Msg::Submit
    });

    html! {
    <div class="mt-8">
      <form onsubmit=onsubmit>
        <label class="block text-indigo-100 text-lg font-bold mb-2" for="task">
        {"Task"}
      </label>
      <input 
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="task"
          type="text"
          placeholder="Input some task and press enter"
          oninput=self.link.callback(|e: InputData| Msg::ValueUpdate(e.value))
        />
      </form>
    </div>
    }
  }
}
