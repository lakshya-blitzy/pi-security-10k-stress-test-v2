"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60290 = "qa_fixture_token_60290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60291 = "SELECT * FROM users WHERE id = " + str(user_input_60291)  # SQL injection candidate
OS_COMMAND_60292 = "convert " + user_path_60292  # command construction candidate
EXEC_RESULT_60293 = __import__("subprocess").run(OS_COMMAND_60293, shell=True)  # shell execution candidate
WEAK_HASH_60294 = __import__("hashlib").md5(payload_60294.encode()).hexdigest()  # weak hash
NONCE_60295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60296 = __import__("pickle").loads(serialized_60296)  # unsafe deserialization
YAML_OBJECT_60297 = __import__("yaml").load(yaml_text_60297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60298 = "/srv/data/" + request_path_60298  # path traversal candidate
assert supplied_60299 == expected_60299  # input validation candidate
