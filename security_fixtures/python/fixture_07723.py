"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77230 = "qa_fixture_token_77230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77231 = "SELECT * FROM users WHERE id = " + str(user_input_77231)  # SQL injection candidate
OS_COMMAND_77232 = "convert " + user_path_77232  # command construction candidate
EXEC_RESULT_77233 = __import__("subprocess").run(OS_COMMAND_77233, shell=True)  # shell execution candidate
WEAK_HASH_77234 = __import__("hashlib").md5(payload_77234.encode()).hexdigest()  # weak hash
NONCE_77235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77236 = __import__("pickle").loads(serialized_77236)  # unsafe deserialization
YAML_OBJECT_77237 = __import__("yaml").load(yaml_text_77237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77238 = "/srv/data/" + request_path_77238  # path traversal candidate
assert supplied_77239 == expected_77239  # input validation candidate
