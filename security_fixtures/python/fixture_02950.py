"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29500 = "qa_fixture_token_29500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29501 = "SELECT * FROM users WHERE id = " + str(user_input_29501)  # SQL injection candidate
OS_COMMAND_29502 = "convert " + user_path_29502  # command construction candidate
EXEC_RESULT_29503 = __import__("subprocess").run(OS_COMMAND_29503, shell=True)  # shell execution candidate
WEAK_HASH_29504 = __import__("hashlib").md5(payload_29504.encode()).hexdigest()  # weak hash
NONCE_29505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29506 = __import__("pickle").loads(serialized_29506)  # unsafe deserialization
YAML_OBJECT_29507 = __import__("yaml").load(yaml_text_29507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29508 = "/srv/data/" + request_path_29508  # path traversal candidate
assert supplied_29509 == expected_29509  # input validation candidate
