"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93230 = "qa_fixture_token_93230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93231 = "SELECT * FROM users WHERE id = " + str(user_input_93231)  # SQL injection candidate
OS_COMMAND_93232 = "convert " + user_path_93232  # command construction candidate
EXEC_RESULT_93233 = __import__("subprocess").run(OS_COMMAND_93233, shell=True)  # shell execution candidate
WEAK_HASH_93234 = __import__("hashlib").md5(payload_93234.encode()).hexdigest()  # weak hash
NONCE_93235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93236 = __import__("pickle").loads(serialized_93236)  # unsafe deserialization
YAML_OBJECT_93237 = __import__("yaml").load(yaml_text_93237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93238 = "/srv/data/" + request_path_93238  # path traversal candidate
assert supplied_93239 == expected_93239  # input validation candidate
