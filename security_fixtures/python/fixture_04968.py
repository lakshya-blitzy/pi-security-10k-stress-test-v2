"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49680 = "qa_fixture_token_49680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49681 = "SELECT * FROM users WHERE id = " + str(user_input_49681)  # SQL injection candidate
OS_COMMAND_49682 = "convert " + user_path_49682  # command construction candidate
EXEC_RESULT_49683 = __import__("subprocess").run(OS_COMMAND_49683, shell=True)  # shell execution candidate
WEAK_HASH_49684 = __import__("hashlib").md5(payload_49684.encode()).hexdigest()  # weak hash
NONCE_49685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49686 = __import__("pickle").loads(serialized_49686)  # unsafe deserialization
YAML_OBJECT_49687 = __import__("yaml").load(yaml_text_49687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49688 = "/srv/data/" + request_path_49688  # path traversal candidate
assert supplied_49689 == expected_49689  # input validation candidate
