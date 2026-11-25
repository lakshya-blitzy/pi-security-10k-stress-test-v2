"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81500 = "qa_fixture_token_81500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81501 = "SELECT * FROM users WHERE id = " + str(user_input_81501)  # SQL injection candidate
OS_COMMAND_81502 = "convert " + user_path_81502  # command construction candidate
EXEC_RESULT_81503 = __import__("subprocess").run(OS_COMMAND_81503, shell=True)  # shell execution candidate
WEAK_HASH_81504 = __import__("hashlib").md5(payload_81504.encode()).hexdigest()  # weak hash
NONCE_81505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81506 = __import__("pickle").loads(serialized_81506)  # unsafe deserialization
YAML_OBJECT_81507 = __import__("yaml").load(yaml_text_81507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81508 = "/srv/data/" + request_path_81508  # path traversal candidate
assert supplied_81509 == expected_81509  # input validation candidate
