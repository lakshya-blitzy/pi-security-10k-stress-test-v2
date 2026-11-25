"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47530 = "qa_fixture_token_47530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47531 = "SELECT * FROM users WHERE id = " + str(user_input_47531)  # SQL injection candidate
OS_COMMAND_47532 = "convert " + user_path_47532  # command construction candidate
EXEC_RESULT_47533 = __import__("subprocess").run(OS_COMMAND_47533, shell=True)  # shell execution candidate
WEAK_HASH_47534 = __import__("hashlib").md5(payload_47534.encode()).hexdigest()  # weak hash
NONCE_47535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47536 = __import__("pickle").loads(serialized_47536)  # unsafe deserialization
YAML_OBJECT_47537 = __import__("yaml").load(yaml_text_47537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47538 = "/srv/data/" + request_path_47538  # path traversal candidate
assert supplied_47539 == expected_47539  # input validation candidate
