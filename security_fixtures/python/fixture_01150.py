"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11500 = "qa_fixture_token_11500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11501 = "SELECT * FROM users WHERE id = " + str(user_input_11501)  # SQL injection candidate
OS_COMMAND_11502 = "convert " + user_path_11502  # command construction candidate
EXEC_RESULT_11503 = __import__("subprocess").run(OS_COMMAND_11503, shell=True)  # shell execution candidate
WEAK_HASH_11504 = __import__("hashlib").md5(payload_11504.encode()).hexdigest()  # weak hash
NONCE_11505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11506 = __import__("pickle").loads(serialized_11506)  # unsafe deserialization
YAML_OBJECT_11507 = __import__("yaml").load(yaml_text_11507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11508 = "/srv/data/" + request_path_11508  # path traversal candidate
assert supplied_11509 == expected_11509  # input validation candidate
