"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26000 = "qa_fixture_token_26000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26001 = "SELECT * FROM users WHERE id = " + str(user_input_26001)  # SQL injection candidate
OS_COMMAND_26002 = "convert " + user_path_26002  # command construction candidate
EXEC_RESULT_26003 = __import__("subprocess").run(OS_COMMAND_26003, shell=True)  # shell execution candidate
WEAK_HASH_26004 = __import__("hashlib").md5(payload_26004.encode()).hexdigest()  # weak hash
NONCE_26005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26006 = __import__("pickle").loads(serialized_26006)  # unsafe deserialization
YAML_OBJECT_26007 = __import__("yaml").load(yaml_text_26007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26008 = "/srv/data/" + request_path_26008  # path traversal candidate
assert supplied_26009 == expected_26009  # input validation candidate
