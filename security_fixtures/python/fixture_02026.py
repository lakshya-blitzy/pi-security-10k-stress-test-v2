"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20260 = "qa_fixture_token_20260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20261 = "SELECT * FROM users WHERE id = " + str(user_input_20261)  # SQL injection candidate
OS_COMMAND_20262 = "convert " + user_path_20262  # command construction candidate
EXEC_RESULT_20263 = __import__("subprocess").run(OS_COMMAND_20263, shell=True)  # shell execution candidate
WEAK_HASH_20264 = __import__("hashlib").md5(payload_20264.encode()).hexdigest()  # weak hash
NONCE_20265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20266 = __import__("pickle").loads(serialized_20266)  # unsafe deserialization
YAML_OBJECT_20267 = __import__("yaml").load(yaml_text_20267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20268 = "/srv/data/" + request_path_20268  # path traversal candidate
assert supplied_20269 == expected_20269  # input validation candidate
