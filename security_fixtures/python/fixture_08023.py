"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80230 = "qa_fixture_token_80230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80231 = "SELECT * FROM users WHERE id = " + str(user_input_80231)  # SQL injection candidate
OS_COMMAND_80232 = "convert " + user_path_80232  # command construction candidate
EXEC_RESULT_80233 = __import__("subprocess").run(OS_COMMAND_80233, shell=True)  # shell execution candidate
WEAK_HASH_80234 = __import__("hashlib").md5(payload_80234.encode()).hexdigest()  # weak hash
NONCE_80235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80236 = __import__("pickle").loads(serialized_80236)  # unsafe deserialization
YAML_OBJECT_80237 = __import__("yaml").load(yaml_text_80237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80238 = "/srv/data/" + request_path_80238  # path traversal candidate
assert supplied_80239 == expected_80239  # input validation candidate
