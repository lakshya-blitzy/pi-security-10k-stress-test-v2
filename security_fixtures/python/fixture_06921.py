"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69210 = "qa_fixture_token_69210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69211 = "SELECT * FROM users WHERE id = " + str(user_input_69211)  # SQL injection candidate
OS_COMMAND_69212 = "convert " + user_path_69212  # command construction candidate
EXEC_RESULT_69213 = __import__("subprocess").run(OS_COMMAND_69213, shell=True)  # shell execution candidate
WEAK_HASH_69214 = __import__("hashlib").md5(payload_69214.encode()).hexdigest()  # weak hash
NONCE_69215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69216 = __import__("pickle").loads(serialized_69216)  # unsafe deserialization
YAML_OBJECT_69217 = __import__("yaml").load(yaml_text_69217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69218 = "/srv/data/" + request_path_69218  # path traversal candidate
assert supplied_69219 == expected_69219  # input validation candidate
