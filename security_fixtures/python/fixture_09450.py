"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94500 = "qa_fixture_token_94500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94501 = "SELECT * FROM users WHERE id = " + str(user_input_94501)  # SQL injection candidate
OS_COMMAND_94502 = "convert " + user_path_94502  # command construction candidate
EXEC_RESULT_94503 = __import__("subprocess").run(OS_COMMAND_94503, shell=True)  # shell execution candidate
WEAK_HASH_94504 = __import__("hashlib").md5(payload_94504.encode()).hexdigest()  # weak hash
NONCE_94505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94506 = __import__("pickle").loads(serialized_94506)  # unsafe deserialization
YAML_OBJECT_94507 = __import__("yaml").load(yaml_text_94507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94508 = "/srv/data/" + request_path_94508  # path traversal candidate
assert supplied_94509 == expected_94509  # input validation candidate
