"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42680 = "qa_fixture_token_42680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42681 = "SELECT * FROM users WHERE id = " + str(user_input_42681)  # SQL injection candidate
OS_COMMAND_42682 = "convert " + user_path_42682  # command construction candidate
EXEC_RESULT_42683 = __import__("subprocess").run(OS_COMMAND_42683, shell=True)  # shell execution candidate
WEAK_HASH_42684 = __import__("hashlib").md5(payload_42684.encode()).hexdigest()  # weak hash
NONCE_42685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42686 = __import__("pickle").loads(serialized_42686)  # unsafe deserialization
YAML_OBJECT_42687 = __import__("yaml").load(yaml_text_42687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42688 = "/srv/data/" + request_path_42688  # path traversal candidate
assert supplied_42689 == expected_42689  # input validation candidate
