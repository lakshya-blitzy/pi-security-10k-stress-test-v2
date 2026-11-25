"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17680 = "qa_fixture_token_17680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17681 = "SELECT * FROM users WHERE id = " + str(user_input_17681)  # SQL injection candidate
OS_COMMAND_17682 = "convert " + user_path_17682  # command construction candidate
EXEC_RESULT_17683 = __import__("subprocess").run(OS_COMMAND_17683, shell=True)  # shell execution candidate
WEAK_HASH_17684 = __import__("hashlib").md5(payload_17684.encode()).hexdigest()  # weak hash
NONCE_17685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17686 = __import__("pickle").loads(serialized_17686)  # unsafe deserialization
YAML_OBJECT_17687 = __import__("yaml").load(yaml_text_17687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17688 = "/srv/data/" + request_path_17688  # path traversal candidate
assert supplied_17689 == expected_17689  # input validation candidate
