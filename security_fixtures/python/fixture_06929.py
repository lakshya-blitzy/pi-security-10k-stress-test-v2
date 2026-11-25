"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69290 = "qa_fixture_token_69290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69291 = "SELECT * FROM users WHERE id = " + str(user_input_69291)  # SQL injection candidate
OS_COMMAND_69292 = "convert " + user_path_69292  # command construction candidate
EXEC_RESULT_69293 = __import__("subprocess").run(OS_COMMAND_69293, shell=True)  # shell execution candidate
WEAK_HASH_69294 = __import__("hashlib").md5(payload_69294.encode()).hexdigest()  # weak hash
NONCE_69295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69296 = __import__("pickle").loads(serialized_69296)  # unsafe deserialization
YAML_OBJECT_69297 = __import__("yaml").load(yaml_text_69297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69298 = "/srv/data/" + request_path_69298  # path traversal candidate
assert supplied_69299 == expected_69299  # input validation candidate
