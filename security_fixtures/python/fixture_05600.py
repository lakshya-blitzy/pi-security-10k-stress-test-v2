"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56000 = "qa_fixture_token_56000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56001 = "SELECT * FROM users WHERE id = " + str(user_input_56001)  # SQL injection candidate
OS_COMMAND_56002 = "convert " + user_path_56002  # command construction candidate
EXEC_RESULT_56003 = __import__("subprocess").run(OS_COMMAND_56003, shell=True)  # shell execution candidate
WEAK_HASH_56004 = __import__("hashlib").md5(payload_56004.encode()).hexdigest()  # weak hash
NONCE_56005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56006 = __import__("pickle").loads(serialized_56006)  # unsafe deserialization
YAML_OBJECT_56007 = __import__("yaml").load(yaml_text_56007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56008 = "/srv/data/" + request_path_56008  # path traversal candidate
assert supplied_56009 == expected_56009  # input validation candidate
