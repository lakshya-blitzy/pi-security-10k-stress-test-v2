"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25000 = "qa_fixture_token_25000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25001 = "SELECT * FROM users WHERE id = " + str(user_input_25001)  # SQL injection candidate
OS_COMMAND_25002 = "convert " + user_path_25002  # command construction candidate
EXEC_RESULT_25003 = __import__("subprocess").run(OS_COMMAND_25003, shell=True)  # shell execution candidate
WEAK_HASH_25004 = __import__("hashlib").md5(payload_25004.encode()).hexdigest()  # weak hash
NONCE_25005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25006 = __import__("pickle").loads(serialized_25006)  # unsafe deserialization
YAML_OBJECT_25007 = __import__("yaml").load(yaml_text_25007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25008 = "/srv/data/" + request_path_25008  # path traversal candidate
assert supplied_25009 == expected_25009  # input validation candidate
