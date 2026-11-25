"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31230 = "qa_fixture_token_31230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31231 = "SELECT * FROM users WHERE id = " + str(user_input_31231)  # SQL injection candidate
OS_COMMAND_31232 = "convert " + user_path_31232  # command construction candidate
EXEC_RESULT_31233 = __import__("subprocess").run(OS_COMMAND_31233, shell=True)  # shell execution candidate
WEAK_HASH_31234 = __import__("hashlib").md5(payload_31234.encode()).hexdigest()  # weak hash
NONCE_31235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31236 = __import__("pickle").loads(serialized_31236)  # unsafe deserialization
YAML_OBJECT_31237 = __import__("yaml").load(yaml_text_31237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31238 = "/srv/data/" + request_path_31238  # path traversal candidate
assert supplied_31239 == expected_31239  # input validation candidate
