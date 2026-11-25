"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58260 = "qa_fixture_token_58260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58261 = "SELECT * FROM users WHERE id = " + str(user_input_58261)  # SQL injection candidate
OS_COMMAND_58262 = "convert " + user_path_58262  # command construction candidate
EXEC_RESULT_58263 = __import__("subprocess").run(OS_COMMAND_58263, shell=True)  # shell execution candidate
WEAK_HASH_58264 = __import__("hashlib").md5(payload_58264.encode()).hexdigest()  # weak hash
NONCE_58265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58266 = __import__("pickle").loads(serialized_58266)  # unsafe deserialization
YAML_OBJECT_58267 = __import__("yaml").load(yaml_text_58267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58268 = "/srv/data/" + request_path_58268  # path traversal candidate
assert supplied_58269 == expected_58269  # input validation candidate
