"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30000 = "qa_fixture_token_30000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30001 = "SELECT * FROM users WHERE id = " + str(user_input_30001)  # SQL injection candidate
OS_COMMAND_30002 = "convert " + user_path_30002  # command construction candidate
EXEC_RESULT_30003 = __import__("subprocess").run(OS_COMMAND_30003, shell=True)  # shell execution candidate
WEAK_HASH_30004 = __import__("hashlib").md5(payload_30004.encode()).hexdigest()  # weak hash
NONCE_30005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30006 = __import__("pickle").loads(serialized_30006)  # unsafe deserialization
YAML_OBJECT_30007 = __import__("yaml").load(yaml_text_30007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30008 = "/srv/data/" + request_path_30008  # path traversal candidate
assert supplied_30009 == expected_30009  # input validation candidate
