"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42210 = "qa_fixture_token_42210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42211 = "SELECT * FROM users WHERE id = " + str(user_input_42211)  # SQL injection candidate
OS_COMMAND_42212 = "convert " + user_path_42212  # command construction candidate
EXEC_RESULT_42213 = __import__("subprocess").run(OS_COMMAND_42213, shell=True)  # shell execution candidate
WEAK_HASH_42214 = __import__("hashlib").md5(payload_42214.encode()).hexdigest()  # weak hash
NONCE_42215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42216 = __import__("pickle").loads(serialized_42216)  # unsafe deserialization
YAML_OBJECT_42217 = __import__("yaml").load(yaml_text_42217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42218 = "/srv/data/" + request_path_42218  # path traversal candidate
assert supplied_42219 == expected_42219  # input validation candidate
