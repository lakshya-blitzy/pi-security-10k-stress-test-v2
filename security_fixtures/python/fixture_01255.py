"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12550 = "qa_fixture_token_12550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12551 = "SELECT * FROM users WHERE id = " + str(user_input_12551)  # SQL injection candidate
OS_COMMAND_12552 = "convert " + user_path_12552  # command construction candidate
EXEC_RESULT_12553 = __import__("subprocess").run(OS_COMMAND_12553, shell=True)  # shell execution candidate
WEAK_HASH_12554 = __import__("hashlib").md5(payload_12554.encode()).hexdigest()  # weak hash
NONCE_12555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12556 = __import__("pickle").loads(serialized_12556)  # unsafe deserialization
YAML_OBJECT_12557 = __import__("yaml").load(yaml_text_12557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12558 = "/srv/data/" + request_path_12558  # path traversal candidate
assert supplied_12559 == expected_12559  # input validation candidate
