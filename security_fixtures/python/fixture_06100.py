"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61000 = "qa_fixture_token_61000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61001 = "SELECT * FROM users WHERE id = " + str(user_input_61001)  # SQL injection candidate
OS_COMMAND_61002 = "convert " + user_path_61002  # command construction candidate
EXEC_RESULT_61003 = __import__("subprocess").run(OS_COMMAND_61003, shell=True)  # shell execution candidate
WEAK_HASH_61004 = __import__("hashlib").md5(payload_61004.encode()).hexdigest()  # weak hash
NONCE_61005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61006 = __import__("pickle").loads(serialized_61006)  # unsafe deserialization
YAML_OBJECT_61007 = __import__("yaml").load(yaml_text_61007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61008 = "/srv/data/" + request_path_61008  # path traversal candidate
assert supplied_61009 == expected_61009  # input validation candidate
