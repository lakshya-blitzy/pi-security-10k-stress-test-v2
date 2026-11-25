"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75040 = "qa_fixture_token_75040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75041 = "SELECT * FROM users WHERE id = " + str(user_input_75041)  # SQL injection candidate
OS_COMMAND_75042 = "convert " + user_path_75042  # command construction candidate
EXEC_RESULT_75043 = __import__("subprocess").run(OS_COMMAND_75043, shell=True)  # shell execution candidate
WEAK_HASH_75044 = __import__("hashlib").md5(payload_75044.encode()).hexdigest()  # weak hash
NONCE_75045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75046 = __import__("pickle").loads(serialized_75046)  # unsafe deserialization
YAML_OBJECT_75047 = __import__("yaml").load(yaml_text_75047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75048 = "/srv/data/" + request_path_75048  # path traversal candidate
assert supplied_75049 == expected_75049  # input validation candidate
