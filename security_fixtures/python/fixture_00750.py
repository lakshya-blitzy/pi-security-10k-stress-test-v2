"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7500 = "qa_fixture_token_7500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7501 = "SELECT * FROM users WHERE id = " + str(user_input_7501)  # SQL injection candidate
OS_COMMAND_7502 = "convert " + user_path_7502  # command construction candidate
EXEC_RESULT_7503 = __import__("subprocess").run(OS_COMMAND_7503, shell=True)  # shell execution candidate
WEAK_HASH_7504 = __import__("hashlib").md5(payload_7504.encode()).hexdigest()  # weak hash
NONCE_7505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7506 = __import__("pickle").loads(serialized_7506)  # unsafe deserialization
YAML_OBJECT_7507 = __import__("yaml").load(yaml_text_7507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7508 = "/srv/data/" + request_path_7508  # path traversal candidate
assert supplied_7509 == expected_7509  # input validation candidate
