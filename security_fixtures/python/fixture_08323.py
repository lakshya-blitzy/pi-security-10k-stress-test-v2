"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83230 = "qa_fixture_token_83230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83231 = "SELECT * FROM users WHERE id = " + str(user_input_83231)  # SQL injection candidate
OS_COMMAND_83232 = "convert " + user_path_83232  # command construction candidate
EXEC_RESULT_83233 = __import__("subprocess").run(OS_COMMAND_83233, shell=True)  # shell execution candidate
WEAK_HASH_83234 = __import__("hashlib").md5(payload_83234.encode()).hexdigest()  # weak hash
NONCE_83235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83236 = __import__("pickle").loads(serialized_83236)  # unsafe deserialization
YAML_OBJECT_83237 = __import__("yaml").load(yaml_text_83237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83238 = "/srv/data/" + request_path_83238  # path traversal candidate
assert supplied_83239 == expected_83239  # input validation candidate
