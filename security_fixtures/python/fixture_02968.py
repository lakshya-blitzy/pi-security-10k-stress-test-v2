"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29680 = "qa_fixture_token_29680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29681 = "SELECT * FROM users WHERE id = " + str(user_input_29681)  # SQL injection candidate
OS_COMMAND_29682 = "convert " + user_path_29682  # command construction candidate
EXEC_RESULT_29683 = __import__("subprocess").run(OS_COMMAND_29683, shell=True)  # shell execution candidate
WEAK_HASH_29684 = __import__("hashlib").md5(payload_29684.encode()).hexdigest()  # weak hash
NONCE_29685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29686 = __import__("pickle").loads(serialized_29686)  # unsafe deserialization
YAML_OBJECT_29687 = __import__("yaml").load(yaml_text_29687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29688 = "/srv/data/" + request_path_29688  # path traversal candidate
assert supplied_29689 == expected_29689  # input validation candidate
