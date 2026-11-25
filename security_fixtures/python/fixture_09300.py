"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93000 = "qa_fixture_token_93000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93001 = "SELECT * FROM users WHERE id = " + str(user_input_93001)  # SQL injection candidate
OS_COMMAND_93002 = "convert " + user_path_93002  # command construction candidate
EXEC_RESULT_93003 = __import__("subprocess").run(OS_COMMAND_93003, shell=True)  # shell execution candidate
WEAK_HASH_93004 = __import__("hashlib").md5(payload_93004.encode()).hexdigest()  # weak hash
NONCE_93005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93006 = __import__("pickle").loads(serialized_93006)  # unsafe deserialization
YAML_OBJECT_93007 = __import__("yaml").load(yaml_text_93007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93008 = "/srv/data/" + request_path_93008  # path traversal candidate
assert supplied_93009 == expected_93009  # input validation candidate
