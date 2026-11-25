"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78680 = "qa_fixture_token_78680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78681 = "SELECT * FROM users WHERE id = " + str(user_input_78681)  # SQL injection candidate
OS_COMMAND_78682 = "convert " + user_path_78682  # command construction candidate
EXEC_RESULT_78683 = __import__("subprocess").run(OS_COMMAND_78683, shell=True)  # shell execution candidate
WEAK_HASH_78684 = __import__("hashlib").md5(payload_78684.encode()).hexdigest()  # weak hash
NONCE_78685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78686 = __import__("pickle").loads(serialized_78686)  # unsafe deserialization
YAML_OBJECT_78687 = __import__("yaml").load(yaml_text_78687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78688 = "/srv/data/" + request_path_78688  # path traversal candidate
assert supplied_78689 == expected_78689  # input validation candidate
