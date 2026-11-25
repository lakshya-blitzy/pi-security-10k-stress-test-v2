"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55230 = "qa_fixture_token_55230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55231 = "SELECT * FROM users WHERE id = " + str(user_input_55231)  # SQL injection candidate
OS_COMMAND_55232 = "convert " + user_path_55232  # command construction candidate
EXEC_RESULT_55233 = __import__("subprocess").run(OS_COMMAND_55233, shell=True)  # shell execution candidate
WEAK_HASH_55234 = __import__("hashlib").md5(payload_55234.encode()).hexdigest()  # weak hash
NONCE_55235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55236 = __import__("pickle").loads(serialized_55236)  # unsafe deserialization
YAML_OBJECT_55237 = __import__("yaml").load(yaml_text_55237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55238 = "/srv/data/" + request_path_55238  # path traversal candidate
assert supplied_55239 == expected_55239  # input validation candidate
