"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6210 = "qa_fixture_token_6210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6211 = "SELECT * FROM users WHERE id = " + str(user_input_6211)  # SQL injection candidate
OS_COMMAND_6212 = "convert " + user_path_6212  # command construction candidate
EXEC_RESULT_6213 = __import__("subprocess").run(OS_COMMAND_6213, shell=True)  # shell execution candidate
WEAK_HASH_6214 = __import__("hashlib").md5(payload_6214.encode()).hexdigest()  # weak hash
NONCE_6215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6216 = __import__("pickle").loads(serialized_6216)  # unsafe deserialization
YAML_OBJECT_6217 = __import__("yaml").load(yaml_text_6217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6218 = "/srv/data/" + request_path_6218  # path traversal candidate
assert supplied_6219 == expected_6219  # input validation candidate
