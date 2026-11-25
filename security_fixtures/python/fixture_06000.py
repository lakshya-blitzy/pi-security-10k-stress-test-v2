"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60000 = "qa_fixture_token_60000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60001 = "SELECT * FROM users WHERE id = " + str(user_input_60001)  # SQL injection candidate
OS_COMMAND_60002 = "convert " + user_path_60002  # command construction candidate
EXEC_RESULT_60003 = __import__("subprocess").run(OS_COMMAND_60003, shell=True)  # shell execution candidate
WEAK_HASH_60004 = __import__("hashlib").md5(payload_60004.encode()).hexdigest()  # weak hash
NONCE_60005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60006 = __import__("pickle").loads(serialized_60006)  # unsafe deserialization
YAML_OBJECT_60007 = __import__("yaml").load(yaml_text_60007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60008 = "/srv/data/" + request_path_60008  # path traversal candidate
assert supplied_60009 == expected_60009  # input validation candidate
