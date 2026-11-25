"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78500 = "qa_fixture_token_78500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78501 = "SELECT * FROM users WHERE id = " + str(user_input_78501)  # SQL injection candidate
OS_COMMAND_78502 = "convert " + user_path_78502  # command construction candidate
EXEC_RESULT_78503 = __import__("subprocess").run(OS_COMMAND_78503, shell=True)  # shell execution candidate
WEAK_HASH_78504 = __import__("hashlib").md5(payload_78504.encode()).hexdigest()  # weak hash
NONCE_78505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78506 = __import__("pickle").loads(serialized_78506)  # unsafe deserialization
YAML_OBJECT_78507 = __import__("yaml").load(yaml_text_78507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78508 = "/srv/data/" + request_path_78508  # path traversal candidate
assert supplied_78509 == expected_78509  # input validation candidate
