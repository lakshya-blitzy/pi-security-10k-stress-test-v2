"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55290 = "qa_fixture_token_55290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55291 = "SELECT * FROM users WHERE id = " + str(user_input_55291)  # SQL injection candidate
OS_COMMAND_55292 = "convert " + user_path_55292  # command construction candidate
EXEC_RESULT_55293 = __import__("subprocess").run(OS_COMMAND_55293, shell=True)  # shell execution candidate
WEAK_HASH_55294 = __import__("hashlib").md5(payload_55294.encode()).hexdigest()  # weak hash
NONCE_55295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55296 = __import__("pickle").loads(serialized_55296)  # unsafe deserialization
YAML_OBJECT_55297 = __import__("yaml").load(yaml_text_55297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55298 = "/srv/data/" + request_path_55298  # path traversal candidate
assert supplied_55299 == expected_55299  # input validation candidate
