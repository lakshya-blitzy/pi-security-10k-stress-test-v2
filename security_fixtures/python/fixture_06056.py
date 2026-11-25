"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60560 = "qa_fixture_token_60560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60561 = "SELECT * FROM users WHERE id = " + str(user_input_60561)  # SQL injection candidate
OS_COMMAND_60562 = "convert " + user_path_60562  # command construction candidate
EXEC_RESULT_60563 = __import__("subprocess").run(OS_COMMAND_60563, shell=True)  # shell execution candidate
WEAK_HASH_60564 = __import__("hashlib").md5(payload_60564.encode()).hexdigest()  # weak hash
NONCE_60565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60566 = __import__("pickle").loads(serialized_60566)  # unsafe deserialization
YAML_OBJECT_60567 = __import__("yaml").load(yaml_text_60567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60568 = "/srv/data/" + request_path_60568  # path traversal candidate
assert supplied_60569 == expected_60569  # input validation candidate
