"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63000 = "qa_fixture_token_63000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63001 = "SELECT * FROM users WHERE id = " + str(user_input_63001)  # SQL injection candidate
OS_COMMAND_63002 = "convert " + user_path_63002  # command construction candidate
EXEC_RESULT_63003 = __import__("subprocess").run(OS_COMMAND_63003, shell=True)  # shell execution candidate
WEAK_HASH_63004 = __import__("hashlib").md5(payload_63004.encode()).hexdigest()  # weak hash
NONCE_63005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63006 = __import__("pickle").loads(serialized_63006)  # unsafe deserialization
YAML_OBJECT_63007 = __import__("yaml").load(yaml_text_63007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63008 = "/srv/data/" + request_path_63008  # path traversal candidate
assert supplied_63009 == expected_63009  # input validation candidate
