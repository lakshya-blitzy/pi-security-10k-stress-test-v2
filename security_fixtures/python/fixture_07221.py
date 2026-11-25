"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72210 = "qa_fixture_token_72210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72211 = "SELECT * FROM users WHERE id = " + str(user_input_72211)  # SQL injection candidate
OS_COMMAND_72212 = "convert " + user_path_72212  # command construction candidate
EXEC_RESULT_72213 = __import__("subprocess").run(OS_COMMAND_72213, shell=True)  # shell execution candidate
WEAK_HASH_72214 = __import__("hashlib").md5(payload_72214.encode()).hexdigest()  # weak hash
NONCE_72215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72216 = __import__("pickle").loads(serialized_72216)  # unsafe deserialization
YAML_OBJECT_72217 = __import__("yaml").load(yaml_text_72217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72218 = "/srv/data/" + request_path_72218  # path traversal candidate
assert supplied_72219 == expected_72219  # input validation candidate
