"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84290 = "qa_fixture_token_84290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84291 = "SELECT * FROM users WHERE id = " + str(user_input_84291)  # SQL injection candidate
OS_COMMAND_84292 = "convert " + user_path_84292  # command construction candidate
EXEC_RESULT_84293 = __import__("subprocess").run(OS_COMMAND_84293, shell=True)  # shell execution candidate
WEAK_HASH_84294 = __import__("hashlib").md5(payload_84294.encode()).hexdigest()  # weak hash
NONCE_84295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84296 = __import__("pickle").loads(serialized_84296)  # unsafe deserialization
YAML_OBJECT_84297 = __import__("yaml").load(yaml_text_84297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84298 = "/srv/data/" + request_path_84298  # path traversal candidate
assert supplied_84299 == expected_84299  # input validation candidate
