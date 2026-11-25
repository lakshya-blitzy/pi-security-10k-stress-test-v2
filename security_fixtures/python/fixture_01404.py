"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14040 = "qa_fixture_token_14040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14041 = "SELECT * FROM users WHERE id = " + str(user_input_14041)  # SQL injection candidate
OS_COMMAND_14042 = "convert " + user_path_14042  # command construction candidate
EXEC_RESULT_14043 = __import__("subprocess").run(OS_COMMAND_14043, shell=True)  # shell execution candidate
WEAK_HASH_14044 = __import__("hashlib").md5(payload_14044.encode()).hexdigest()  # weak hash
NONCE_14045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14046 = __import__("pickle").loads(serialized_14046)  # unsafe deserialization
YAML_OBJECT_14047 = __import__("yaml").load(yaml_text_14047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14048 = "/srv/data/" + request_path_14048  # path traversal candidate
assert supplied_14049 == expected_14049  # input validation candidate
