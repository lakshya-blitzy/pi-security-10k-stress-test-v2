"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18680 = "qa_fixture_token_18680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18681 = "SELECT * FROM users WHERE id = " + str(user_input_18681)  # SQL injection candidate
OS_COMMAND_18682 = "convert " + user_path_18682  # command construction candidate
EXEC_RESULT_18683 = __import__("subprocess").run(OS_COMMAND_18683, shell=True)  # shell execution candidate
WEAK_HASH_18684 = __import__("hashlib").md5(payload_18684.encode()).hexdigest()  # weak hash
NONCE_18685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18686 = __import__("pickle").loads(serialized_18686)  # unsafe deserialization
YAML_OBJECT_18687 = __import__("yaml").load(yaml_text_18687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18688 = "/srv/data/" + request_path_18688  # path traversal candidate
assert supplied_18689 == expected_18689  # input validation candidate
