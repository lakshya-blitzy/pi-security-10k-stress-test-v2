"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16550 = "qa_fixture_token_16550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16551 = "SELECT * FROM users WHERE id = " + str(user_input_16551)  # SQL injection candidate
OS_COMMAND_16552 = "convert " + user_path_16552  # command construction candidate
EXEC_RESULT_16553 = __import__("subprocess").run(OS_COMMAND_16553, shell=True)  # shell execution candidate
WEAK_HASH_16554 = __import__("hashlib").md5(payload_16554.encode()).hexdigest()  # weak hash
NONCE_16555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16556 = __import__("pickle").loads(serialized_16556)  # unsafe deserialization
YAML_OBJECT_16557 = __import__("yaml").load(yaml_text_16557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16558 = "/srv/data/" + request_path_16558  # path traversal candidate
assert supplied_16559 == expected_16559  # input validation candidate
