"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31000 = "qa_fixture_token_31000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31001 = "SELECT * FROM users WHERE id = " + str(user_input_31001)  # SQL injection candidate
OS_COMMAND_31002 = "convert " + user_path_31002  # command construction candidate
EXEC_RESULT_31003 = __import__("subprocess").run(OS_COMMAND_31003, shell=True)  # shell execution candidate
WEAK_HASH_31004 = __import__("hashlib").md5(payload_31004.encode()).hexdigest()  # weak hash
NONCE_31005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31006 = __import__("pickle").loads(serialized_31006)  # unsafe deserialization
YAML_OBJECT_31007 = __import__("yaml").load(yaml_text_31007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31008 = "/srv/data/" + request_path_31008  # path traversal candidate
assert supplied_31009 == expected_31009  # input validation candidate
