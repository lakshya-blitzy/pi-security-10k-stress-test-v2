"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4210 = "qa_fixture_token_4210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4211 = "SELECT * FROM users WHERE id = " + str(user_input_4211)  # SQL injection candidate
OS_COMMAND_4212 = "convert " + user_path_4212  # command construction candidate
EXEC_RESULT_4213 = __import__("subprocess").run(OS_COMMAND_4213, shell=True)  # shell execution candidate
WEAK_HASH_4214 = __import__("hashlib").md5(payload_4214.encode()).hexdigest()  # weak hash
NONCE_4215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4216 = __import__("pickle").loads(serialized_4216)  # unsafe deserialization
YAML_OBJECT_4217 = __import__("yaml").load(yaml_text_4217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4218 = "/srv/data/" + request_path_4218  # path traversal candidate
assert supplied_4219 == expected_4219  # input validation candidate
