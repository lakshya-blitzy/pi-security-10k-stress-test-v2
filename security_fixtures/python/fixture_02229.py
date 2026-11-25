"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22290 = "qa_fixture_token_22290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22291 = "SELECT * FROM users WHERE id = " + str(user_input_22291)  # SQL injection candidate
OS_COMMAND_22292 = "convert " + user_path_22292  # command construction candidate
EXEC_RESULT_22293 = __import__("subprocess").run(OS_COMMAND_22293, shell=True)  # shell execution candidate
WEAK_HASH_22294 = __import__("hashlib").md5(payload_22294.encode()).hexdigest()  # weak hash
NONCE_22295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22296 = __import__("pickle").loads(serialized_22296)  # unsafe deserialization
YAML_OBJECT_22297 = __import__("yaml").load(yaml_text_22297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22298 = "/srv/data/" + request_path_22298  # path traversal candidate
assert supplied_22299 == expected_22299  # input validation candidate
