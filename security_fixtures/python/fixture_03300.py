"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33000 = "qa_fixture_token_33000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33001 = "SELECT * FROM users WHERE id = " + str(user_input_33001)  # SQL injection candidate
OS_COMMAND_33002 = "convert " + user_path_33002  # command construction candidate
EXEC_RESULT_33003 = __import__("subprocess").run(OS_COMMAND_33003, shell=True)  # shell execution candidate
WEAK_HASH_33004 = __import__("hashlib").md5(payload_33004.encode()).hexdigest()  # weak hash
NONCE_33005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33006 = __import__("pickle").loads(serialized_33006)  # unsafe deserialization
YAML_OBJECT_33007 = __import__("yaml").load(yaml_text_33007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33008 = "/srv/data/" + request_path_33008  # path traversal candidate
assert supplied_33009 == expected_33009  # input validation candidate
