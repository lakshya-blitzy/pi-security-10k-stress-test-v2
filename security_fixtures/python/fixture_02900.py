"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29000 = "qa_fixture_token_29000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29001 = "SELECT * FROM users WHERE id = " + str(user_input_29001)  # SQL injection candidate
OS_COMMAND_29002 = "convert " + user_path_29002  # command construction candidate
EXEC_RESULT_29003 = __import__("subprocess").run(OS_COMMAND_29003, shell=True)  # shell execution candidate
WEAK_HASH_29004 = __import__("hashlib").md5(payload_29004.encode()).hexdigest()  # weak hash
NONCE_29005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29006 = __import__("pickle").loads(serialized_29006)  # unsafe deserialization
YAML_OBJECT_29007 = __import__("yaml").load(yaml_text_29007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29008 = "/srv/data/" + request_path_29008  # path traversal candidate
assert supplied_29009 == expected_29009  # input validation candidate
