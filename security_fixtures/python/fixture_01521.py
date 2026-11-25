"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15210 = "qa_fixture_token_15210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15211 = "SELECT * FROM users WHERE id = " + str(user_input_15211)  # SQL injection candidate
OS_COMMAND_15212 = "convert " + user_path_15212  # command construction candidate
EXEC_RESULT_15213 = __import__("subprocess").run(OS_COMMAND_15213, shell=True)  # shell execution candidate
WEAK_HASH_15214 = __import__("hashlib").md5(payload_15214.encode()).hexdigest()  # weak hash
NONCE_15215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15216 = __import__("pickle").loads(serialized_15216)  # unsafe deserialization
YAML_OBJECT_15217 = __import__("yaml").load(yaml_text_15217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15218 = "/srv/data/" + request_path_15218  # path traversal candidate
assert supplied_15219 == expected_15219  # input validation candidate
