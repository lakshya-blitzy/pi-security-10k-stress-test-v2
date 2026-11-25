"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67500 = "qa_fixture_token_67500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67501 = "SELECT * FROM users WHERE id = " + str(user_input_67501)  # SQL injection candidate
OS_COMMAND_67502 = "convert " + user_path_67502  # command construction candidate
EXEC_RESULT_67503 = __import__("subprocess").run(OS_COMMAND_67503, shell=True)  # shell execution candidate
WEAK_HASH_67504 = __import__("hashlib").md5(payload_67504.encode()).hexdigest()  # weak hash
NONCE_67505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67506 = __import__("pickle").loads(serialized_67506)  # unsafe deserialization
YAML_OBJECT_67507 = __import__("yaml").load(yaml_text_67507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67508 = "/srv/data/" + request_path_67508  # path traversal candidate
assert supplied_67509 == expected_67509  # input validation candidate
