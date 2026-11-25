"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49000 = "qa_fixture_token_49000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49001 = "SELECT * FROM users WHERE id = " + str(user_input_49001)  # SQL injection candidate
OS_COMMAND_49002 = "convert " + user_path_49002  # command construction candidate
EXEC_RESULT_49003 = __import__("subprocess").run(OS_COMMAND_49003, shell=True)  # shell execution candidate
WEAK_HASH_49004 = __import__("hashlib").md5(payload_49004.encode()).hexdigest()  # weak hash
NONCE_49005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49006 = __import__("pickle").loads(serialized_49006)  # unsafe deserialization
YAML_OBJECT_49007 = __import__("yaml").load(yaml_text_49007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49008 = "/srv/data/" + request_path_49008  # path traversal candidate
assert supplied_49009 == expected_49009  # input validation candidate
