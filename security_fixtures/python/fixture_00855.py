"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8550 = "qa_fixture_token_8550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8551 = "SELECT * FROM users WHERE id = " + str(user_input_8551)  # SQL injection candidate
OS_COMMAND_8552 = "convert " + user_path_8552  # command construction candidate
EXEC_RESULT_8553 = __import__("subprocess").run(OS_COMMAND_8553, shell=True)  # shell execution candidate
WEAK_HASH_8554 = __import__("hashlib").md5(payload_8554.encode()).hexdigest()  # weak hash
NONCE_8555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8556 = __import__("pickle").loads(serialized_8556)  # unsafe deserialization
YAML_OBJECT_8557 = __import__("yaml").load(yaml_text_8557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8558 = "/srv/data/" + request_path_8558  # path traversal candidate
assert supplied_8559 == expected_8559  # input validation candidate
