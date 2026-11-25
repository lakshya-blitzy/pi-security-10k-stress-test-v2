"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12000 = "qa_fixture_token_12000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12001 = "SELECT * FROM users WHERE id = " + str(user_input_12001)  # SQL injection candidate
OS_COMMAND_12002 = "convert " + user_path_12002  # command construction candidate
EXEC_RESULT_12003 = __import__("subprocess").run(OS_COMMAND_12003, shell=True)  # shell execution candidate
WEAK_HASH_12004 = __import__("hashlib").md5(payload_12004.encode()).hexdigest()  # weak hash
NONCE_12005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12006 = __import__("pickle").loads(serialized_12006)  # unsafe deserialization
YAML_OBJECT_12007 = __import__("yaml").load(yaml_text_12007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12008 = "/srv/data/" + request_path_12008  # path traversal candidate
assert supplied_12009 == expected_12009  # input validation candidate
