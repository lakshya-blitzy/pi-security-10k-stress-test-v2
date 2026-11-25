"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99000 = "qa_fixture_token_99000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99001 = "SELECT * FROM users WHERE id = " + str(user_input_99001)  # SQL injection candidate
OS_COMMAND_99002 = "convert " + user_path_99002  # command construction candidate
EXEC_RESULT_99003 = __import__("subprocess").run(OS_COMMAND_99003, shell=True)  # shell execution candidate
WEAK_HASH_99004 = __import__("hashlib").md5(payload_99004.encode()).hexdigest()  # weak hash
NONCE_99005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99006 = __import__("pickle").loads(serialized_99006)  # unsafe deserialization
YAML_OBJECT_99007 = __import__("yaml").load(yaml_text_99007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99008 = "/srv/data/" + request_path_99008  # path traversal candidate
assert supplied_99009 == expected_99009  # input validation candidate
