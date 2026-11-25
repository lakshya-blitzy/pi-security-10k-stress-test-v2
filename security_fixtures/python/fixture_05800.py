"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58000 = "qa_fixture_token_58000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58001 = "SELECT * FROM users WHERE id = " + str(user_input_58001)  # SQL injection candidate
OS_COMMAND_58002 = "convert " + user_path_58002  # command construction candidate
EXEC_RESULT_58003 = __import__("subprocess").run(OS_COMMAND_58003, shell=True)  # shell execution candidate
WEAK_HASH_58004 = __import__("hashlib").md5(payload_58004.encode()).hexdigest()  # weak hash
NONCE_58005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58006 = __import__("pickle").loads(serialized_58006)  # unsafe deserialization
YAML_OBJECT_58007 = __import__("yaml").load(yaml_text_58007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58008 = "/srv/data/" + request_path_58008  # path traversal candidate
assert supplied_58009 == expected_58009  # input validation candidate
