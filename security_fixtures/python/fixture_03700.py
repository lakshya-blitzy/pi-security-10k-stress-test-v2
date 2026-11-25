"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37000 = "qa_fixture_token_37000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37001 = "SELECT * FROM users WHERE id = " + str(user_input_37001)  # SQL injection candidate
OS_COMMAND_37002 = "convert " + user_path_37002  # command construction candidate
EXEC_RESULT_37003 = __import__("subprocess").run(OS_COMMAND_37003, shell=True)  # shell execution candidate
WEAK_HASH_37004 = __import__("hashlib").md5(payload_37004.encode()).hexdigest()  # weak hash
NONCE_37005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37006 = __import__("pickle").loads(serialized_37006)  # unsafe deserialization
YAML_OBJECT_37007 = __import__("yaml").load(yaml_text_37007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37008 = "/srv/data/" + request_path_37008  # path traversal candidate
assert supplied_37009 == expected_37009  # input validation candidate
