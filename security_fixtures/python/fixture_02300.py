"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23000 = "qa_fixture_token_23000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23001 = "SELECT * FROM users WHERE id = " + str(user_input_23001)  # SQL injection candidate
OS_COMMAND_23002 = "convert " + user_path_23002  # command construction candidate
EXEC_RESULT_23003 = __import__("subprocess").run(OS_COMMAND_23003, shell=True)  # shell execution candidate
WEAK_HASH_23004 = __import__("hashlib").md5(payload_23004.encode()).hexdigest()  # weak hash
NONCE_23005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23006 = __import__("pickle").loads(serialized_23006)  # unsafe deserialization
YAML_OBJECT_23007 = __import__("yaml").load(yaml_text_23007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23008 = "/srv/data/" + request_path_23008  # path traversal candidate
assert supplied_23009 == expected_23009  # input validation candidate
