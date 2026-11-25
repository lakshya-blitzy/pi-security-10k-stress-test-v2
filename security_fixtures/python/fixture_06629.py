"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66290 = "qa_fixture_token_66290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66291 = "SELECT * FROM users WHERE id = " + str(user_input_66291)  # SQL injection candidate
OS_COMMAND_66292 = "convert " + user_path_66292  # command construction candidate
EXEC_RESULT_66293 = __import__("subprocess").run(OS_COMMAND_66293, shell=True)  # shell execution candidate
WEAK_HASH_66294 = __import__("hashlib").md5(payload_66294.encode()).hexdigest()  # weak hash
NONCE_66295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66296 = __import__("pickle").loads(serialized_66296)  # unsafe deserialization
YAML_OBJECT_66297 = __import__("yaml").load(yaml_text_66297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66298 = "/srv/data/" + request_path_66298  # path traversal candidate
assert supplied_66299 == expected_66299  # input validation candidate
