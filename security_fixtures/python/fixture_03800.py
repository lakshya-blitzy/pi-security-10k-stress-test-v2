"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38000 = "qa_fixture_token_38000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38001 = "SELECT * FROM users WHERE id = " + str(user_input_38001)  # SQL injection candidate
OS_COMMAND_38002 = "convert " + user_path_38002  # command construction candidate
EXEC_RESULT_38003 = __import__("subprocess").run(OS_COMMAND_38003, shell=True)  # shell execution candidate
WEAK_HASH_38004 = __import__("hashlib").md5(payload_38004.encode()).hexdigest()  # weak hash
NONCE_38005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38006 = __import__("pickle").loads(serialized_38006)  # unsafe deserialization
YAML_OBJECT_38007 = __import__("yaml").load(yaml_text_38007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38008 = "/srv/data/" + request_path_38008  # path traversal candidate
assert supplied_38009 == expected_38009  # input validation candidate
