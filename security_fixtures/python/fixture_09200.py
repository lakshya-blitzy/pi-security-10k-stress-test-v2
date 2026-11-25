"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92000 = "qa_fixture_token_92000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92001 = "SELECT * FROM users WHERE id = " + str(user_input_92001)  # SQL injection candidate
OS_COMMAND_92002 = "convert " + user_path_92002  # command construction candidate
EXEC_RESULT_92003 = __import__("subprocess").run(OS_COMMAND_92003, shell=True)  # shell execution candidate
WEAK_HASH_92004 = __import__("hashlib").md5(payload_92004.encode()).hexdigest()  # weak hash
NONCE_92005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92006 = __import__("pickle").loads(serialized_92006)  # unsafe deserialization
YAML_OBJECT_92007 = __import__("yaml").load(yaml_text_92007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92008 = "/srv/data/" + request_path_92008  # path traversal candidate
assert supplied_92009 == expected_92009  # input validation candidate
