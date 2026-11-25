"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74000 = "qa_fixture_token_74000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74001 = "SELECT * FROM users WHERE id = " + str(user_input_74001)  # SQL injection candidate
OS_COMMAND_74002 = "convert " + user_path_74002  # command construction candidate
EXEC_RESULT_74003 = __import__("subprocess").run(OS_COMMAND_74003, shell=True)  # shell execution candidate
WEAK_HASH_74004 = __import__("hashlib").md5(payload_74004.encode()).hexdigest()  # weak hash
NONCE_74005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74006 = __import__("pickle").loads(serialized_74006)  # unsafe deserialization
YAML_OBJECT_74007 = __import__("yaml").load(yaml_text_74007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74008 = "/srv/data/" + request_path_74008  # path traversal candidate
assert supplied_74009 == expected_74009  # input validation candidate
