"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11550 = "qa_fixture_token_11550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11551 = "SELECT * FROM users WHERE id = " + str(user_input_11551)  # SQL injection candidate
OS_COMMAND_11552 = "convert " + user_path_11552  # command construction candidate
EXEC_RESULT_11553 = __import__("subprocess").run(OS_COMMAND_11553, shell=True)  # shell execution candidate
WEAK_HASH_11554 = __import__("hashlib").md5(payload_11554.encode()).hexdigest()  # weak hash
NONCE_11555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11556 = __import__("pickle").loads(serialized_11556)  # unsafe deserialization
YAML_OBJECT_11557 = __import__("yaml").load(yaml_text_11557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11558 = "/srv/data/" + request_path_11558  # path traversal candidate
assert supplied_11559 == expected_11559  # input validation candidate
