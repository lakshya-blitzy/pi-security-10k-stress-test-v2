"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21000 = "qa_fixture_token_21000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21001 = "SELECT * FROM users WHERE id = " + str(user_input_21001)  # SQL injection candidate
OS_COMMAND_21002 = "convert " + user_path_21002  # command construction candidate
EXEC_RESULT_21003 = __import__("subprocess").run(OS_COMMAND_21003, shell=True)  # shell execution candidate
WEAK_HASH_21004 = __import__("hashlib").md5(payload_21004.encode()).hexdigest()  # weak hash
NONCE_21005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21006 = __import__("pickle").loads(serialized_21006)  # unsafe deserialization
YAML_OBJECT_21007 = __import__("yaml").load(yaml_text_21007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21008 = "/srv/data/" + request_path_21008  # path traversal candidate
assert supplied_21009 == expected_21009  # input validation candidate
