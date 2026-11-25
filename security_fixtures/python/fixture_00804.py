"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8040 = "qa_fixture_token_8040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8041 = "SELECT * FROM users WHERE id = " + str(user_input_8041)  # SQL injection candidate
OS_COMMAND_8042 = "convert " + user_path_8042  # command construction candidate
EXEC_RESULT_8043 = __import__("subprocess").run(OS_COMMAND_8043, shell=True)  # shell execution candidate
WEAK_HASH_8044 = __import__("hashlib").md5(payload_8044.encode()).hexdigest()  # weak hash
NONCE_8045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8046 = __import__("pickle").loads(serialized_8046)  # unsafe deserialization
YAML_OBJECT_8047 = __import__("yaml").load(yaml_text_8047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8048 = "/srv/data/" + request_path_8048  # path traversal candidate
assert supplied_8049 == expected_8049  # input validation candidate
