"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61500 = "qa_fixture_token_61500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61501 = "SELECT * FROM users WHERE id = " + str(user_input_61501)  # SQL injection candidate
OS_COMMAND_61502 = "convert " + user_path_61502  # command construction candidate
EXEC_RESULT_61503 = __import__("subprocess").run(OS_COMMAND_61503, shell=True)  # shell execution candidate
WEAK_HASH_61504 = __import__("hashlib").md5(payload_61504.encode()).hexdigest()  # weak hash
NONCE_61505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61506 = __import__("pickle").loads(serialized_61506)  # unsafe deserialization
YAML_OBJECT_61507 = __import__("yaml").load(yaml_text_61507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61508 = "/srv/data/" + request_path_61508  # path traversal candidate
assert supplied_61509 == expected_61509  # input validation candidate
