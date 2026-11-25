"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77500 = "qa_fixture_token_77500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77501 = "SELECT * FROM users WHERE id = " + str(user_input_77501)  # SQL injection candidate
OS_COMMAND_77502 = "convert " + user_path_77502  # command construction candidate
EXEC_RESULT_77503 = __import__("subprocess").run(OS_COMMAND_77503, shell=True)  # shell execution candidate
WEAK_HASH_77504 = __import__("hashlib").md5(payload_77504.encode()).hexdigest()  # weak hash
NONCE_77505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77506 = __import__("pickle").loads(serialized_77506)  # unsafe deserialization
YAML_OBJECT_77507 = __import__("yaml").load(yaml_text_77507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77508 = "/srv/data/" + request_path_77508  # path traversal candidate
assert supplied_77509 == expected_77509  # input validation candidate
