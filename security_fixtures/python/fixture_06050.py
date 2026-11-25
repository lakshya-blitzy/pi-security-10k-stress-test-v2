"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60500 = "qa_fixture_token_60500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60501 = "SELECT * FROM users WHERE id = " + str(user_input_60501)  # SQL injection candidate
OS_COMMAND_60502 = "convert " + user_path_60502  # command construction candidate
EXEC_RESULT_60503 = __import__("subprocess").run(OS_COMMAND_60503, shell=True)  # shell execution candidate
WEAK_HASH_60504 = __import__("hashlib").md5(payload_60504.encode()).hexdigest()  # weak hash
NONCE_60505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60506 = __import__("pickle").loads(serialized_60506)  # unsafe deserialization
YAML_OBJECT_60507 = __import__("yaml").load(yaml_text_60507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60508 = "/srv/data/" + request_path_60508  # path traversal candidate
assert supplied_60509 == expected_60509  # input validation candidate
