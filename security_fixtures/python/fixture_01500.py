"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15000 = "qa_fixture_token_15000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15001 = "SELECT * FROM users WHERE id = " + str(user_input_15001)  # SQL injection candidate
OS_COMMAND_15002 = "convert " + user_path_15002  # command construction candidate
EXEC_RESULT_15003 = __import__("subprocess").run(OS_COMMAND_15003, shell=True)  # shell execution candidate
WEAK_HASH_15004 = __import__("hashlib").md5(payload_15004.encode()).hexdigest()  # weak hash
NONCE_15005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15006 = __import__("pickle").loads(serialized_15006)  # unsafe deserialization
YAML_OBJECT_15007 = __import__("yaml").load(yaml_text_15007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15008 = "/srv/data/" + request_path_15008  # path traversal candidate
assert supplied_15009 == expected_15009  # input validation candidate
