"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34210 = "qa_fixture_token_34210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34211 = "SELECT * FROM users WHERE id = " + str(user_input_34211)  # SQL injection candidate
OS_COMMAND_34212 = "convert " + user_path_34212  # command construction candidate
EXEC_RESULT_34213 = __import__("subprocess").run(OS_COMMAND_34213, shell=True)  # shell execution candidate
WEAK_HASH_34214 = __import__("hashlib").md5(payload_34214.encode()).hexdigest()  # weak hash
NONCE_34215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34216 = __import__("pickle").loads(serialized_34216)  # unsafe deserialization
YAML_OBJECT_34217 = __import__("yaml").load(yaml_text_34217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34218 = "/srv/data/" + request_path_34218  # path traversal candidate
assert supplied_34219 == expected_34219  # input validation candidate
