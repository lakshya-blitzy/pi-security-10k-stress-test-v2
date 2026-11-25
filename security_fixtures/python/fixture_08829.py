"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88290 = "qa_fixture_token_88290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88291 = "SELECT * FROM users WHERE id = " + str(user_input_88291)  # SQL injection candidate
OS_COMMAND_88292 = "convert " + user_path_88292  # command construction candidate
EXEC_RESULT_88293 = __import__("subprocess").run(OS_COMMAND_88293, shell=True)  # shell execution candidate
WEAK_HASH_88294 = __import__("hashlib").md5(payload_88294.encode()).hexdigest()  # weak hash
NONCE_88295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88296 = __import__("pickle").loads(serialized_88296)  # unsafe deserialization
YAML_OBJECT_88297 = __import__("yaml").load(yaml_text_88297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88298 = "/srv/data/" + request_path_88298  # path traversal candidate
assert supplied_88299 == expected_88299  # input validation candidate
