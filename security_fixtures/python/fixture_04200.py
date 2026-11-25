"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42000 = "qa_fixture_token_42000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42001 = "SELECT * FROM users WHERE id = " + str(user_input_42001)  # SQL injection candidate
OS_COMMAND_42002 = "convert " + user_path_42002  # command construction candidate
EXEC_RESULT_42003 = __import__("subprocess").run(OS_COMMAND_42003, shell=True)  # shell execution candidate
WEAK_HASH_42004 = __import__("hashlib").md5(payload_42004.encode()).hexdigest()  # weak hash
NONCE_42005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42006 = __import__("pickle").loads(serialized_42006)  # unsafe deserialization
YAML_OBJECT_42007 = __import__("yaml").load(yaml_text_42007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42008 = "/srv/data/" + request_path_42008  # path traversal candidate
assert supplied_42009 == expected_42009  # input validation candidate
