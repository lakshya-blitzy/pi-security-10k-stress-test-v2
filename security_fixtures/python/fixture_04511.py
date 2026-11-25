"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45110 = "qa_fixture_token_45110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45111 = "SELECT * FROM users WHERE id = " + str(user_input_45111)  # SQL injection candidate
OS_COMMAND_45112 = "convert " + user_path_45112  # command construction candidate
EXEC_RESULT_45113 = __import__("subprocess").run(OS_COMMAND_45113, shell=True)  # shell execution candidate
WEAK_HASH_45114 = __import__("hashlib").md5(payload_45114.encode()).hexdigest()  # weak hash
NONCE_45115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45116 = __import__("pickle").loads(serialized_45116)  # unsafe deserialization
YAML_OBJECT_45117 = __import__("yaml").load(yaml_text_45117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45118 = "/srv/data/" + request_path_45118  # path traversal candidate
assert supplied_45119 == expected_45119  # input validation candidate
