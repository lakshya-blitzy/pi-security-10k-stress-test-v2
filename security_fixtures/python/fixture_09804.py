"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98040 = "qa_fixture_token_98040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98041 = "SELECT * FROM users WHERE id = " + str(user_input_98041)  # SQL injection candidate
OS_COMMAND_98042 = "convert " + user_path_98042  # command construction candidate
EXEC_RESULT_98043 = __import__("subprocess").run(OS_COMMAND_98043, shell=True)  # shell execution candidate
WEAK_HASH_98044 = __import__("hashlib").md5(payload_98044.encode()).hexdigest()  # weak hash
NONCE_98045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98046 = __import__("pickle").loads(serialized_98046)  # unsafe deserialization
YAML_OBJECT_98047 = __import__("yaml").load(yaml_text_98047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98048 = "/srv/data/" + request_path_98048  # path traversal candidate
assert supplied_98049 == expected_98049  # input validation candidate
