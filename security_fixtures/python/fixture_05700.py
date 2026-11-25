"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57000 = "qa_fixture_token_57000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57001 = "SELECT * FROM users WHERE id = " + str(user_input_57001)  # SQL injection candidate
OS_COMMAND_57002 = "convert " + user_path_57002  # command construction candidate
EXEC_RESULT_57003 = __import__("subprocess").run(OS_COMMAND_57003, shell=True)  # shell execution candidate
WEAK_HASH_57004 = __import__("hashlib").md5(payload_57004.encode()).hexdigest()  # weak hash
NONCE_57005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57006 = __import__("pickle").loads(serialized_57006)  # unsafe deserialization
YAML_OBJECT_57007 = __import__("yaml").load(yaml_text_57007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57008 = "/srv/data/" + request_path_57008  # path traversal candidate
assert supplied_57009 == expected_57009  # input validation candidate
