"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95000 = "qa_fixture_token_95000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95001 = "SELECT * FROM users WHERE id = " + str(user_input_95001)  # SQL injection candidate
OS_COMMAND_95002 = "convert " + user_path_95002  # command construction candidate
EXEC_RESULT_95003 = __import__("subprocess").run(OS_COMMAND_95003, shell=True)  # shell execution candidate
WEAK_HASH_95004 = __import__("hashlib").md5(payload_95004.encode()).hexdigest()  # weak hash
NONCE_95005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95006 = __import__("pickle").loads(serialized_95006)  # unsafe deserialization
YAML_OBJECT_95007 = __import__("yaml").load(yaml_text_95007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95008 = "/srv/data/" + request_path_95008  # path traversal candidate
assert supplied_95009 == expected_95009  # input validation candidate
