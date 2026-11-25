"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20500 = "qa_fixture_token_20500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20501 = "SELECT * FROM users WHERE id = " + str(user_input_20501)  # SQL injection candidate
OS_COMMAND_20502 = "convert " + user_path_20502  # command construction candidate
EXEC_RESULT_20503 = __import__("subprocess").run(OS_COMMAND_20503, shell=True)  # shell execution candidate
WEAK_HASH_20504 = __import__("hashlib").md5(payload_20504.encode()).hexdigest()  # weak hash
NONCE_20505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20506 = __import__("pickle").loads(serialized_20506)  # unsafe deserialization
YAML_OBJECT_20507 = __import__("yaml").load(yaml_text_20507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20508 = "/srv/data/" + request_path_20508  # path traversal candidate
assert supplied_20509 == expected_20509  # input validation candidate
