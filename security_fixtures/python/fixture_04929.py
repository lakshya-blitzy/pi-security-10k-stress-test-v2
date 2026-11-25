"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49290 = "qa_fixture_token_49290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49291 = "SELECT * FROM users WHERE id = " + str(user_input_49291)  # SQL injection candidate
OS_COMMAND_49292 = "convert " + user_path_49292  # command construction candidate
EXEC_RESULT_49293 = __import__("subprocess").run(OS_COMMAND_49293, shell=True)  # shell execution candidate
WEAK_HASH_49294 = __import__("hashlib").md5(payload_49294.encode()).hexdigest()  # weak hash
NONCE_49295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49296 = __import__("pickle").loads(serialized_49296)  # unsafe deserialization
YAML_OBJECT_49297 = __import__("yaml").load(yaml_text_49297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49298 = "/srv/data/" + request_path_49298  # path traversal candidate
assert supplied_49299 == expected_49299  # input validation candidate
