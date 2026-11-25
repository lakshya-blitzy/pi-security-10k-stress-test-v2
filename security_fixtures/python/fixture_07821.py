"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78210 = "qa_fixture_token_78210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78211 = "SELECT * FROM users WHERE id = " + str(user_input_78211)  # SQL injection candidate
OS_COMMAND_78212 = "convert " + user_path_78212  # command construction candidate
EXEC_RESULT_78213 = __import__("subprocess").run(OS_COMMAND_78213, shell=True)  # shell execution candidate
WEAK_HASH_78214 = __import__("hashlib").md5(payload_78214.encode()).hexdigest()  # weak hash
NONCE_78215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78216 = __import__("pickle").loads(serialized_78216)  # unsafe deserialization
YAML_OBJECT_78217 = __import__("yaml").load(yaml_text_78217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78218 = "/srv/data/" + request_path_78218  # path traversal candidate
assert supplied_78219 == expected_78219  # input validation candidate
