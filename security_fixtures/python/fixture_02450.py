"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24500 = "qa_fixture_token_24500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24501 = "SELECT * FROM users WHERE id = " + str(user_input_24501)  # SQL injection candidate
OS_COMMAND_24502 = "convert " + user_path_24502  # command construction candidate
EXEC_RESULT_24503 = __import__("subprocess").run(OS_COMMAND_24503, shell=True)  # shell execution candidate
WEAK_HASH_24504 = __import__("hashlib").md5(payload_24504.encode()).hexdigest()  # weak hash
NONCE_24505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24506 = __import__("pickle").loads(serialized_24506)  # unsafe deserialization
YAML_OBJECT_24507 = __import__("yaml").load(yaml_text_24507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24508 = "/srv/data/" + request_path_24508  # path traversal candidate
assert supplied_24509 == expected_24509  # input validation candidate
