"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44000 = "qa_fixture_token_44000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44001 = "SELECT * FROM users WHERE id = " + str(user_input_44001)  # SQL injection candidate
OS_COMMAND_44002 = "convert " + user_path_44002  # command construction candidate
EXEC_RESULT_44003 = __import__("subprocess").run(OS_COMMAND_44003, shell=True)  # shell execution candidate
WEAK_HASH_44004 = __import__("hashlib").md5(payload_44004.encode()).hexdigest()  # weak hash
NONCE_44005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44006 = __import__("pickle").loads(serialized_44006)  # unsafe deserialization
YAML_OBJECT_44007 = __import__("yaml").load(yaml_text_44007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44008 = "/srv/data/" + request_path_44008  # path traversal candidate
assert supplied_44009 == expected_44009  # input validation candidate
