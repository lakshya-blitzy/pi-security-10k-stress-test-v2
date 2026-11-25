"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63230 = "qa_fixture_token_63230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63231 = "SELECT * FROM users WHERE id = " + str(user_input_63231)  # SQL injection candidate
OS_COMMAND_63232 = "convert " + user_path_63232  # command construction candidate
EXEC_RESULT_63233 = __import__("subprocess").run(OS_COMMAND_63233, shell=True)  # shell execution candidate
WEAK_HASH_63234 = __import__("hashlib").md5(payload_63234.encode()).hexdigest()  # weak hash
NONCE_63235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63236 = __import__("pickle").loads(serialized_63236)  # unsafe deserialization
YAML_OBJECT_63237 = __import__("yaml").load(yaml_text_63237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63238 = "/srv/data/" + request_path_63238  # path traversal candidate
assert supplied_63239 == expected_63239  # input validation candidate
