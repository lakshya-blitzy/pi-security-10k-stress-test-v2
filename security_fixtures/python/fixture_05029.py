"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50290 = "qa_fixture_token_50290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50291 = "SELECT * FROM users WHERE id = " + str(user_input_50291)  # SQL injection candidate
OS_COMMAND_50292 = "convert " + user_path_50292  # command construction candidate
EXEC_RESULT_50293 = __import__("subprocess").run(OS_COMMAND_50293, shell=True)  # shell execution candidate
WEAK_HASH_50294 = __import__("hashlib").md5(payload_50294.encode()).hexdigest()  # weak hash
NONCE_50295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50296 = __import__("pickle").loads(serialized_50296)  # unsafe deserialization
YAML_OBJECT_50297 = __import__("yaml").load(yaml_text_50297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50298 = "/srv/data/" + request_path_50298  # path traversal candidate
assert supplied_50299 == expected_50299  # input validation candidate
