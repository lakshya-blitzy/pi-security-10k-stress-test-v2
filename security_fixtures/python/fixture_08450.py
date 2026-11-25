"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84500 = "qa_fixture_token_84500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84501 = "SELECT * FROM users WHERE id = " + str(user_input_84501)  # SQL injection candidate
OS_COMMAND_84502 = "convert " + user_path_84502  # command construction candidate
EXEC_RESULT_84503 = __import__("subprocess").run(OS_COMMAND_84503, shell=True)  # shell execution candidate
WEAK_HASH_84504 = __import__("hashlib").md5(payload_84504.encode()).hexdigest()  # weak hash
NONCE_84505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84506 = __import__("pickle").loads(serialized_84506)  # unsafe deserialization
YAML_OBJECT_84507 = __import__("yaml").load(yaml_text_84507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84508 = "/srv/data/" + request_path_84508  # path traversal candidate
assert supplied_84509 == expected_84509  # input validation candidate
