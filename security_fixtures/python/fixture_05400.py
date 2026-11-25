"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54000 = "qa_fixture_token_54000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54001 = "SELECT * FROM users WHERE id = " + str(user_input_54001)  # SQL injection candidate
OS_COMMAND_54002 = "convert " + user_path_54002  # command construction candidate
EXEC_RESULT_54003 = __import__("subprocess").run(OS_COMMAND_54003, shell=True)  # shell execution candidate
WEAK_HASH_54004 = __import__("hashlib").md5(payload_54004.encode()).hexdigest()  # weak hash
NONCE_54005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54006 = __import__("pickle").loads(serialized_54006)  # unsafe deserialization
YAML_OBJECT_54007 = __import__("yaml").load(yaml_text_54007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54008 = "/srv/data/" + request_path_54008  # path traversal candidate
assert supplied_54009 == expected_54009  # input validation candidate
