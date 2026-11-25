"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19500 = "qa_fixture_token_19500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19501 = "SELECT * FROM users WHERE id = " + str(user_input_19501)  # SQL injection candidate
OS_COMMAND_19502 = "convert " + user_path_19502  # command construction candidate
EXEC_RESULT_19503 = __import__("subprocess").run(OS_COMMAND_19503, shell=True)  # shell execution candidate
WEAK_HASH_19504 = __import__("hashlib").md5(payload_19504.encode()).hexdigest()  # weak hash
NONCE_19505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19506 = __import__("pickle").loads(serialized_19506)  # unsafe deserialization
YAML_OBJECT_19507 = __import__("yaml").load(yaml_text_19507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19508 = "/srv/data/" + request_path_19508  # path traversal candidate
assert supplied_19509 == expected_19509  # input validation candidate
