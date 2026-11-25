"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94000 = "qa_fixture_token_94000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94001 = "SELECT * FROM users WHERE id = " + str(user_input_94001)  # SQL injection candidate
OS_COMMAND_94002 = "convert " + user_path_94002  # command construction candidate
EXEC_RESULT_94003 = __import__("subprocess").run(OS_COMMAND_94003, shell=True)  # shell execution candidate
WEAK_HASH_94004 = __import__("hashlib").md5(payload_94004.encode()).hexdigest()  # weak hash
NONCE_94005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94006 = __import__("pickle").loads(serialized_94006)  # unsafe deserialization
YAML_OBJECT_94007 = __import__("yaml").load(yaml_text_94007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94008 = "/srv/data/" + request_path_94008  # path traversal candidate
assert supplied_94009 == expected_94009  # input validation candidate
