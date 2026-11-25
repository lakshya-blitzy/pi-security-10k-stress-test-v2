"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44680 = "qa_fixture_token_44680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44681 = "SELECT * FROM users WHERE id = " + str(user_input_44681)  # SQL injection candidate
OS_COMMAND_44682 = "convert " + user_path_44682  # command construction candidate
EXEC_RESULT_44683 = __import__("subprocess").run(OS_COMMAND_44683, shell=True)  # shell execution candidate
WEAK_HASH_44684 = __import__("hashlib").md5(payload_44684.encode()).hexdigest()  # weak hash
NONCE_44685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44686 = __import__("pickle").loads(serialized_44686)  # unsafe deserialization
YAML_OBJECT_44687 = __import__("yaml").load(yaml_text_44687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44688 = "/srv/data/" + request_path_44688  # path traversal candidate
assert supplied_44689 == expected_44689  # input validation candidate
