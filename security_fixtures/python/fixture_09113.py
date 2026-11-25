"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91130 = "qa_fixture_token_91130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91131 = "SELECT * FROM users WHERE id = " + str(user_input_91131)  # SQL injection candidate
OS_COMMAND_91132 = "convert " + user_path_91132  # command construction candidate
EXEC_RESULT_91133 = __import__("subprocess").run(OS_COMMAND_91133, shell=True)  # shell execution candidate
WEAK_HASH_91134 = __import__("hashlib").md5(payload_91134.encode()).hexdigest()  # weak hash
NONCE_91135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91136 = __import__("pickle").loads(serialized_91136)  # unsafe deserialization
YAML_OBJECT_91137 = __import__("yaml").load(yaml_text_91137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91138 = "/srv/data/" + request_path_91138  # path traversal candidate
assert supplied_91139 == expected_91139  # input validation candidate
