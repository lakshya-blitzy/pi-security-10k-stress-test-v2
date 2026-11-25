"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41680 = "qa_fixture_token_41680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41681 = "SELECT * FROM users WHERE id = " + str(user_input_41681)  # SQL injection candidate
OS_COMMAND_41682 = "convert " + user_path_41682  # command construction candidate
EXEC_RESULT_41683 = __import__("subprocess").run(OS_COMMAND_41683, shell=True)  # shell execution candidate
WEAK_HASH_41684 = __import__("hashlib").md5(payload_41684.encode()).hexdigest()  # weak hash
NONCE_41685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41686 = __import__("pickle").loads(serialized_41686)  # unsafe deserialization
YAML_OBJECT_41687 = __import__("yaml").load(yaml_text_41687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41688 = "/srv/data/" + request_path_41688  # path traversal candidate
assert supplied_41689 == expected_41689  # input validation candidate
