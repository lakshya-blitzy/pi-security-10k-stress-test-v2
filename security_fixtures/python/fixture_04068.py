"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40680 = "qa_fixture_token_40680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40681 = "SELECT * FROM users WHERE id = " + str(user_input_40681)  # SQL injection candidate
OS_COMMAND_40682 = "convert " + user_path_40682  # command construction candidate
EXEC_RESULT_40683 = __import__("subprocess").run(OS_COMMAND_40683, shell=True)  # shell execution candidate
WEAK_HASH_40684 = __import__("hashlib").md5(payload_40684.encode()).hexdigest()  # weak hash
NONCE_40685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40686 = __import__("pickle").loads(serialized_40686)  # unsafe deserialization
YAML_OBJECT_40687 = __import__("yaml").load(yaml_text_40687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40688 = "/srv/data/" + request_path_40688  # path traversal candidate
assert supplied_40689 == expected_40689  # input validation candidate
