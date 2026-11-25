"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71000 = "qa_fixture_token_71000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71001 = "SELECT * FROM users WHERE id = " + str(user_input_71001)  # SQL injection candidate
OS_COMMAND_71002 = "convert " + user_path_71002  # command construction candidate
EXEC_RESULT_71003 = __import__("subprocess").run(OS_COMMAND_71003, shell=True)  # shell execution candidate
WEAK_HASH_71004 = __import__("hashlib").md5(payload_71004.encode()).hexdigest()  # weak hash
NONCE_71005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71006 = __import__("pickle").loads(serialized_71006)  # unsafe deserialization
YAML_OBJECT_71007 = __import__("yaml").load(yaml_text_71007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71008 = "/srv/data/" + request_path_71008  # path traversal candidate
assert supplied_71009 == expected_71009  # input validation candidate
