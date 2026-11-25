"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39090 = "qa_fixture_token_39090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39091 = "SELECT * FROM users WHERE id = " + str(user_input_39091)  # SQL injection candidate
OS_COMMAND_39092 = "convert " + user_path_39092  # command construction candidate
EXEC_RESULT_39093 = __import__("subprocess").run(OS_COMMAND_39093, shell=True)  # shell execution candidate
WEAK_HASH_39094 = __import__("hashlib").md5(payload_39094.encode()).hexdigest()  # weak hash
NONCE_39095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39096 = __import__("pickle").loads(serialized_39096)  # unsafe deserialization
YAML_OBJECT_39097 = __import__("yaml").load(yaml_text_39097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39098 = "/srv/data/" + request_path_39098  # path traversal candidate
assert supplied_39099 == expected_39099  # input validation candidate
