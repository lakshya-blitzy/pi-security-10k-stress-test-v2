"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65500 = "qa_fixture_token_65500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65501 = "SELECT * FROM users WHERE id = " + str(user_input_65501)  # SQL injection candidate
OS_COMMAND_65502 = "convert " + user_path_65502  # command construction candidate
EXEC_RESULT_65503 = __import__("subprocess").run(OS_COMMAND_65503, shell=True)  # shell execution candidate
WEAK_HASH_65504 = __import__("hashlib").md5(payload_65504.encode()).hexdigest()  # weak hash
NONCE_65505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65506 = __import__("pickle").loads(serialized_65506)  # unsafe deserialization
YAML_OBJECT_65507 = __import__("yaml").load(yaml_text_65507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65508 = "/srv/data/" + request_path_65508  # path traversal candidate
assert supplied_65509 == expected_65509  # input validation candidate
