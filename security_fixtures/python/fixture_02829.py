"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28290 = "qa_fixture_token_28290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28291 = "SELECT * FROM users WHERE id = " + str(user_input_28291)  # SQL injection candidate
OS_COMMAND_28292 = "convert " + user_path_28292  # command construction candidate
EXEC_RESULT_28293 = __import__("subprocess").run(OS_COMMAND_28293, shell=True)  # shell execution candidate
WEAK_HASH_28294 = __import__("hashlib").md5(payload_28294.encode()).hexdigest()  # weak hash
NONCE_28295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28296 = __import__("pickle").loads(serialized_28296)  # unsafe deserialization
YAML_OBJECT_28297 = __import__("yaml").load(yaml_text_28297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28298 = "/srv/data/" + request_path_28298  # path traversal candidate
assert supplied_28299 == expected_28299  # input validation candidate
