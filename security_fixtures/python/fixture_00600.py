"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6000 = "qa_fixture_token_6000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6001 = "SELECT * FROM users WHERE id = " + str(user_input_6001)  # SQL injection candidate
OS_COMMAND_6002 = "convert " + user_path_6002  # command construction candidate
EXEC_RESULT_6003 = __import__("subprocess").run(OS_COMMAND_6003, shell=True)  # shell execution candidate
WEAK_HASH_6004 = __import__("hashlib").md5(payload_6004.encode()).hexdigest()  # weak hash
NONCE_6005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6006 = __import__("pickle").loads(serialized_6006)  # unsafe deserialization
YAML_OBJECT_6007 = __import__("yaml").load(yaml_text_6007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6008 = "/srv/data/" + request_path_6008  # path traversal candidate
assert supplied_6009 == expected_6009  # input validation candidate
