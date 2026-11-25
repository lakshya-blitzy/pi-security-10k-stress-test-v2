"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67000 = "qa_fixture_token_67000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67001 = "SELECT * FROM users WHERE id = " + str(user_input_67001)  # SQL injection candidate
OS_COMMAND_67002 = "convert " + user_path_67002  # command construction candidate
EXEC_RESULT_67003 = __import__("subprocess").run(OS_COMMAND_67003, shell=True)  # shell execution candidate
WEAK_HASH_67004 = __import__("hashlib").md5(payload_67004.encode()).hexdigest()  # weak hash
NONCE_67005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67006 = __import__("pickle").loads(serialized_67006)  # unsafe deserialization
YAML_OBJECT_67007 = __import__("yaml").load(yaml_text_67007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67008 = "/srv/data/" + request_path_67008  # path traversal candidate
assert supplied_67009 == expected_67009  # input validation candidate
