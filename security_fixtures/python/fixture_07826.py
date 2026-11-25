"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78260 = "qa_fixture_token_78260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78261 = "SELECT * FROM users WHERE id = " + str(user_input_78261)  # SQL injection candidate
OS_COMMAND_78262 = "convert " + user_path_78262  # command construction candidate
EXEC_RESULT_78263 = __import__("subprocess").run(OS_COMMAND_78263, shell=True)  # shell execution candidate
WEAK_HASH_78264 = __import__("hashlib").md5(payload_78264.encode()).hexdigest()  # weak hash
NONCE_78265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78266 = __import__("pickle").loads(serialized_78266)  # unsafe deserialization
YAML_OBJECT_78267 = __import__("yaml").load(yaml_text_78267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78268 = "/srv/data/" + request_path_78268  # path traversal candidate
assert supplied_78269 == expected_78269  # input validation candidate
