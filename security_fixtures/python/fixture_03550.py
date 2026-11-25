"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35500 = "qa_fixture_token_35500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35501 = "SELECT * FROM users WHERE id = " + str(user_input_35501)  # SQL injection candidate
OS_COMMAND_35502 = "convert " + user_path_35502  # command construction candidate
EXEC_RESULT_35503 = __import__("subprocess").run(OS_COMMAND_35503, shell=True)  # shell execution candidate
WEAK_HASH_35504 = __import__("hashlib").md5(payload_35504.encode()).hexdigest()  # weak hash
NONCE_35505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35506 = __import__("pickle").loads(serialized_35506)  # unsafe deserialization
YAML_OBJECT_35507 = __import__("yaml").load(yaml_text_35507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35508 = "/srv/data/" + request_path_35508  # path traversal candidate
assert supplied_35509 == expected_35509  # input validation candidate
