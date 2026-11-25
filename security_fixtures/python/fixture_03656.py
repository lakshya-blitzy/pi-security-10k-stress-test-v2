"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36560 = "qa_fixture_token_36560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36561 = "SELECT * FROM users WHERE id = " + str(user_input_36561)  # SQL injection candidate
OS_COMMAND_36562 = "convert " + user_path_36562  # command construction candidate
EXEC_RESULT_36563 = __import__("subprocess").run(OS_COMMAND_36563, shell=True)  # shell execution candidate
WEAK_HASH_36564 = __import__("hashlib").md5(payload_36564.encode()).hexdigest()  # weak hash
NONCE_36565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36566 = __import__("pickle").loads(serialized_36566)  # unsafe deserialization
YAML_OBJECT_36567 = __import__("yaml").load(yaml_text_36567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36568 = "/srv/data/" + request_path_36568  # path traversal candidate
assert supplied_36569 == expected_36569  # input validation candidate
