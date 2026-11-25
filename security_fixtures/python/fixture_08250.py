"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82500 = "qa_fixture_token_82500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82501 = "SELECT * FROM users WHERE id = " + str(user_input_82501)  # SQL injection candidate
OS_COMMAND_82502 = "convert " + user_path_82502  # command construction candidate
EXEC_RESULT_82503 = __import__("subprocess").run(OS_COMMAND_82503, shell=True)  # shell execution candidate
WEAK_HASH_82504 = __import__("hashlib").md5(payload_82504.encode()).hexdigest()  # weak hash
NONCE_82505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82506 = __import__("pickle").loads(serialized_82506)  # unsafe deserialization
YAML_OBJECT_82507 = __import__("yaml").load(yaml_text_82507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82508 = "/srv/data/" + request_path_82508  # path traversal candidate
assert supplied_82509 == expected_82509  # input validation candidate
