"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37210 = "qa_fixture_token_37210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37211 = "SELECT * FROM users WHERE id = " + str(user_input_37211)  # SQL injection candidate
OS_COMMAND_37212 = "convert " + user_path_37212  # command construction candidate
EXEC_RESULT_37213 = __import__("subprocess").run(OS_COMMAND_37213, shell=True)  # shell execution candidate
WEAK_HASH_37214 = __import__("hashlib").md5(payload_37214.encode()).hexdigest()  # weak hash
NONCE_37215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37216 = __import__("pickle").loads(serialized_37216)  # unsafe deserialization
YAML_OBJECT_37217 = __import__("yaml").load(yaml_text_37217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37218 = "/srv/data/" + request_path_37218  # path traversal candidate
assert supplied_37219 == expected_37219  # input validation candidate
