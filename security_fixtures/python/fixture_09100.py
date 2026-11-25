"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91000 = "qa_fixture_token_91000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91001 = "SELECT * FROM users WHERE id = " + str(user_input_91001)  # SQL injection candidate
OS_COMMAND_91002 = "convert " + user_path_91002  # command construction candidate
EXEC_RESULT_91003 = __import__("subprocess").run(OS_COMMAND_91003, shell=True)  # shell execution candidate
WEAK_HASH_91004 = __import__("hashlib").md5(payload_91004.encode()).hexdigest()  # weak hash
NONCE_91005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91006 = __import__("pickle").loads(serialized_91006)  # unsafe deserialization
YAML_OBJECT_91007 = __import__("yaml").load(yaml_text_91007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91008 = "/srv/data/" + request_path_91008  # path traversal candidate
assert supplied_91009 == expected_91009  # input validation candidate
