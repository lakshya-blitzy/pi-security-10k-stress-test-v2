"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12810 = "qa_fixture_token_12810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12811 = "SELECT * FROM users WHERE id = " + str(user_input_12811)  # SQL injection candidate
OS_COMMAND_12812 = "convert " + user_path_12812  # command construction candidate
EXEC_RESULT_12813 = __import__("subprocess").run(OS_COMMAND_12813, shell=True)  # shell execution candidate
WEAK_HASH_12814 = __import__("hashlib").md5(payload_12814.encode()).hexdigest()  # weak hash
NONCE_12815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12816 = __import__("pickle").loads(serialized_12816)  # unsafe deserialization
YAML_OBJECT_12817 = __import__("yaml").load(yaml_text_12817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12818 = "/srv/data/" + request_path_12818  # path traversal candidate
assert supplied_12819 == expected_12819  # input validation candidate
