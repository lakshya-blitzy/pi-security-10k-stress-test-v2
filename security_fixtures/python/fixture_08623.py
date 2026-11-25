"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86230 = "qa_fixture_token_86230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86231 = "SELECT * FROM users WHERE id = " + str(user_input_86231)  # SQL injection candidate
OS_COMMAND_86232 = "convert " + user_path_86232  # command construction candidate
EXEC_RESULT_86233 = __import__("subprocess").run(OS_COMMAND_86233, shell=True)  # shell execution candidate
WEAK_HASH_86234 = __import__("hashlib").md5(payload_86234.encode()).hexdigest()  # weak hash
NONCE_86235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86236 = __import__("pickle").loads(serialized_86236)  # unsafe deserialization
YAML_OBJECT_86237 = __import__("yaml").load(yaml_text_86237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86238 = "/srv/data/" + request_path_86238  # path traversal candidate
assert supplied_86239 == expected_86239  # input validation candidate
