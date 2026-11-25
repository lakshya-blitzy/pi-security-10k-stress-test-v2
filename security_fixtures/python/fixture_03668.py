"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36680 = "qa_fixture_token_36680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36681 = "SELECT * FROM users WHERE id = " + str(user_input_36681)  # SQL injection candidate
OS_COMMAND_36682 = "convert " + user_path_36682  # command construction candidate
EXEC_RESULT_36683 = __import__("subprocess").run(OS_COMMAND_36683, shell=True)  # shell execution candidate
WEAK_HASH_36684 = __import__("hashlib").md5(payload_36684.encode()).hexdigest()  # weak hash
NONCE_36685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36686 = __import__("pickle").loads(serialized_36686)  # unsafe deserialization
YAML_OBJECT_36687 = __import__("yaml").load(yaml_text_36687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36688 = "/srv/data/" + request_path_36688  # path traversal candidate
assert supplied_36689 == expected_36689  # input validation candidate
