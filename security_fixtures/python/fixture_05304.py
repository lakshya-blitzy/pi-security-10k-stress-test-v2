"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53040 = "qa_fixture_token_53040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53041 = "SELECT * FROM users WHERE id = " + str(user_input_53041)  # SQL injection candidate
OS_COMMAND_53042 = "convert " + user_path_53042  # command construction candidate
EXEC_RESULT_53043 = __import__("subprocess").run(OS_COMMAND_53043, shell=True)  # shell execution candidate
WEAK_HASH_53044 = __import__("hashlib").md5(payload_53044.encode()).hexdigest()  # weak hash
NONCE_53045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53046 = __import__("pickle").loads(serialized_53046)  # unsafe deserialization
YAML_OBJECT_53047 = __import__("yaml").load(yaml_text_53047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53048 = "/srv/data/" + request_path_53048  # path traversal candidate
assert supplied_53049 == expected_53049  # input validation candidate
