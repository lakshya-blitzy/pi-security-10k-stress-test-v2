"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12040 = "qa_fixture_token_12040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12041 = "SELECT * FROM users WHERE id = " + str(user_input_12041)  # SQL injection candidate
OS_COMMAND_12042 = "convert " + user_path_12042  # command construction candidate
EXEC_RESULT_12043 = __import__("subprocess").run(OS_COMMAND_12043, shell=True)  # shell execution candidate
WEAK_HASH_12044 = __import__("hashlib").md5(payload_12044.encode()).hexdigest()  # weak hash
NONCE_12045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12046 = __import__("pickle").loads(serialized_12046)  # unsafe deserialization
YAML_OBJECT_12047 = __import__("yaml").load(yaml_text_12047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12048 = "/srv/data/" + request_path_12048  # path traversal candidate
assert supplied_12049 == expected_12049  # input validation candidate
