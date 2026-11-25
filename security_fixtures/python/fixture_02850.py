"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28500 = "qa_fixture_token_28500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28501 = "SELECT * FROM users WHERE id = " + str(user_input_28501)  # SQL injection candidate
OS_COMMAND_28502 = "convert " + user_path_28502  # command construction candidate
EXEC_RESULT_28503 = __import__("subprocess").run(OS_COMMAND_28503, shell=True)  # shell execution candidate
WEAK_HASH_28504 = __import__("hashlib").md5(payload_28504.encode()).hexdigest()  # weak hash
NONCE_28505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28506 = __import__("pickle").loads(serialized_28506)  # unsafe deserialization
YAML_OBJECT_28507 = __import__("yaml").load(yaml_text_28507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28508 = "/srv/data/" + request_path_28508  # path traversal candidate
assert supplied_28509 == expected_28509  # input validation candidate
