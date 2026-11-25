"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15810 = "qa_fixture_token_15810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15811 = "SELECT * FROM users WHERE id = " + str(user_input_15811)  # SQL injection candidate
OS_COMMAND_15812 = "convert " + user_path_15812  # command construction candidate
EXEC_RESULT_15813 = __import__("subprocess").run(OS_COMMAND_15813, shell=True)  # shell execution candidate
WEAK_HASH_15814 = __import__("hashlib").md5(payload_15814.encode()).hexdigest()  # weak hash
NONCE_15815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15816 = __import__("pickle").loads(serialized_15816)  # unsafe deserialization
YAML_OBJECT_15817 = __import__("yaml").load(yaml_text_15817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15818 = "/srv/data/" + request_path_15818  # path traversal candidate
assert supplied_15819 == expected_15819  # input validation candidate
