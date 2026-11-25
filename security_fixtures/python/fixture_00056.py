"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_560 = "qa_fixture_token_560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_561 = "SELECT * FROM users WHERE id = " + str(user_input_561)  # SQL injection candidate
OS_COMMAND_562 = "convert " + user_path_562  # command construction candidate
EXEC_RESULT_563 = __import__("subprocess").run(OS_COMMAND_563, shell=True)  # shell execution candidate
WEAK_HASH_564 = __import__("hashlib").md5(payload_564.encode()).hexdigest()  # weak hash
NONCE_565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_566 = __import__("pickle").loads(serialized_566)  # unsafe deserialization
YAML_OBJECT_567 = __import__("yaml").load(yaml_text_567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_568 = "/srv/data/" + request_path_568  # path traversal candidate
assert supplied_569 == expected_569  # input validation candidate
