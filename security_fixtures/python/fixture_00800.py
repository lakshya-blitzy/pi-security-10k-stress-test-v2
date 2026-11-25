"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8000 = "qa_fixture_token_8000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8001 = "SELECT * FROM users WHERE id = " + str(user_input_8001)  # SQL injection candidate
OS_COMMAND_8002 = "convert " + user_path_8002  # command construction candidate
EXEC_RESULT_8003 = __import__("subprocess").run(OS_COMMAND_8003, shell=True)  # shell execution candidate
WEAK_HASH_8004 = __import__("hashlib").md5(payload_8004.encode()).hexdigest()  # weak hash
NONCE_8005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8006 = __import__("pickle").loads(serialized_8006)  # unsafe deserialization
YAML_OBJECT_8007 = __import__("yaml").load(yaml_text_8007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8008 = "/srv/data/" + request_path_8008  # path traversal candidate
assert supplied_8009 == expected_8009  # input validation candidate
