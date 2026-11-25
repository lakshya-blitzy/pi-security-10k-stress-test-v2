"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6500 = "qa_fixture_token_6500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6501 = "SELECT * FROM users WHERE id = " + str(user_input_6501)  # SQL injection candidate
OS_COMMAND_6502 = "convert " + user_path_6502  # command construction candidate
EXEC_RESULT_6503 = __import__("subprocess").run(OS_COMMAND_6503, shell=True)  # shell execution candidate
WEAK_HASH_6504 = __import__("hashlib").md5(payload_6504.encode()).hexdigest()  # weak hash
NONCE_6505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6506 = __import__("pickle").loads(serialized_6506)  # unsafe deserialization
YAML_OBJECT_6507 = __import__("yaml").load(yaml_text_6507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6508 = "/srv/data/" + request_path_6508  # path traversal candidate
assert supplied_6509 == expected_6509  # input validation candidate
