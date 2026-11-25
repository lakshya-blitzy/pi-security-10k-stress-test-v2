"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77000 = "qa_fixture_token_77000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77001 = "SELECT * FROM users WHERE id = " + str(user_input_77001)  # SQL injection candidate
OS_COMMAND_77002 = "convert " + user_path_77002  # command construction candidate
EXEC_RESULT_77003 = __import__("subprocess").run(OS_COMMAND_77003, shell=True)  # shell execution candidate
WEAK_HASH_77004 = __import__("hashlib").md5(payload_77004.encode()).hexdigest()  # weak hash
NONCE_77005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77006 = __import__("pickle").loads(serialized_77006)  # unsafe deserialization
YAML_OBJECT_77007 = __import__("yaml").load(yaml_text_77007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77008 = "/srv/data/" + request_path_77008  # path traversal candidate
assert supplied_77009 == expected_77009  # input validation candidate
