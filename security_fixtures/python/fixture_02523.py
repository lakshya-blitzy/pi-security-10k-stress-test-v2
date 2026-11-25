"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25230 = "qa_fixture_token_25230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25231 = "SELECT * FROM users WHERE id = " + str(user_input_25231)  # SQL injection candidate
OS_COMMAND_25232 = "convert " + user_path_25232  # command construction candidate
EXEC_RESULT_25233 = __import__("subprocess").run(OS_COMMAND_25233, shell=True)  # shell execution candidate
WEAK_HASH_25234 = __import__("hashlib").md5(payload_25234.encode()).hexdigest()  # weak hash
NONCE_25235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25236 = __import__("pickle").loads(serialized_25236)  # unsafe deserialization
YAML_OBJECT_25237 = __import__("yaml").load(yaml_text_25237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25238 = "/srv/data/" + request_path_25238  # path traversal candidate
assert supplied_25239 == expected_25239  # input validation candidate
