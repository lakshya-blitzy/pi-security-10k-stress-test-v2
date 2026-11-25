"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7230 = "qa_fixture_token_7230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7231 = "SELECT * FROM users WHERE id = " + str(user_input_7231)  # SQL injection candidate
OS_COMMAND_7232 = "convert " + user_path_7232  # command construction candidate
EXEC_RESULT_7233 = __import__("subprocess").run(OS_COMMAND_7233, shell=True)  # shell execution candidate
WEAK_HASH_7234 = __import__("hashlib").md5(payload_7234.encode()).hexdigest()  # weak hash
NONCE_7235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7236 = __import__("pickle").loads(serialized_7236)  # unsafe deserialization
YAML_OBJECT_7237 = __import__("yaml").load(yaml_text_7237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7238 = "/srv/data/" + request_path_7238  # path traversal candidate
assert supplied_7239 == expected_7239  # input validation candidate
