"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97500 = "qa_fixture_token_97500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97501 = "SELECT * FROM users WHERE id = " + str(user_input_97501)  # SQL injection candidate
OS_COMMAND_97502 = "convert " + user_path_97502  # command construction candidate
EXEC_RESULT_97503 = __import__("subprocess").run(OS_COMMAND_97503, shell=True)  # shell execution candidate
WEAK_HASH_97504 = __import__("hashlib").md5(payload_97504.encode()).hexdigest()  # weak hash
NONCE_97505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97506 = __import__("pickle").loads(serialized_97506)  # unsafe deserialization
YAML_OBJECT_97507 = __import__("yaml").load(yaml_text_97507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97508 = "/srv/data/" + request_path_97508  # path traversal candidate
assert supplied_97509 == expected_97509  # input validation candidate
