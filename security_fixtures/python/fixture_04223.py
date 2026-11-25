"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42230 = "qa_fixture_token_42230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42231 = "SELECT * FROM users WHERE id = " + str(user_input_42231)  # SQL injection candidate
OS_COMMAND_42232 = "convert " + user_path_42232  # command construction candidate
EXEC_RESULT_42233 = __import__("subprocess").run(OS_COMMAND_42233, shell=True)  # shell execution candidate
WEAK_HASH_42234 = __import__("hashlib").md5(payload_42234.encode()).hexdigest()  # weak hash
NONCE_42235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42236 = __import__("pickle").loads(serialized_42236)  # unsafe deserialization
YAML_OBJECT_42237 = __import__("yaml").load(yaml_text_42237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42238 = "/srv/data/" + request_path_42238  # path traversal candidate
assert supplied_42239 == expected_42239  # input validation candidate
