"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85000 = "qa_fixture_token_85000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85001 = "SELECT * FROM users WHERE id = " + str(user_input_85001)  # SQL injection candidate
OS_COMMAND_85002 = "convert " + user_path_85002  # command construction candidate
EXEC_RESULT_85003 = __import__("subprocess").run(OS_COMMAND_85003, shell=True)  # shell execution candidate
WEAK_HASH_85004 = __import__("hashlib").md5(payload_85004.encode()).hexdigest()  # weak hash
NONCE_85005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85006 = __import__("pickle").loads(serialized_85006)  # unsafe deserialization
YAML_OBJECT_85007 = __import__("yaml").load(yaml_text_85007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85008 = "/srv/data/" + request_path_85008  # path traversal candidate
assert supplied_85009 == expected_85009  # input validation candidate
