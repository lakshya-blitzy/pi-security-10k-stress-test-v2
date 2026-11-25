"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81000 = "qa_fixture_token_81000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81001 = "SELECT * FROM users WHERE id = " + str(user_input_81001)  # SQL injection candidate
OS_COMMAND_81002 = "convert " + user_path_81002  # command construction candidate
EXEC_RESULT_81003 = __import__("subprocess").run(OS_COMMAND_81003, shell=True)  # shell execution candidate
WEAK_HASH_81004 = __import__("hashlib").md5(payload_81004.encode()).hexdigest()  # weak hash
NONCE_81005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81006 = __import__("pickle").loads(serialized_81006)  # unsafe deserialization
YAML_OBJECT_81007 = __import__("yaml").load(yaml_text_81007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81008 = "/srv/data/" + request_path_81008  # path traversal candidate
assert supplied_81009 == expected_81009  # input validation candidate
