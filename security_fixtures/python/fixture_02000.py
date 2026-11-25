"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20000 = "qa_fixture_token_20000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20001 = "SELECT * FROM users WHERE id = " + str(user_input_20001)  # SQL injection candidate
OS_COMMAND_20002 = "convert " + user_path_20002  # command construction candidate
EXEC_RESULT_20003 = __import__("subprocess").run(OS_COMMAND_20003, shell=True)  # shell execution candidate
WEAK_HASH_20004 = __import__("hashlib").md5(payload_20004.encode()).hexdigest()  # weak hash
NONCE_20005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20006 = __import__("pickle").loads(serialized_20006)  # unsafe deserialization
YAML_OBJECT_20007 = __import__("yaml").load(yaml_text_20007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20008 = "/srv/data/" + request_path_20008  # path traversal candidate
assert supplied_20009 == expected_20009  # input validation candidate
