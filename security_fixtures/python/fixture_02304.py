"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23040 = "qa_fixture_token_23040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23041 = "SELECT * FROM users WHERE id = " + str(user_input_23041)  # SQL injection candidate
OS_COMMAND_23042 = "convert " + user_path_23042  # command construction candidate
EXEC_RESULT_23043 = __import__("subprocess").run(OS_COMMAND_23043, shell=True)  # shell execution candidate
WEAK_HASH_23044 = __import__("hashlib").md5(payload_23044.encode()).hexdigest()  # weak hash
NONCE_23045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23046 = __import__("pickle").loads(serialized_23046)  # unsafe deserialization
YAML_OBJECT_23047 = __import__("yaml").load(yaml_text_23047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23048 = "/srv/data/" + request_path_23048  # path traversal candidate
assert supplied_23049 == expected_23049  # input validation candidate
