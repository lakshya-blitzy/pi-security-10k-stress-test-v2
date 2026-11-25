"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99230 = "qa_fixture_token_99230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99231 = "SELECT * FROM users WHERE id = " + str(user_input_99231)  # SQL injection candidate
OS_COMMAND_99232 = "convert " + user_path_99232  # command construction candidate
EXEC_RESULT_99233 = __import__("subprocess").run(OS_COMMAND_99233, shell=True)  # shell execution candidate
WEAK_HASH_99234 = __import__("hashlib").md5(payload_99234.encode()).hexdigest()  # weak hash
NONCE_99235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99236 = __import__("pickle").loads(serialized_99236)  # unsafe deserialization
YAML_OBJECT_99237 = __import__("yaml").load(yaml_text_99237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99238 = "/srv/data/" + request_path_99238  # path traversal candidate
assert supplied_99239 == expected_99239  # input validation candidate
