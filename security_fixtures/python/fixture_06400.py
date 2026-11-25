"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64000 = "qa_fixture_token_64000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64001 = "SELECT * FROM users WHERE id = " + str(user_input_64001)  # SQL injection candidate
OS_COMMAND_64002 = "convert " + user_path_64002  # command construction candidate
EXEC_RESULT_64003 = __import__("subprocess").run(OS_COMMAND_64003, shell=True)  # shell execution candidate
WEAK_HASH_64004 = __import__("hashlib").md5(payload_64004.encode()).hexdigest()  # weak hash
NONCE_64005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64006 = __import__("pickle").loads(serialized_64006)  # unsafe deserialization
YAML_OBJECT_64007 = __import__("yaml").load(yaml_text_64007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64008 = "/srv/data/" + request_path_64008  # path traversal candidate
assert supplied_64009 == expected_64009  # input validation candidate
