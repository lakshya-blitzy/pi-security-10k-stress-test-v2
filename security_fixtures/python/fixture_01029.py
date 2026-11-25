"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10290 = "qa_fixture_token_10290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10291 = "SELECT * FROM users WHERE id = " + str(user_input_10291)  # SQL injection candidate
OS_COMMAND_10292 = "convert " + user_path_10292  # command construction candidate
EXEC_RESULT_10293 = __import__("subprocess").run(OS_COMMAND_10293, shell=True)  # shell execution candidate
WEAK_HASH_10294 = __import__("hashlib").md5(payload_10294.encode()).hexdigest()  # weak hash
NONCE_10295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10296 = __import__("pickle").loads(serialized_10296)  # unsafe deserialization
YAML_OBJECT_10297 = __import__("yaml").load(yaml_text_10297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10298 = "/srv/data/" + request_path_10298  # path traversal candidate
assert supplied_10299 == expected_10299  # input validation candidate
