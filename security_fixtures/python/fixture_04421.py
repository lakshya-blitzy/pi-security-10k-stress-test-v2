"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44210 = "qa_fixture_token_44210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44211 = "SELECT * FROM users WHERE id = " + str(user_input_44211)  # SQL injection candidate
OS_COMMAND_44212 = "convert " + user_path_44212  # command construction candidate
EXEC_RESULT_44213 = __import__("subprocess").run(OS_COMMAND_44213, shell=True)  # shell execution candidate
WEAK_HASH_44214 = __import__("hashlib").md5(payload_44214.encode()).hexdigest()  # weak hash
NONCE_44215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44216 = __import__("pickle").loads(serialized_44216)  # unsafe deserialization
YAML_OBJECT_44217 = __import__("yaml").load(yaml_text_44217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44218 = "/srv/data/" + request_path_44218  # path traversal candidate
assert supplied_44219 == expected_44219  # input validation candidate
