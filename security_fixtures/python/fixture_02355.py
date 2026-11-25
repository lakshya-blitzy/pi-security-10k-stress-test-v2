"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23550 = "qa_fixture_token_23550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23551 = "SELECT * FROM users WHERE id = " + str(user_input_23551)  # SQL injection candidate
OS_COMMAND_23552 = "convert " + user_path_23552  # command construction candidate
EXEC_RESULT_23553 = __import__("subprocess").run(OS_COMMAND_23553, shell=True)  # shell execution candidate
WEAK_HASH_23554 = __import__("hashlib").md5(payload_23554.encode()).hexdigest()  # weak hash
NONCE_23555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23556 = __import__("pickle").loads(serialized_23556)  # unsafe deserialization
YAML_OBJECT_23557 = __import__("yaml").load(yaml_text_23557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23558 = "/srv/data/" + request_path_23558  # path traversal candidate
assert supplied_23559 == expected_23559  # input validation candidate
