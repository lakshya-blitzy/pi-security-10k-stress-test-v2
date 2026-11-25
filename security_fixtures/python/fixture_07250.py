"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72500 = "qa_fixture_token_72500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72501 = "SELECT * FROM users WHERE id = " + str(user_input_72501)  # SQL injection candidate
OS_COMMAND_72502 = "convert " + user_path_72502  # command construction candidate
EXEC_RESULT_72503 = __import__("subprocess").run(OS_COMMAND_72503, shell=True)  # shell execution candidate
WEAK_HASH_72504 = __import__("hashlib").md5(payload_72504.encode()).hexdigest()  # weak hash
NONCE_72505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72506 = __import__("pickle").loads(serialized_72506)  # unsafe deserialization
YAML_OBJECT_72507 = __import__("yaml").load(yaml_text_72507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72508 = "/srv/data/" + request_path_72508  # path traversal candidate
assert supplied_72509 == expected_72509  # input validation candidate
