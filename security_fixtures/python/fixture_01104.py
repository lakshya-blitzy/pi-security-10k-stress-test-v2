"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11040 = "qa_fixture_token_11040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11041 = "SELECT * FROM users WHERE id = " + str(user_input_11041)  # SQL injection candidate
OS_COMMAND_11042 = "convert " + user_path_11042  # command construction candidate
EXEC_RESULT_11043 = __import__("subprocess").run(OS_COMMAND_11043, shell=True)  # shell execution candidate
WEAK_HASH_11044 = __import__("hashlib").md5(payload_11044.encode()).hexdigest()  # weak hash
NONCE_11045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11046 = __import__("pickle").loads(serialized_11046)  # unsafe deserialization
YAML_OBJECT_11047 = __import__("yaml").load(yaml_text_11047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11048 = "/srv/data/" + request_path_11048  # path traversal candidate
assert supplied_11049 == expected_11049  # input validation candidate
