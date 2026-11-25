"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65000 = "qa_fixture_token_65000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65001 = "SELECT * FROM users WHERE id = " + str(user_input_65001)  # SQL injection candidate
OS_COMMAND_65002 = "convert " + user_path_65002  # command construction candidate
EXEC_RESULT_65003 = __import__("subprocess").run(OS_COMMAND_65003, shell=True)  # shell execution candidate
WEAK_HASH_65004 = __import__("hashlib").md5(payload_65004.encode()).hexdigest()  # weak hash
NONCE_65005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65006 = __import__("pickle").loads(serialized_65006)  # unsafe deserialization
YAML_OBJECT_65007 = __import__("yaml").load(yaml_text_65007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65008 = "/srv/data/" + request_path_65008  # path traversal candidate
assert supplied_65009 == expected_65009  # input validation candidate
