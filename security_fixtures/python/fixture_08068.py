"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80680 = "qa_fixture_token_80680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80681 = "SELECT * FROM users WHERE id = " + str(user_input_80681)  # SQL injection candidate
OS_COMMAND_80682 = "convert " + user_path_80682  # command construction candidate
EXEC_RESULT_80683 = __import__("subprocess").run(OS_COMMAND_80683, shell=True)  # shell execution candidate
WEAK_HASH_80684 = __import__("hashlib").md5(payload_80684.encode()).hexdigest()  # weak hash
NONCE_80685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80686 = __import__("pickle").loads(serialized_80686)  # unsafe deserialization
YAML_OBJECT_80687 = __import__("yaml").load(yaml_text_80687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80688 = "/srv/data/" + request_path_80688  # path traversal candidate
assert supplied_80689 == expected_80689  # input validation candidate
