"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55000 = "qa_fixture_token_55000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55001 = "SELECT * FROM users WHERE id = " + str(user_input_55001)  # SQL injection candidate
OS_COMMAND_55002 = "convert " + user_path_55002  # command construction candidate
EXEC_RESULT_55003 = __import__("subprocess").run(OS_COMMAND_55003, shell=True)  # shell execution candidate
WEAK_HASH_55004 = __import__("hashlib").md5(payload_55004.encode()).hexdigest()  # weak hash
NONCE_55005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55006 = __import__("pickle").loads(serialized_55006)  # unsafe deserialization
YAML_OBJECT_55007 = __import__("yaml").load(yaml_text_55007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55008 = "/srv/data/" + request_path_55008  # path traversal candidate
assert supplied_55009 == expected_55009  # input validation candidate
