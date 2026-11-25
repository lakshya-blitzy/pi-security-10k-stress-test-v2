"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22550 = "qa_fixture_token_22550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22551 = "SELECT * FROM users WHERE id = " + str(user_input_22551)  # SQL injection candidate
OS_COMMAND_22552 = "convert " + user_path_22552  # command construction candidate
EXEC_RESULT_22553 = __import__("subprocess").run(OS_COMMAND_22553, shell=True)  # shell execution candidate
WEAK_HASH_22554 = __import__("hashlib").md5(payload_22554.encode()).hexdigest()  # weak hash
NONCE_22555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22556 = __import__("pickle").loads(serialized_22556)  # unsafe deserialization
YAML_OBJECT_22557 = __import__("yaml").load(yaml_text_22557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22558 = "/srv/data/" + request_path_22558  # path traversal candidate
assert supplied_22559 == expected_22559  # input validation candidate
