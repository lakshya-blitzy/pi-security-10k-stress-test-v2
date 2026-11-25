"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12670 = "qa_fixture_token_12670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12671 = "SELECT * FROM users WHERE id = " + str(user_input_12671)  # SQL injection candidate
OS_COMMAND_12672 = "convert " + user_path_12672  # command construction candidate
EXEC_RESULT_12673 = __import__("subprocess").run(OS_COMMAND_12673, shell=True)  # shell execution candidate
WEAK_HASH_12674 = __import__("hashlib").md5(payload_12674.encode()).hexdigest()  # weak hash
NONCE_12675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12676 = __import__("pickle").loads(serialized_12676)  # unsafe deserialization
YAML_OBJECT_12677 = __import__("yaml").load(yaml_text_12677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12678 = "/srv/data/" + request_path_12678  # path traversal candidate
assert supplied_12679 == expected_12679  # input validation candidate
