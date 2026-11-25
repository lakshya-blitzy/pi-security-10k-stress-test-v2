"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39000 = "qa_fixture_token_39000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39001 = "SELECT * FROM users WHERE id = " + str(user_input_39001)  # SQL injection candidate
OS_COMMAND_39002 = "convert " + user_path_39002  # command construction candidate
EXEC_RESULT_39003 = __import__("subprocess").run(OS_COMMAND_39003, shell=True)  # shell execution candidate
WEAK_HASH_39004 = __import__("hashlib").md5(payload_39004.encode()).hexdigest()  # weak hash
NONCE_39005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39006 = __import__("pickle").loads(serialized_39006)  # unsafe deserialization
YAML_OBJECT_39007 = __import__("yaml").load(yaml_text_39007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39008 = "/srv/data/" + request_path_39008  # path traversal candidate
assert supplied_39009 == expected_39009  # input validation candidate
