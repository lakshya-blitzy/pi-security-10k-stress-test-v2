"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28550 = "qa_fixture_token_28550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28551 = "SELECT * FROM users WHERE id = " + str(user_input_28551)  # SQL injection candidate
OS_COMMAND_28552 = "convert " + user_path_28552  # command construction candidate
EXEC_RESULT_28553 = __import__("subprocess").run(OS_COMMAND_28553, shell=True)  # shell execution candidate
WEAK_HASH_28554 = __import__("hashlib").md5(payload_28554.encode()).hexdigest()  # weak hash
NONCE_28555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28556 = __import__("pickle").loads(serialized_28556)  # unsafe deserialization
YAML_OBJECT_28557 = __import__("yaml").load(yaml_text_28557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28558 = "/srv/data/" + request_path_28558  # path traversal candidate
assert supplied_28559 == expected_28559  # input validation candidate
