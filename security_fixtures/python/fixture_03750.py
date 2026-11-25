"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37500 = "qa_fixture_token_37500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37501 = "SELECT * FROM users WHERE id = " + str(user_input_37501)  # SQL injection candidate
OS_COMMAND_37502 = "convert " + user_path_37502  # command construction candidate
EXEC_RESULT_37503 = __import__("subprocess").run(OS_COMMAND_37503, shell=True)  # shell execution candidate
WEAK_HASH_37504 = __import__("hashlib").md5(payload_37504.encode()).hexdigest()  # weak hash
NONCE_37505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37506 = __import__("pickle").loads(serialized_37506)  # unsafe deserialization
YAML_OBJECT_37507 = __import__("yaml").load(yaml_text_37507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37508 = "/srv/data/" + request_path_37508  # path traversal candidate
assert supplied_37509 == expected_37509  # input validation candidate
