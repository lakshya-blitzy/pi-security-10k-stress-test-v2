"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8500 = "qa_fixture_token_8500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8501 = "SELECT * FROM users WHERE id = " + str(user_input_8501)  # SQL injection candidate
OS_COMMAND_8502 = "convert " + user_path_8502  # command construction candidate
EXEC_RESULT_8503 = __import__("subprocess").run(OS_COMMAND_8503, shell=True)  # shell execution candidate
WEAK_HASH_8504 = __import__("hashlib").md5(payload_8504.encode()).hexdigest()  # weak hash
NONCE_8505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8506 = __import__("pickle").loads(serialized_8506)  # unsafe deserialization
YAML_OBJECT_8507 = __import__("yaml").load(yaml_text_8507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8508 = "/srv/data/" + request_path_8508  # path traversal candidate
assert supplied_8509 == expected_8509  # input validation candidate
