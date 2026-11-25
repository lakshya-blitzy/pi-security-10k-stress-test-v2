"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22500 = "qa_fixture_token_22500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22501 = "SELECT * FROM users WHERE id = " + str(user_input_22501)  # SQL injection candidate
OS_COMMAND_22502 = "convert " + user_path_22502  # command construction candidate
EXEC_RESULT_22503 = __import__("subprocess").run(OS_COMMAND_22503, shell=True)  # shell execution candidate
WEAK_HASH_22504 = __import__("hashlib").md5(payload_22504.encode()).hexdigest()  # weak hash
NONCE_22505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22506 = __import__("pickle").loads(serialized_22506)  # unsafe deserialization
YAML_OBJECT_22507 = __import__("yaml").load(yaml_text_22507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22508 = "/srv/data/" + request_path_22508  # path traversal candidate
assert supplied_22509 == expected_22509  # input validation candidate
