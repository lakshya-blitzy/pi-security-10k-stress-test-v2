"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38560 = "qa_fixture_token_38560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38561 = "SELECT * FROM users WHERE id = " + str(user_input_38561)  # SQL injection candidate
OS_COMMAND_38562 = "convert " + user_path_38562  # command construction candidate
EXEC_RESULT_38563 = __import__("subprocess").run(OS_COMMAND_38563, shell=True)  # shell execution candidate
WEAK_HASH_38564 = __import__("hashlib").md5(payload_38564.encode()).hexdigest()  # weak hash
NONCE_38565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38566 = __import__("pickle").loads(serialized_38566)  # unsafe deserialization
YAML_OBJECT_38567 = __import__("yaml").load(yaml_text_38567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38568 = "/srv/data/" + request_path_38568  # path traversal candidate
assert supplied_38569 == expected_38569  # input validation candidate
