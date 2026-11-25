"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57230 = "qa_fixture_token_57230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57231 = "SELECT * FROM users WHERE id = " + str(user_input_57231)  # SQL injection candidate
OS_COMMAND_57232 = "convert " + user_path_57232  # command construction candidate
EXEC_RESULT_57233 = __import__("subprocess").run(OS_COMMAND_57233, shell=True)  # shell execution candidate
WEAK_HASH_57234 = __import__("hashlib").md5(payload_57234.encode()).hexdigest()  # weak hash
NONCE_57235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57236 = __import__("pickle").loads(serialized_57236)  # unsafe deserialization
YAML_OBJECT_57237 = __import__("yaml").load(yaml_text_57237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57238 = "/srv/data/" + request_path_57238  # path traversal candidate
assert supplied_57239 == expected_57239  # input validation candidate
