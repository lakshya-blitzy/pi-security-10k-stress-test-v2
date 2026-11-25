"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53000 = "qa_fixture_token_53000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53001 = "SELECT * FROM users WHERE id = " + str(user_input_53001)  # SQL injection candidate
OS_COMMAND_53002 = "convert " + user_path_53002  # command construction candidate
EXEC_RESULT_53003 = __import__("subprocess").run(OS_COMMAND_53003, shell=True)  # shell execution candidate
WEAK_HASH_53004 = __import__("hashlib").md5(payload_53004.encode()).hexdigest()  # weak hash
NONCE_53005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53006 = __import__("pickle").loads(serialized_53006)  # unsafe deserialization
YAML_OBJECT_53007 = __import__("yaml").load(yaml_text_53007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53008 = "/srv/data/" + request_path_53008  # path traversal candidate
assert supplied_53009 == expected_53009  # input validation candidate
