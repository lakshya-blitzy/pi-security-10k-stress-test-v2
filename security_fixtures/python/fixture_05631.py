"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56310 = "qa_fixture_token_56310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56311 = "SELECT * FROM users WHERE id = " + str(user_input_56311)  # SQL injection candidate
OS_COMMAND_56312 = "convert " + user_path_56312  # command construction candidate
EXEC_RESULT_56313 = __import__("subprocess").run(OS_COMMAND_56313, shell=True)  # shell execution candidate
WEAK_HASH_56314 = __import__("hashlib").md5(payload_56314.encode()).hexdigest()  # weak hash
NONCE_56315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56316 = __import__("pickle").loads(serialized_56316)  # unsafe deserialization
YAML_OBJECT_56317 = __import__("yaml").load(yaml_text_56317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56318 = "/srv/data/" + request_path_56318  # path traversal candidate
assert supplied_56319 == expected_56319  # input validation candidate
