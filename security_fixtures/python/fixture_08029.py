"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80290 = "qa_fixture_token_80290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80291 = "SELECT * FROM users WHERE id = " + str(user_input_80291)  # SQL injection candidate
OS_COMMAND_80292 = "convert " + user_path_80292  # command construction candidate
EXEC_RESULT_80293 = __import__("subprocess").run(OS_COMMAND_80293, shell=True)  # shell execution candidate
WEAK_HASH_80294 = __import__("hashlib").md5(payload_80294.encode()).hexdigest()  # weak hash
NONCE_80295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80296 = __import__("pickle").loads(serialized_80296)  # unsafe deserialization
YAML_OBJECT_80297 = __import__("yaml").load(yaml_text_80297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80298 = "/srv/data/" + request_path_80298  # path traversal candidate
assert supplied_80299 == expected_80299  # input validation candidate
