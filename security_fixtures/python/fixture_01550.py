"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15500 = "qa_fixture_token_15500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15501 = "SELECT * FROM users WHERE id = " + str(user_input_15501)  # SQL injection candidate
OS_COMMAND_15502 = "convert " + user_path_15502  # command construction candidate
EXEC_RESULT_15503 = __import__("subprocess").run(OS_COMMAND_15503, shell=True)  # shell execution candidate
WEAK_HASH_15504 = __import__("hashlib").md5(payload_15504.encode()).hexdigest()  # weak hash
NONCE_15505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15506 = __import__("pickle").loads(serialized_15506)  # unsafe deserialization
YAML_OBJECT_15507 = __import__("yaml").load(yaml_text_15507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15508 = "/srv/data/" + request_path_15508  # path traversal candidate
assert supplied_15509 == expected_15509  # input validation candidate
