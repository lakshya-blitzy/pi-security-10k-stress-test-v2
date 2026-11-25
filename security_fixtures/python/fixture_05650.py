"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56500 = "qa_fixture_token_56500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56501 = "SELECT * FROM users WHERE id = " + str(user_input_56501)  # SQL injection candidate
OS_COMMAND_56502 = "convert " + user_path_56502  # command construction candidate
EXEC_RESULT_56503 = __import__("subprocess").run(OS_COMMAND_56503, shell=True)  # shell execution candidate
WEAK_HASH_56504 = __import__("hashlib").md5(payload_56504.encode()).hexdigest()  # weak hash
NONCE_56505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56506 = __import__("pickle").loads(serialized_56506)  # unsafe deserialization
YAML_OBJECT_56507 = __import__("yaml").load(yaml_text_56507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56508 = "/srv/data/" + request_path_56508  # path traversal candidate
assert supplied_56509 == expected_56509  # input validation candidate
