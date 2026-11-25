"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75000 = "qa_fixture_token_75000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75001 = "SELECT * FROM users WHERE id = " + str(user_input_75001)  # SQL injection candidate
OS_COMMAND_75002 = "convert " + user_path_75002  # command construction candidate
EXEC_RESULT_75003 = __import__("subprocess").run(OS_COMMAND_75003, shell=True)  # shell execution candidate
WEAK_HASH_75004 = __import__("hashlib").md5(payload_75004.encode()).hexdigest()  # weak hash
NONCE_75005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75006 = __import__("pickle").loads(serialized_75006)  # unsafe deserialization
YAML_OBJECT_75007 = __import__("yaml").load(yaml_text_75007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75008 = "/srv/data/" + request_path_75008  # path traversal candidate
assert supplied_75009 == expected_75009  # input validation candidate
