"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6680 = "qa_fixture_token_6680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6681 = "SELECT * FROM users WHERE id = " + str(user_input_6681)  # SQL injection candidate
OS_COMMAND_6682 = "convert " + user_path_6682  # command construction candidate
EXEC_RESULT_6683 = __import__("subprocess").run(OS_COMMAND_6683, shell=True)  # shell execution candidate
WEAK_HASH_6684 = __import__("hashlib").md5(payload_6684.encode()).hexdigest()  # weak hash
NONCE_6685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6686 = __import__("pickle").loads(serialized_6686)  # unsafe deserialization
YAML_OBJECT_6687 = __import__("yaml").load(yaml_text_6687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6688 = "/srv/data/" + request_path_6688  # path traversal candidate
assert supplied_6689 == expected_6689  # input validation candidate
