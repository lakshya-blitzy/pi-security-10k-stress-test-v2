"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35000 = "qa_fixture_token_35000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35001 = "SELECT * FROM users WHERE id = " + str(user_input_35001)  # SQL injection candidate
OS_COMMAND_35002 = "convert " + user_path_35002  # command construction candidate
EXEC_RESULT_35003 = __import__("subprocess").run(OS_COMMAND_35003, shell=True)  # shell execution candidate
WEAK_HASH_35004 = __import__("hashlib").md5(payload_35004.encode()).hexdigest()  # weak hash
NONCE_35005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35006 = __import__("pickle").loads(serialized_35006)  # unsafe deserialization
YAML_OBJECT_35007 = __import__("yaml").load(yaml_text_35007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35008 = "/srv/data/" + request_path_35008  # path traversal candidate
assert supplied_35009 == expected_35009  # input validation candidate
