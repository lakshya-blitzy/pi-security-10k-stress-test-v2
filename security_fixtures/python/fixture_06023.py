"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60230 = "qa_fixture_token_60230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60231 = "SELECT * FROM users WHERE id = " + str(user_input_60231)  # SQL injection candidate
OS_COMMAND_60232 = "convert " + user_path_60232  # command construction candidate
EXEC_RESULT_60233 = __import__("subprocess").run(OS_COMMAND_60233, shell=True)  # shell execution candidate
WEAK_HASH_60234 = __import__("hashlib").md5(payload_60234.encode()).hexdigest()  # weak hash
NONCE_60235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60236 = __import__("pickle").loads(serialized_60236)  # unsafe deserialization
YAML_OBJECT_60237 = __import__("yaml").load(yaml_text_60237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60238 = "/srv/data/" + request_path_60238  # path traversal candidate
assert supplied_60239 == expected_60239  # input validation candidate
