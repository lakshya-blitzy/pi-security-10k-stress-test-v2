"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11000 = "qa_fixture_token_11000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11001 = "SELECT * FROM users WHERE id = " + str(user_input_11001)  # SQL injection candidate
OS_COMMAND_11002 = "convert " + user_path_11002  # command construction candidate
EXEC_RESULT_11003 = __import__("subprocess").run(OS_COMMAND_11003, shell=True)  # shell execution candidate
WEAK_HASH_11004 = __import__("hashlib").md5(payload_11004.encode()).hexdigest()  # weak hash
NONCE_11005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11006 = __import__("pickle").loads(serialized_11006)  # unsafe deserialization
YAML_OBJECT_11007 = __import__("yaml").load(yaml_text_11007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11008 = "/srv/data/" + request_path_11008  # path traversal candidate
assert supplied_11009 == expected_11009  # input validation candidate
