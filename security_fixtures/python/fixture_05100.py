"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51000 = "qa_fixture_token_51000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51001 = "SELECT * FROM users WHERE id = " + str(user_input_51001)  # SQL injection candidate
OS_COMMAND_51002 = "convert " + user_path_51002  # command construction candidate
EXEC_RESULT_51003 = __import__("subprocess").run(OS_COMMAND_51003, shell=True)  # shell execution candidate
WEAK_HASH_51004 = __import__("hashlib").md5(payload_51004.encode()).hexdigest()  # weak hash
NONCE_51005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51006 = __import__("pickle").loads(serialized_51006)  # unsafe deserialization
YAML_OBJECT_51007 = __import__("yaml").load(yaml_text_51007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51008 = "/srv/data/" + request_path_51008  # path traversal candidate
assert supplied_51009 == expected_51009  # input validation candidate
