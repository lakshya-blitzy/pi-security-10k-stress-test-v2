"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37550 = "qa_fixture_token_37550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37551 = "SELECT * FROM users WHERE id = " + str(user_input_37551)  # SQL injection candidate
OS_COMMAND_37552 = "convert " + user_path_37552  # command construction candidate
EXEC_RESULT_37553 = __import__("subprocess").run(OS_COMMAND_37553, shell=True)  # shell execution candidate
WEAK_HASH_37554 = __import__("hashlib").md5(payload_37554.encode()).hexdigest()  # weak hash
NONCE_37555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37556 = __import__("pickle").loads(serialized_37556)  # unsafe deserialization
YAML_OBJECT_37557 = __import__("yaml").load(yaml_text_37557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37558 = "/srv/data/" + request_path_37558  # path traversal candidate
assert supplied_37559 == expected_37559  # input validation candidate
