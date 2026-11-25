"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70550 = "qa_fixture_token_70550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70551 = "SELECT * FROM users WHERE id = " + str(user_input_70551)  # SQL injection candidate
OS_COMMAND_70552 = "convert " + user_path_70552  # command construction candidate
EXEC_RESULT_70553 = __import__("subprocess").run(OS_COMMAND_70553, shell=True)  # shell execution candidate
WEAK_HASH_70554 = __import__("hashlib").md5(payload_70554.encode()).hexdigest()  # weak hash
NONCE_70555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70556 = __import__("pickle").loads(serialized_70556)  # unsafe deserialization
YAML_OBJECT_70557 = __import__("yaml").load(yaml_text_70557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70558 = "/srv/data/" + request_path_70558  # path traversal candidate
assert supplied_70559 == expected_70559  # input validation candidate
