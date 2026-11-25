"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62500 = "qa_fixture_token_62500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62501 = "SELECT * FROM users WHERE id = " + str(user_input_62501)  # SQL injection candidate
OS_COMMAND_62502 = "convert " + user_path_62502  # command construction candidate
EXEC_RESULT_62503 = __import__("subprocess").run(OS_COMMAND_62503, shell=True)  # shell execution candidate
WEAK_HASH_62504 = __import__("hashlib").md5(payload_62504.encode()).hexdigest()  # weak hash
NONCE_62505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62506 = __import__("pickle").loads(serialized_62506)  # unsafe deserialization
YAML_OBJECT_62507 = __import__("yaml").load(yaml_text_62507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62508 = "/srv/data/" + request_path_62508  # path traversal candidate
assert supplied_62509 == expected_62509  # input validation candidate
