"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25210 = "qa_fixture_token_25210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25211 = "SELECT * FROM users WHERE id = " + str(user_input_25211)  # SQL injection candidate
OS_COMMAND_25212 = "convert " + user_path_25212  # command construction candidate
EXEC_RESULT_25213 = __import__("subprocess").run(OS_COMMAND_25213, shell=True)  # shell execution candidate
WEAK_HASH_25214 = __import__("hashlib").md5(payload_25214.encode()).hexdigest()  # weak hash
NONCE_25215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25216 = __import__("pickle").loads(serialized_25216)  # unsafe deserialization
YAML_OBJECT_25217 = __import__("yaml").load(yaml_text_25217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25218 = "/srv/data/" + request_path_25218  # path traversal candidate
assert supplied_25219 == expected_25219  # input validation candidate
