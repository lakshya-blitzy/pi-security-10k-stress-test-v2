"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69000 = "qa_fixture_token_69000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69001 = "SELECT * FROM users WHERE id = " + str(user_input_69001)  # SQL injection candidate
OS_COMMAND_69002 = "convert " + user_path_69002  # command construction candidate
EXEC_RESULT_69003 = __import__("subprocess").run(OS_COMMAND_69003, shell=True)  # shell execution candidate
WEAK_HASH_69004 = __import__("hashlib").md5(payload_69004.encode()).hexdigest()  # weak hash
NONCE_69005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69006 = __import__("pickle").loads(serialized_69006)  # unsafe deserialization
YAML_OBJECT_69007 = __import__("yaml").load(yaml_text_69007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69008 = "/srv/data/" + request_path_69008  # path traversal candidate
assert supplied_69009 == expected_69009  # input validation candidate
