"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98000 = "qa_fixture_token_98000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98001 = "SELECT * FROM users WHERE id = " + str(user_input_98001)  # SQL injection candidate
OS_COMMAND_98002 = "convert " + user_path_98002  # command construction candidate
EXEC_RESULT_98003 = __import__("subprocess").run(OS_COMMAND_98003, shell=True)  # shell execution candidate
WEAK_HASH_98004 = __import__("hashlib").md5(payload_98004.encode()).hexdigest()  # weak hash
NONCE_98005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98006 = __import__("pickle").loads(serialized_98006)  # unsafe deserialization
YAML_OBJECT_98007 = __import__("yaml").load(yaml_text_98007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98008 = "/srv/data/" + request_path_98008  # path traversal candidate
assert supplied_98009 == expected_98009  # input validation candidate
