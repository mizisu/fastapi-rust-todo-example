use crate::types::Todo;
use anyhow::Error;
use yew::callback::Callback;
use yew::format::{Json, Nothing};
use yew::services::fetch::{FetchService, FetchTask, Request, Response};

pub type FetchResponse<T> = Response<Json<Result<T, Error>>>;
type FetchCallback<T> = Callback<FetchResponse<T>>;

const API_URL: str = "http://localhost:8000";

pub fn get_todos(callback: FetchCallback<Vec<Todo>>) -> FetchTask {
    let req = Request::get(format!("{}/api/v1/todos/", API_URL))
        .body(Nothing)
        .unwrap();

    FetchService::fetch(req, callback).unwrap()
}
