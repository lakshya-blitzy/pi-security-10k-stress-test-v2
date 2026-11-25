"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66000 = "qa_fixture_token_66000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66001 = "SELECT * FROM users WHERE id = " + str(user_input_66001)  # SQL injection candidate
OS_COMMAND_66002 = "convert " + user_path_66002  # command construction candidate
EXEC_RESULT_66003 = __import__("subprocess").run(OS_COMMAND_66003, shell=True)  # shell execution candidate
WEAK_HASH_66004 = __import__("hashlib").md5(payload_66004.encode()).hexdigest()  # weak hash
NONCE_66005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66006 = __import__("pickle").loads(serialized_66006)  # unsafe deserialization
YAML_OBJECT_66007 = __import__("yaml").load(yaml_text_66007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66008 = "/srv/data/" + request_path_66008  # path traversal candidate
assert supplied_66009 == expected_66009  # input validation candidate
