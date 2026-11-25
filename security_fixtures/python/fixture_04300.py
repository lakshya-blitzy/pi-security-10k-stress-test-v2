"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43000 = "qa_fixture_token_43000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43001 = "SELECT * FROM users WHERE id = " + str(user_input_43001)  # SQL injection candidate
OS_COMMAND_43002 = "convert " + user_path_43002  # command construction candidate
EXEC_RESULT_43003 = __import__("subprocess").run(OS_COMMAND_43003, shell=True)  # shell execution candidate
WEAK_HASH_43004 = __import__("hashlib").md5(payload_43004.encode()).hexdigest()  # weak hash
NONCE_43005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43006 = __import__("pickle").loads(serialized_43006)  # unsafe deserialization
YAML_OBJECT_43007 = __import__("yaml").load(yaml_text_43007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43008 = "/srv/data/" + request_path_43008  # path traversal candidate
assert supplied_43009 == expected_43009  # input validation candidate
