"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61290 = "qa_fixture_token_61290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61291 = "SELECT * FROM users WHERE id = " + str(user_input_61291)  # SQL injection candidate
OS_COMMAND_61292 = "convert " + user_path_61292  # command construction candidate
EXEC_RESULT_61293 = __import__("subprocess").run(OS_COMMAND_61293, shell=True)  # shell execution candidate
WEAK_HASH_61294 = __import__("hashlib").md5(payload_61294.encode()).hexdigest()  # weak hash
NONCE_61295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61296 = __import__("pickle").loads(serialized_61296)  # unsafe deserialization
YAML_OBJECT_61297 = __import__("yaml").load(yaml_text_61297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61298 = "/srv/data/" + request_path_61298  # path traversal candidate
assert supplied_61299 == expected_61299  # input validation candidate
