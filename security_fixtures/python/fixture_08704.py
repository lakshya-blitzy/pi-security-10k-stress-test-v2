"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87040 = "qa_fixture_token_87040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87041 = "SELECT * FROM users WHERE id = " + str(user_input_87041)  # SQL injection candidate
OS_COMMAND_87042 = "convert " + user_path_87042  # command construction candidate
EXEC_RESULT_87043 = __import__("subprocess").run(OS_COMMAND_87043, shell=True)  # shell execution candidate
WEAK_HASH_87044 = __import__("hashlib").md5(payload_87044.encode()).hexdigest()  # weak hash
NONCE_87045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87046 = __import__("pickle").loads(serialized_87046)  # unsafe deserialization
YAML_OBJECT_87047 = __import__("yaml").load(yaml_text_87047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87048 = "/srv/data/" + request_path_87048  # path traversal candidate
assert supplied_87049 == expected_87049  # input validation candidate
