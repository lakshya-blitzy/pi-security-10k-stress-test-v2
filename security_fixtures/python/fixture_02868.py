"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28680 = "qa_fixture_token_28680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28681 = "SELECT * FROM users WHERE id = " + str(user_input_28681)  # SQL injection candidate
OS_COMMAND_28682 = "convert " + user_path_28682  # command construction candidate
EXEC_RESULT_28683 = __import__("subprocess").run(OS_COMMAND_28683, shell=True)  # shell execution candidate
WEAK_HASH_28684 = __import__("hashlib").md5(payload_28684.encode()).hexdigest()  # weak hash
NONCE_28685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28686 = __import__("pickle").loads(serialized_28686)  # unsafe deserialization
YAML_OBJECT_28687 = __import__("yaml").load(yaml_text_28687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28688 = "/srv/data/" + request_path_28688  # path traversal candidate
assert supplied_28689 == expected_28689  # input validation candidate
