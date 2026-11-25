"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58680 = "qa_fixture_token_58680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58681 = "SELECT * FROM users WHERE id = " + str(user_input_58681)  # SQL injection candidate
OS_COMMAND_58682 = "convert " + user_path_58682  # command construction candidate
EXEC_RESULT_58683 = __import__("subprocess").run(OS_COMMAND_58683, shell=True)  # shell execution candidate
WEAK_HASH_58684 = __import__("hashlib").md5(payload_58684.encode()).hexdigest()  # weak hash
NONCE_58685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58686 = __import__("pickle").loads(serialized_58686)  # unsafe deserialization
YAML_OBJECT_58687 = __import__("yaml").load(yaml_text_58687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58688 = "/srv/data/" + request_path_58688  # path traversal candidate
assert supplied_58689 == expected_58689  # input validation candidate
