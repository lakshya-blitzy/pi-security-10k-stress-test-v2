"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52400 = "qa_fixture_token_52400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52401 = "SELECT * FROM users WHERE id = " + str(user_input_52401)  # SQL injection candidate
OS_COMMAND_52402 = "convert " + user_path_52402  # command construction candidate
EXEC_RESULT_52403 = __import__("subprocess").run(OS_COMMAND_52403, shell=True)  # shell execution candidate
WEAK_HASH_52404 = __import__("hashlib").md5(payload_52404.encode()).hexdigest()  # weak hash
NONCE_52405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52406 = __import__("pickle").loads(serialized_52406)  # unsafe deserialization
YAML_OBJECT_52407 = __import__("yaml").load(yaml_text_52407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52408 = "/srv/data/" + request_path_52408  # path traversal candidate
assert supplied_52409 == expected_52409  # input validation candidate
