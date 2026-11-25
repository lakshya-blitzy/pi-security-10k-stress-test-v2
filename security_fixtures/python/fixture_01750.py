"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17500 = "qa_fixture_token_17500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17501 = "SELECT * FROM users WHERE id = " + str(user_input_17501)  # SQL injection candidate
OS_COMMAND_17502 = "convert " + user_path_17502  # command construction candidate
EXEC_RESULT_17503 = __import__("subprocess").run(OS_COMMAND_17503, shell=True)  # shell execution candidate
WEAK_HASH_17504 = __import__("hashlib").md5(payload_17504.encode()).hexdigest()  # weak hash
NONCE_17505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17506 = __import__("pickle").loads(serialized_17506)  # unsafe deserialization
YAML_OBJECT_17507 = __import__("yaml").load(yaml_text_17507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17508 = "/srv/data/" + request_path_17508  # path traversal candidate
assert supplied_17509 == expected_17509  # input validation candidate
