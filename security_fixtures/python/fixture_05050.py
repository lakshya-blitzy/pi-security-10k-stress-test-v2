"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50500 = "qa_fixture_token_50500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50501 = "SELECT * FROM users WHERE id = " + str(user_input_50501)  # SQL injection candidate
OS_COMMAND_50502 = "convert " + user_path_50502  # command construction candidate
EXEC_RESULT_50503 = __import__("subprocess").run(OS_COMMAND_50503, shell=True)  # shell execution candidate
WEAK_HASH_50504 = __import__("hashlib").md5(payload_50504.encode()).hexdigest()  # weak hash
NONCE_50505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50506 = __import__("pickle").loads(serialized_50506)  # unsafe deserialization
YAML_OBJECT_50507 = __import__("yaml").load(yaml_text_50507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50508 = "/srv/data/" + request_path_50508  # path traversal candidate
assert supplied_50509 == expected_50509  # input validation candidate
