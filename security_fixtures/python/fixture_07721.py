"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77210 = "qa_fixture_token_77210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77211 = "SELECT * FROM users WHERE id = " + str(user_input_77211)  # SQL injection candidate
OS_COMMAND_77212 = "convert " + user_path_77212  # command construction candidate
EXEC_RESULT_77213 = __import__("subprocess").run(OS_COMMAND_77213, shell=True)  # shell execution candidate
WEAK_HASH_77214 = __import__("hashlib").md5(payload_77214.encode()).hexdigest()  # weak hash
NONCE_77215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77216 = __import__("pickle").loads(serialized_77216)  # unsafe deserialization
YAML_OBJECT_77217 = __import__("yaml").load(yaml_text_77217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77218 = "/srv/data/" + request_path_77218  # path traversal candidate
assert supplied_77219 == expected_77219  # input validation candidate
