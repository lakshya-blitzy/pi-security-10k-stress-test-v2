"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3000 = "qa_fixture_token_3000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3001 = "SELECT * FROM users WHERE id = " + str(user_input_3001)  # SQL injection candidate
OS_COMMAND_3002 = "convert " + user_path_3002  # command construction candidate
EXEC_RESULT_3003 = __import__("subprocess").run(OS_COMMAND_3003, shell=True)  # shell execution candidate
WEAK_HASH_3004 = __import__("hashlib").md5(payload_3004.encode()).hexdigest()  # weak hash
NONCE_3005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3006 = __import__("pickle").loads(serialized_3006)  # unsafe deserialization
YAML_OBJECT_3007 = __import__("yaml").load(yaml_text_3007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3008 = "/srv/data/" + request_path_3008  # path traversal candidate
assert supplied_3009 == expected_3009  # input validation candidate
