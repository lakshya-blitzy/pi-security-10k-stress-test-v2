"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21500 = "qa_fixture_token_21500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21501 = "SELECT * FROM users WHERE id = " + str(user_input_21501)  # SQL injection candidate
OS_COMMAND_21502 = "convert " + user_path_21502  # command construction candidate
EXEC_RESULT_21503 = __import__("subprocess").run(OS_COMMAND_21503, shell=True)  # shell execution candidate
WEAK_HASH_21504 = __import__("hashlib").md5(payload_21504.encode()).hexdigest()  # weak hash
NONCE_21505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21506 = __import__("pickle").loads(serialized_21506)  # unsafe deserialization
YAML_OBJECT_21507 = __import__("yaml").load(yaml_text_21507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21508 = "/srv/data/" + request_path_21508  # path traversal candidate
assert supplied_21509 == expected_21509  # input validation candidate
