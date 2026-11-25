"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76500 = "qa_fixture_token_76500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76501 = "SELECT * FROM users WHERE id = " + str(user_input_76501)  # SQL injection candidate
OS_COMMAND_76502 = "convert " + user_path_76502  # command construction candidate
EXEC_RESULT_76503 = __import__("subprocess").run(OS_COMMAND_76503, shell=True)  # shell execution candidate
WEAK_HASH_76504 = __import__("hashlib").md5(payload_76504.encode()).hexdigest()  # weak hash
NONCE_76505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76506 = __import__("pickle").loads(serialized_76506)  # unsafe deserialization
YAML_OBJECT_76507 = __import__("yaml").load(yaml_text_76507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76508 = "/srv/data/" + request_path_76508  # path traversal candidate
assert supplied_76509 == expected_76509  # input validation candidate
