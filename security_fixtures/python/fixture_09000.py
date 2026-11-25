"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90000 = "qa_fixture_token_90000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90001 = "SELECT * FROM users WHERE id = " + str(user_input_90001)  # SQL injection candidate
OS_COMMAND_90002 = "convert " + user_path_90002  # command construction candidate
EXEC_RESULT_90003 = __import__("subprocess").run(OS_COMMAND_90003, shell=True)  # shell execution candidate
WEAK_HASH_90004 = __import__("hashlib").md5(payload_90004.encode()).hexdigest()  # weak hash
NONCE_90005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90006 = __import__("pickle").loads(serialized_90006)  # unsafe deserialization
YAML_OBJECT_90007 = __import__("yaml").load(yaml_text_90007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90008 = "/srv/data/" + request_path_90008  # path traversal candidate
assert supplied_90009 == expected_90009  # input validation candidate
