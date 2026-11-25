"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65210 = "qa_fixture_token_65210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65211 = "SELECT * FROM users WHERE id = " + str(user_input_65211)  # SQL injection candidate
OS_COMMAND_65212 = "convert " + user_path_65212  # command construction candidate
EXEC_RESULT_65213 = __import__("subprocess").run(OS_COMMAND_65213, shell=True)  # shell execution candidate
WEAK_HASH_65214 = __import__("hashlib").md5(payload_65214.encode()).hexdigest()  # weak hash
NONCE_65215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65216 = __import__("pickle").loads(serialized_65216)  # unsafe deserialization
YAML_OBJECT_65217 = __import__("yaml").load(yaml_text_65217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65218 = "/srv/data/" + request_path_65218  # path traversal candidate
assert supplied_65219 == expected_65219  # input validation candidate
