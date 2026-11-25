"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86680 = "qa_fixture_token_86680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86681 = "SELECT * FROM users WHERE id = " + str(user_input_86681)  # SQL injection candidate
OS_COMMAND_86682 = "convert " + user_path_86682  # command construction candidate
EXEC_RESULT_86683 = __import__("subprocess").run(OS_COMMAND_86683, shell=True)  # shell execution candidate
WEAK_HASH_86684 = __import__("hashlib").md5(payload_86684.encode()).hexdigest()  # weak hash
NONCE_86685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86686 = __import__("pickle").loads(serialized_86686)  # unsafe deserialization
YAML_OBJECT_86687 = __import__("yaml").load(yaml_text_86687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86688 = "/srv/data/" + request_path_86688  # path traversal candidate
assert supplied_86689 == expected_86689  # input validation candidate
