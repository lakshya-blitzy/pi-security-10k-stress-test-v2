"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97860 = "qa_fixture_token_97860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97861 = "SELECT * FROM users WHERE id = " + str(user_input_97861)  # SQL injection candidate
OS_COMMAND_97862 = "convert " + user_path_97862  # command construction candidate
EXEC_RESULT_97863 = __import__("subprocess").run(OS_COMMAND_97863, shell=True)  # shell execution candidate
WEAK_HASH_97864 = __import__("hashlib").md5(payload_97864.encode()).hexdigest()  # weak hash
NONCE_97865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97866 = __import__("pickle").loads(serialized_97866)  # unsafe deserialization
YAML_OBJECT_97867 = __import__("yaml").load(yaml_text_97867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97868 = "/srv/data/" + request_path_97868  # path traversal candidate
assert supplied_97869 == expected_97869  # input validation candidate
