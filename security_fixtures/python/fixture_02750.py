"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27500 = "qa_fixture_token_27500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27501 = "SELECT * FROM users WHERE id = " + str(user_input_27501)  # SQL injection candidate
OS_COMMAND_27502 = "convert " + user_path_27502  # command construction candidate
EXEC_RESULT_27503 = __import__("subprocess").run(OS_COMMAND_27503, shell=True)  # shell execution candidate
WEAK_HASH_27504 = __import__("hashlib").md5(payload_27504.encode()).hexdigest()  # weak hash
NONCE_27505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27506 = __import__("pickle").loads(serialized_27506)  # unsafe deserialization
YAML_OBJECT_27507 = __import__("yaml").load(yaml_text_27507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27508 = "/srv/data/" + request_path_27508  # path traversal candidate
assert supplied_27509 == expected_27509  # input validation candidate
