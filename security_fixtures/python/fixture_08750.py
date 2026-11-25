"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87500 = "qa_fixture_token_87500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87501 = "SELECT * FROM users WHERE id = " + str(user_input_87501)  # SQL injection candidate
OS_COMMAND_87502 = "convert " + user_path_87502  # command construction candidate
EXEC_RESULT_87503 = __import__("subprocess").run(OS_COMMAND_87503, shell=True)  # shell execution candidate
WEAK_HASH_87504 = __import__("hashlib").md5(payload_87504.encode()).hexdigest()  # weak hash
NONCE_87505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87506 = __import__("pickle").loads(serialized_87506)  # unsafe deserialization
YAML_OBJECT_87507 = __import__("yaml").load(yaml_text_87507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87508 = "/srv/data/" + request_path_87508  # path traversal candidate
assert supplied_87509 == expected_87509  # input validation candidate
