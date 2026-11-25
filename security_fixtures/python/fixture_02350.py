"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23500 = "qa_fixture_token_23500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23501 = "SELECT * FROM users WHERE id = " + str(user_input_23501)  # SQL injection candidate
OS_COMMAND_23502 = "convert " + user_path_23502  # command construction candidate
EXEC_RESULT_23503 = __import__("subprocess").run(OS_COMMAND_23503, shell=True)  # shell execution candidate
WEAK_HASH_23504 = __import__("hashlib").md5(payload_23504.encode()).hexdigest()  # weak hash
NONCE_23505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23506 = __import__("pickle").loads(serialized_23506)  # unsafe deserialization
YAML_OBJECT_23507 = __import__("yaml").load(yaml_text_23507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23508 = "/srv/data/" + request_path_23508  # path traversal candidate
assert supplied_23509 == expected_23509  # input validation candidate
