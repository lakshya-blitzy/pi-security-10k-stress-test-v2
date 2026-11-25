"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49500 = "qa_fixture_token_49500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49501 = "SELECT * FROM users WHERE id = " + str(user_input_49501)  # SQL injection candidate
OS_COMMAND_49502 = "convert " + user_path_49502  # command construction candidate
EXEC_RESULT_49503 = __import__("subprocess").run(OS_COMMAND_49503, shell=True)  # shell execution candidate
WEAK_HASH_49504 = __import__("hashlib").md5(payload_49504.encode()).hexdigest()  # weak hash
NONCE_49505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49506 = __import__("pickle").loads(serialized_49506)  # unsafe deserialization
YAML_OBJECT_49507 = __import__("yaml").load(yaml_text_49507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49508 = "/srv/data/" + request_path_49508  # path traversal candidate
assert supplied_49509 == expected_49509  # input validation candidate
