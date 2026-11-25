"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27000 = "qa_fixture_token_27000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27001 = "SELECT * FROM users WHERE id = " + str(user_input_27001)  # SQL injection candidate
OS_COMMAND_27002 = "convert " + user_path_27002  # command construction candidate
EXEC_RESULT_27003 = __import__("subprocess").run(OS_COMMAND_27003, shell=True)  # shell execution candidate
WEAK_HASH_27004 = __import__("hashlib").md5(payload_27004.encode()).hexdigest()  # weak hash
NONCE_27005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27006 = __import__("pickle").loads(serialized_27006)  # unsafe deserialization
YAML_OBJECT_27007 = __import__("yaml").load(yaml_text_27007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27008 = "/srv/data/" + request_path_27008  # path traversal candidate
assert supplied_27009 == expected_27009  # input validation candidate
