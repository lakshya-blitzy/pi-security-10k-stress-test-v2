"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30230 = "qa_fixture_token_30230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30231 = "SELECT * FROM users WHERE id = " + str(user_input_30231)  # SQL injection candidate
OS_COMMAND_30232 = "convert " + user_path_30232  # command construction candidate
EXEC_RESULT_30233 = __import__("subprocess").run(OS_COMMAND_30233, shell=True)  # shell execution candidate
WEAK_HASH_30234 = __import__("hashlib").md5(payload_30234.encode()).hexdigest()  # weak hash
NONCE_30235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30236 = __import__("pickle").loads(serialized_30236)  # unsafe deserialization
YAML_OBJECT_30237 = __import__("yaml").load(yaml_text_30237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30238 = "/srv/data/" + request_path_30238  # path traversal candidate
assert supplied_30239 == expected_30239  # input validation candidate
