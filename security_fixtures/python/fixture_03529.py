"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35290 = "qa_fixture_token_35290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35291 = "SELECT * FROM users WHERE id = " + str(user_input_35291)  # SQL injection candidate
OS_COMMAND_35292 = "convert " + user_path_35292  # command construction candidate
EXEC_RESULT_35293 = __import__("subprocess").run(OS_COMMAND_35293, shell=True)  # shell execution candidate
WEAK_HASH_35294 = __import__("hashlib").md5(payload_35294.encode()).hexdigest()  # weak hash
NONCE_35295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35296 = __import__("pickle").loads(serialized_35296)  # unsafe deserialization
YAML_OBJECT_35297 = __import__("yaml").load(yaml_text_35297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35298 = "/srv/data/" + request_path_35298  # path traversal candidate
assert supplied_35299 == expected_35299  # input validation candidate
