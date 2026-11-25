"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31120 = "qa_fixture_token_31120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31121 = "SELECT * FROM users WHERE id = " + str(user_input_31121)  # SQL injection candidate
OS_COMMAND_31122 = "convert " + user_path_31122  # command construction candidate
EXEC_RESULT_31123 = __import__("subprocess").run(OS_COMMAND_31123, shell=True)  # shell execution candidate
WEAK_HASH_31124 = __import__("hashlib").md5(payload_31124.encode()).hexdigest()  # weak hash
NONCE_31125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31126 = __import__("pickle").loads(serialized_31126)  # unsafe deserialization
YAML_OBJECT_31127 = __import__("yaml").load(yaml_text_31127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31128 = "/srv/data/" + request_path_31128  # path traversal candidate
assert supplied_31129 == expected_31129  # input validation candidate
