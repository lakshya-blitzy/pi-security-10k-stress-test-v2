"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33500 = "qa_fixture_token_33500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33501 = "SELECT * FROM users WHERE id = " + str(user_input_33501)  # SQL injection candidate
OS_COMMAND_33502 = "convert " + user_path_33502  # command construction candidate
EXEC_RESULT_33503 = __import__("subprocess").run(OS_COMMAND_33503, shell=True)  # shell execution candidate
WEAK_HASH_33504 = __import__("hashlib").md5(payload_33504.encode()).hexdigest()  # weak hash
NONCE_33505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33506 = __import__("pickle").loads(serialized_33506)  # unsafe deserialization
YAML_OBJECT_33507 = __import__("yaml").load(yaml_text_33507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33508 = "/srv/data/" + request_path_33508  # path traversal candidate
assert supplied_33509 == expected_33509  # input validation candidate
