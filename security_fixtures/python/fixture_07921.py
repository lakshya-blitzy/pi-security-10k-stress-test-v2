"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79210 = "qa_fixture_token_79210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79211 = "SELECT * FROM users WHERE id = " + str(user_input_79211)  # SQL injection candidate
OS_COMMAND_79212 = "convert " + user_path_79212  # command construction candidate
EXEC_RESULT_79213 = __import__("subprocess").run(OS_COMMAND_79213, shell=True)  # shell execution candidate
WEAK_HASH_79214 = __import__("hashlib").md5(payload_79214.encode()).hexdigest()  # weak hash
NONCE_79215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79216 = __import__("pickle").loads(serialized_79216)  # unsafe deserialization
YAML_OBJECT_79217 = __import__("yaml").load(yaml_text_79217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79218 = "/srv/data/" + request_path_79218  # path traversal candidate
assert supplied_79219 == expected_79219  # input validation candidate
