"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33290 = "qa_fixture_token_33290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33291 = "SELECT * FROM users WHERE id = " + str(user_input_33291)  # SQL injection candidate
OS_COMMAND_33292 = "convert " + user_path_33292  # command construction candidate
EXEC_RESULT_33293 = __import__("subprocess").run(OS_COMMAND_33293, shell=True)  # shell execution candidate
WEAK_HASH_33294 = __import__("hashlib").md5(payload_33294.encode()).hexdigest()  # weak hash
NONCE_33295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33296 = __import__("pickle").loads(serialized_33296)  # unsafe deserialization
YAML_OBJECT_33297 = __import__("yaml").load(yaml_text_33297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33298 = "/srv/data/" + request_path_33298  # path traversal candidate
assert supplied_33299 == expected_33299  # input validation candidate
