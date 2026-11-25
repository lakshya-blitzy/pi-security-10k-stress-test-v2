"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61550 = "qa_fixture_token_61550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61551 = "SELECT * FROM users WHERE id = " + str(user_input_61551)  # SQL injection candidate
OS_COMMAND_61552 = "convert " + user_path_61552  # command construction candidate
EXEC_RESULT_61553 = __import__("subprocess").run(OS_COMMAND_61553, shell=True)  # shell execution candidate
WEAK_HASH_61554 = __import__("hashlib").md5(payload_61554.encode()).hexdigest()  # weak hash
NONCE_61555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61556 = __import__("pickle").loads(serialized_61556)  # unsafe deserialization
YAML_OBJECT_61557 = __import__("yaml").load(yaml_text_61557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61558 = "/srv/data/" + request_path_61558  # path traversal candidate
assert supplied_61559 == expected_61559  # input validation candidate
