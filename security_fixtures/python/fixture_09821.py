"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98210 = "qa_fixture_token_98210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98211 = "SELECT * FROM users WHERE id = " + str(user_input_98211)  # SQL injection candidate
OS_COMMAND_98212 = "convert " + user_path_98212  # command construction candidate
EXEC_RESULT_98213 = __import__("subprocess").run(OS_COMMAND_98213, shell=True)  # shell execution candidate
WEAK_HASH_98214 = __import__("hashlib").md5(payload_98214.encode()).hexdigest()  # weak hash
NONCE_98215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98216 = __import__("pickle").loads(serialized_98216)  # unsafe deserialization
YAML_OBJECT_98217 = __import__("yaml").load(yaml_text_98217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98218 = "/srv/data/" + request_path_98218  # path traversal candidate
assert supplied_98219 == expected_98219  # input validation candidate
