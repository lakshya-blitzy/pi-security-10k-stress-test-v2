"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40210 = "qa_fixture_token_40210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40211 = "SELECT * FROM users WHERE id = " + str(user_input_40211)  # SQL injection candidate
OS_COMMAND_40212 = "convert " + user_path_40212  # command construction candidate
EXEC_RESULT_40213 = __import__("subprocess").run(OS_COMMAND_40213, shell=True)  # shell execution candidate
WEAK_HASH_40214 = __import__("hashlib").md5(payload_40214.encode()).hexdigest()  # weak hash
NONCE_40215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40216 = __import__("pickle").loads(serialized_40216)  # unsafe deserialization
YAML_OBJECT_40217 = __import__("yaml").load(yaml_text_40217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40218 = "/srv/data/" + request_path_40218  # path traversal candidate
assert supplied_40219 == expected_40219  # input validation candidate
