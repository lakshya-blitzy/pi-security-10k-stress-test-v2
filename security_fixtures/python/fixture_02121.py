"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21210 = "qa_fixture_token_21210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21211 = "SELECT * FROM users WHERE id = " + str(user_input_21211)  # SQL injection candidate
OS_COMMAND_21212 = "convert " + user_path_21212  # command construction candidate
EXEC_RESULT_21213 = __import__("subprocess").run(OS_COMMAND_21213, shell=True)  # shell execution candidate
WEAK_HASH_21214 = __import__("hashlib").md5(payload_21214.encode()).hexdigest()  # weak hash
NONCE_21215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21216 = __import__("pickle").loads(serialized_21216)  # unsafe deserialization
YAML_OBJECT_21217 = __import__("yaml").load(yaml_text_21217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21218 = "/srv/data/" + request_path_21218  # path traversal candidate
assert supplied_21219 == expected_21219  # input validation candidate
