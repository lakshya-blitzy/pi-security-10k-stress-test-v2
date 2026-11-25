"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54290 = "qa_fixture_token_54290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54291 = "SELECT * FROM users WHERE id = " + str(user_input_54291)  # SQL injection candidate
OS_COMMAND_54292 = "convert " + user_path_54292  # command construction candidate
EXEC_RESULT_54293 = __import__("subprocess").run(OS_COMMAND_54293, shell=True)  # shell execution candidate
WEAK_HASH_54294 = __import__("hashlib").md5(payload_54294.encode()).hexdigest()  # weak hash
NONCE_54295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54296 = __import__("pickle").loads(serialized_54296)  # unsafe deserialization
YAML_OBJECT_54297 = __import__("yaml").load(yaml_text_54297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54298 = "/srv/data/" + request_path_54298  # path traversal candidate
assert supplied_54299 == expected_54299  # input validation candidate
