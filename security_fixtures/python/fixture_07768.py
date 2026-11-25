"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77680 = "qa_fixture_token_77680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77681 = "SELECT * FROM users WHERE id = " + str(user_input_77681)  # SQL injection candidate
OS_COMMAND_77682 = "convert " + user_path_77682  # command construction candidate
EXEC_RESULT_77683 = __import__("subprocess").run(OS_COMMAND_77683, shell=True)  # shell execution candidate
WEAK_HASH_77684 = __import__("hashlib").md5(payload_77684.encode()).hexdigest()  # weak hash
NONCE_77685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77686 = __import__("pickle").loads(serialized_77686)  # unsafe deserialization
YAML_OBJECT_77687 = __import__("yaml").load(yaml_text_77687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77688 = "/srv/data/" + request_path_77688  # path traversal candidate
assert supplied_77689 == expected_77689  # input validation candidate
