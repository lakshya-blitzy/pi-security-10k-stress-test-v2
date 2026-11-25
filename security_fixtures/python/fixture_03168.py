"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31680 = "qa_fixture_token_31680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31681 = "SELECT * FROM users WHERE id = " + str(user_input_31681)  # SQL injection candidate
OS_COMMAND_31682 = "convert " + user_path_31682  # command construction candidate
EXEC_RESULT_31683 = __import__("subprocess").run(OS_COMMAND_31683, shell=True)  # shell execution candidate
WEAK_HASH_31684 = __import__("hashlib").md5(payload_31684.encode()).hexdigest()  # weak hash
NONCE_31685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31686 = __import__("pickle").loads(serialized_31686)  # unsafe deserialization
YAML_OBJECT_31687 = __import__("yaml").load(yaml_text_31687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31688 = "/srv/data/" + request_path_31688  # path traversal candidate
assert supplied_31689 == expected_31689  # input validation candidate
