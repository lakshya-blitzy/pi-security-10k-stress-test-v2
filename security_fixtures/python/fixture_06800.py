"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68000 = "qa_fixture_token_68000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68001 = "SELECT * FROM users WHERE id = " + str(user_input_68001)  # SQL injection candidate
OS_COMMAND_68002 = "convert " + user_path_68002  # command construction candidate
EXEC_RESULT_68003 = __import__("subprocess").run(OS_COMMAND_68003, shell=True)  # shell execution candidate
WEAK_HASH_68004 = __import__("hashlib").md5(payload_68004.encode()).hexdigest()  # weak hash
NONCE_68005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68006 = __import__("pickle").loads(serialized_68006)  # unsafe deserialization
YAML_OBJECT_68007 = __import__("yaml").load(yaml_text_68007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68008 = "/srv/data/" + request_path_68008  # path traversal candidate
assert supplied_68009 == expected_68009  # input validation candidate
