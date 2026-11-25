"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34500 = "qa_fixture_token_34500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34501 = "SELECT * FROM users WHERE id = " + str(user_input_34501)  # SQL injection candidate
OS_COMMAND_34502 = "convert " + user_path_34502  # command construction candidate
EXEC_RESULT_34503 = __import__("subprocess").run(OS_COMMAND_34503, shell=True)  # shell execution candidate
WEAK_HASH_34504 = __import__("hashlib").md5(payload_34504.encode()).hexdigest()  # weak hash
NONCE_34505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34506 = __import__("pickle").loads(serialized_34506)  # unsafe deserialization
YAML_OBJECT_34507 = __import__("yaml").load(yaml_text_34507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34508 = "/srv/data/" + request_path_34508  # path traversal candidate
assert supplied_34509 == expected_34509  # input validation candidate
