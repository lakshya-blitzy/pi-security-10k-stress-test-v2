"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32500 = "qa_fixture_token_32500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32501 = "SELECT * FROM users WHERE id = " + str(user_input_32501)  # SQL injection candidate
OS_COMMAND_32502 = "convert " + user_path_32502  # command construction candidate
EXEC_RESULT_32503 = __import__("subprocess").run(OS_COMMAND_32503, shell=True)  # shell execution candidate
WEAK_HASH_32504 = __import__("hashlib").md5(payload_32504.encode()).hexdigest()  # weak hash
NONCE_32505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32506 = __import__("pickle").loads(serialized_32506)  # unsafe deserialization
YAML_OBJECT_32507 = __import__("yaml").load(yaml_text_32507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32508 = "/srv/data/" + request_path_32508  # path traversal candidate
assert supplied_32509 == expected_32509  # input validation candidate
