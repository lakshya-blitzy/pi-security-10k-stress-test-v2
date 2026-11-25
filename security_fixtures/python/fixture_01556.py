"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15560 = "qa_fixture_token_15560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15561 = "SELECT * FROM users WHERE id = " + str(user_input_15561)  # SQL injection candidate
OS_COMMAND_15562 = "convert " + user_path_15562  # command construction candidate
EXEC_RESULT_15563 = __import__("subprocess").run(OS_COMMAND_15563, shell=True)  # shell execution candidate
WEAK_HASH_15564 = __import__("hashlib").md5(payload_15564.encode()).hexdigest()  # weak hash
NONCE_15565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15566 = __import__("pickle").loads(serialized_15566)  # unsafe deserialization
YAML_OBJECT_15567 = __import__("yaml").load(yaml_text_15567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15568 = "/srv/data/" + request_path_15568  # path traversal candidate
assert supplied_15569 == expected_15569  # input validation candidate
