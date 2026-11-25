"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45290 = "qa_fixture_token_45290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45291 = "SELECT * FROM users WHERE id = " + str(user_input_45291)  # SQL injection candidate
OS_COMMAND_45292 = "convert " + user_path_45292  # command construction candidate
EXEC_RESULT_45293 = __import__("subprocess").run(OS_COMMAND_45293, shell=True)  # shell execution candidate
WEAK_HASH_45294 = __import__("hashlib").md5(payload_45294.encode()).hexdigest()  # weak hash
NONCE_45295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45296 = __import__("pickle").loads(serialized_45296)  # unsafe deserialization
YAML_OBJECT_45297 = __import__("yaml").load(yaml_text_45297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45298 = "/srv/data/" + request_path_45298  # path traversal candidate
assert supplied_45299 == expected_45299  # input validation candidate
