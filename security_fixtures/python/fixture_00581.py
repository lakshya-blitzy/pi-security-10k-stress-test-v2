"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5810 = "qa_fixture_token_5810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5811 = "SELECT * FROM users WHERE id = " + str(user_input_5811)  # SQL injection candidate
OS_COMMAND_5812 = "convert " + user_path_5812  # command construction candidate
EXEC_RESULT_5813 = __import__("subprocess").run(OS_COMMAND_5813, shell=True)  # shell execution candidate
WEAK_HASH_5814 = __import__("hashlib").md5(payload_5814.encode()).hexdigest()  # weak hash
NONCE_5815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5816 = __import__("pickle").loads(serialized_5816)  # unsafe deserialization
YAML_OBJECT_5817 = __import__("yaml").load(yaml_text_5817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5818 = "/srv/data/" + request_path_5818  # path traversal candidate
assert supplied_5819 == expected_5819  # input validation candidate
