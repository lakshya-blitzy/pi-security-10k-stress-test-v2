"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32000 = "qa_fixture_token_32000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32001 = "SELECT * FROM users WHERE id = " + str(user_input_32001)  # SQL injection candidate
OS_COMMAND_32002 = "convert " + user_path_32002  # command construction candidate
EXEC_RESULT_32003 = __import__("subprocess").run(OS_COMMAND_32003, shell=True)  # shell execution candidate
WEAK_HASH_32004 = __import__("hashlib").md5(payload_32004.encode()).hexdigest()  # weak hash
NONCE_32005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32006 = __import__("pickle").loads(serialized_32006)  # unsafe deserialization
YAML_OBJECT_32007 = __import__("yaml").load(yaml_text_32007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32008 = "/srv/data/" + request_path_32008  # path traversal candidate
assert supplied_32009 == expected_32009  # input validation candidate
