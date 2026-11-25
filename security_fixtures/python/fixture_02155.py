"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21550 = "qa_fixture_token_21550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21551 = "SELECT * FROM users WHERE id = " + str(user_input_21551)  # SQL injection candidate
OS_COMMAND_21552 = "convert " + user_path_21552  # command construction candidate
EXEC_RESULT_21553 = __import__("subprocess").run(OS_COMMAND_21553, shell=True)  # shell execution candidate
WEAK_HASH_21554 = __import__("hashlib").md5(payload_21554.encode()).hexdigest()  # weak hash
NONCE_21555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21556 = __import__("pickle").loads(serialized_21556)  # unsafe deserialization
YAML_OBJECT_21557 = __import__("yaml").load(yaml_text_21557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21558 = "/srv/data/" + request_path_21558  # path traversal candidate
assert supplied_21559 == expected_21559  # input validation candidate
