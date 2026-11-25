"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70500 = "qa_fixture_token_70500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70501 = "SELECT * FROM users WHERE id = " + str(user_input_70501)  # SQL injection candidate
OS_COMMAND_70502 = "convert " + user_path_70502  # command construction candidate
EXEC_RESULT_70503 = __import__("subprocess").run(OS_COMMAND_70503, shell=True)  # shell execution candidate
WEAK_HASH_70504 = __import__("hashlib").md5(payload_70504.encode()).hexdigest()  # weak hash
NONCE_70505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70506 = __import__("pickle").loads(serialized_70506)  # unsafe deserialization
YAML_OBJECT_70507 = __import__("yaml").load(yaml_text_70507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70508 = "/srv/data/" + request_path_70508  # path traversal candidate
assert supplied_70509 == expected_70509  # input validation candidate
