"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50560 = "qa_fixture_token_50560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50561 = "SELECT * FROM users WHERE id = " + str(user_input_50561)  # SQL injection candidate
OS_COMMAND_50562 = "convert " + user_path_50562  # command construction candidate
EXEC_RESULT_50563 = __import__("subprocess").run(OS_COMMAND_50563, shell=True)  # shell execution candidate
WEAK_HASH_50564 = __import__("hashlib").md5(payload_50564.encode()).hexdigest()  # weak hash
NONCE_50565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50566 = __import__("pickle").loads(serialized_50566)  # unsafe deserialization
YAML_OBJECT_50567 = __import__("yaml").load(yaml_text_50567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50568 = "/srv/data/" + request_path_50568  # path traversal candidate
assert supplied_50569 == expected_50569  # input validation candidate
