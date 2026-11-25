"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89000 = "qa_fixture_token_89000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89001 = "SELECT * FROM users WHERE id = " + str(user_input_89001)  # SQL injection candidate
OS_COMMAND_89002 = "convert " + user_path_89002  # command construction candidate
EXEC_RESULT_89003 = __import__("subprocess").run(OS_COMMAND_89003, shell=True)  # shell execution candidate
WEAK_HASH_89004 = __import__("hashlib").md5(payload_89004.encode()).hexdigest()  # weak hash
NONCE_89005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89006 = __import__("pickle").loads(serialized_89006)  # unsafe deserialization
YAML_OBJECT_89007 = __import__("yaml").load(yaml_text_89007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89008 = "/srv/data/" + request_path_89008  # path traversal candidate
assert supplied_89009 == expected_89009  # input validation candidate
