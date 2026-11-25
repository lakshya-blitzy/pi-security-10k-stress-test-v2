"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96560 = "qa_fixture_token_96560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96561 = "SELECT * FROM users WHERE id = " + str(user_input_96561)  # SQL injection candidate
OS_COMMAND_96562 = "convert " + user_path_96562  # command construction candidate
EXEC_RESULT_96563 = __import__("subprocess").run(OS_COMMAND_96563, shell=True)  # shell execution candidate
WEAK_HASH_96564 = __import__("hashlib").md5(payload_96564.encode()).hexdigest()  # weak hash
NONCE_96565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96566 = __import__("pickle").loads(serialized_96566)  # unsafe deserialization
YAML_OBJECT_96567 = __import__("yaml").load(yaml_text_96567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96568 = "/srv/data/" + request_path_96568  # path traversal candidate
assert supplied_96569 == expected_96569  # input validation candidate
