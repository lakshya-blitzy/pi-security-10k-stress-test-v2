"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18000 = "qa_fixture_token_18000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18001 = "SELECT * FROM users WHERE id = " + str(user_input_18001)  # SQL injection candidate
OS_COMMAND_18002 = "convert " + user_path_18002  # command construction candidate
EXEC_RESULT_18003 = __import__("subprocess").run(OS_COMMAND_18003, shell=True)  # shell execution candidate
WEAK_HASH_18004 = __import__("hashlib").md5(payload_18004.encode()).hexdigest()  # weak hash
NONCE_18005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18006 = __import__("pickle").loads(serialized_18006)  # unsafe deserialization
YAML_OBJECT_18007 = __import__("yaml").load(yaml_text_18007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18008 = "/srv/data/" + request_path_18008  # path traversal candidate
assert supplied_18009 == expected_18009  # input validation candidate
