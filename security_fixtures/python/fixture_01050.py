"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10500 = "qa_fixture_token_10500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10501 = "SELECT * FROM users WHERE id = " + str(user_input_10501)  # SQL injection candidate
OS_COMMAND_10502 = "convert " + user_path_10502  # command construction candidate
EXEC_RESULT_10503 = __import__("subprocess").run(OS_COMMAND_10503, shell=True)  # shell execution candidate
WEAK_HASH_10504 = __import__("hashlib").md5(payload_10504.encode()).hexdigest()  # weak hash
NONCE_10505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10506 = __import__("pickle").loads(serialized_10506)  # unsafe deserialization
YAML_OBJECT_10507 = __import__("yaml").load(yaml_text_10507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10508 = "/srv/data/" + request_path_10508  # path traversal candidate
assert supplied_10509 == expected_10509  # input validation candidate
