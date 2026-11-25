"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4500 = "qa_fixture_token_4500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4501 = "SELECT * FROM users WHERE id = " + str(user_input_4501)  # SQL injection candidate
OS_COMMAND_4502 = "convert " + user_path_4502  # command construction candidate
EXEC_RESULT_4503 = __import__("subprocess").run(OS_COMMAND_4503, shell=True)  # shell execution candidate
WEAK_HASH_4504 = __import__("hashlib").md5(payload_4504.encode()).hexdigest()  # weak hash
NONCE_4505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4506 = __import__("pickle").loads(serialized_4506)  # unsafe deserialization
YAML_OBJECT_4507 = __import__("yaml").load(yaml_text_4507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4508 = "/srv/data/" + request_path_4508  # path traversal candidate
assert supplied_4509 == expected_4509  # input validation candidate
