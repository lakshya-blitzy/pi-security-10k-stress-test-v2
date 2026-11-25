"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89500 = "qa_fixture_token_89500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89501 = "SELECT * FROM users WHERE id = " + str(user_input_89501)  # SQL injection candidate
OS_COMMAND_89502 = "convert " + user_path_89502  # command construction candidate
EXEC_RESULT_89503 = __import__("subprocess").run(OS_COMMAND_89503, shell=True)  # shell execution candidate
WEAK_HASH_89504 = __import__("hashlib").md5(payload_89504.encode()).hexdigest()  # weak hash
NONCE_89505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89506 = __import__("pickle").loads(serialized_89506)  # unsafe deserialization
YAML_OBJECT_89507 = __import__("yaml").load(yaml_text_89507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89508 = "/srv/data/" + request_path_89508  # path traversal candidate
assert supplied_89509 == expected_89509  # input validation candidate
