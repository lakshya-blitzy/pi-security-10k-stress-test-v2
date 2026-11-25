"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93210 = "qa_fixture_token_93210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93211 = "SELECT * FROM users WHERE id = " + str(user_input_93211)  # SQL injection candidate
OS_COMMAND_93212 = "convert " + user_path_93212  # command construction candidate
EXEC_RESULT_93213 = __import__("subprocess").run(OS_COMMAND_93213, shell=True)  # shell execution candidate
WEAK_HASH_93214 = __import__("hashlib").md5(payload_93214.encode()).hexdigest()  # weak hash
NONCE_93215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93216 = __import__("pickle").loads(serialized_93216)  # unsafe deserialization
YAML_OBJECT_93217 = __import__("yaml").load(yaml_text_93217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93218 = "/srv/data/" + request_path_93218  # path traversal candidate
assert supplied_93219 == expected_93219  # input validation candidate
