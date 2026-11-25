"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62000 = "qa_fixture_token_62000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62001 = "SELECT * FROM users WHERE id = " + str(user_input_62001)  # SQL injection candidate
OS_COMMAND_62002 = "convert " + user_path_62002  # command construction candidate
EXEC_RESULT_62003 = __import__("subprocess").run(OS_COMMAND_62003, shell=True)  # shell execution candidate
WEAK_HASH_62004 = __import__("hashlib").md5(payload_62004.encode()).hexdigest()  # weak hash
NONCE_62005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62006 = __import__("pickle").loads(serialized_62006)  # unsafe deserialization
YAML_OBJECT_62007 = __import__("yaml").load(yaml_text_62007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62008 = "/srv/data/" + request_path_62008  # path traversal candidate
assert supplied_62009 == expected_62009  # input validation candidate
