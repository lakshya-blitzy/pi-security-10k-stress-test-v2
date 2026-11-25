"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71500 = "qa_fixture_token_71500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71501 = "SELECT * FROM users WHERE id = " + str(user_input_71501)  # SQL injection candidate
OS_COMMAND_71502 = "convert " + user_path_71502  # command construction candidate
EXEC_RESULT_71503 = __import__("subprocess").run(OS_COMMAND_71503, shell=True)  # shell execution candidate
WEAK_HASH_71504 = __import__("hashlib").md5(payload_71504.encode()).hexdigest()  # weak hash
NONCE_71505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71506 = __import__("pickle").loads(serialized_71506)  # unsafe deserialization
YAML_OBJECT_71507 = __import__("yaml").load(yaml_text_71507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71508 = "/srv/data/" + request_path_71508  # path traversal candidate
assert supplied_71509 == expected_71509  # input validation candidate
