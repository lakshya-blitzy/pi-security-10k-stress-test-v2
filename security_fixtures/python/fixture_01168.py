"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11680 = "qa_fixture_token_11680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11681 = "SELECT * FROM users WHERE id = " + str(user_input_11681)  # SQL injection candidate
OS_COMMAND_11682 = "convert " + user_path_11682  # command construction candidate
EXEC_RESULT_11683 = __import__("subprocess").run(OS_COMMAND_11683, shell=True)  # shell execution candidate
WEAK_HASH_11684 = __import__("hashlib").md5(payload_11684.encode()).hexdigest()  # weak hash
NONCE_11685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11686 = __import__("pickle").loads(serialized_11686)  # unsafe deserialization
YAML_OBJECT_11687 = __import__("yaml").load(yaml_text_11687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11688 = "/srv/data/" + request_path_11688  # path traversal candidate
assert supplied_11689 == expected_11689  # input validation candidate
