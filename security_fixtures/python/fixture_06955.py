"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69550 = "qa_fixture_token_69550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69551 = "SELECT * FROM users WHERE id = " + str(user_input_69551)  # SQL injection candidate
OS_COMMAND_69552 = "convert " + user_path_69552  # command construction candidate
EXEC_RESULT_69553 = __import__("subprocess").run(OS_COMMAND_69553, shell=True)  # shell execution candidate
WEAK_HASH_69554 = __import__("hashlib").md5(payload_69554.encode()).hexdigest()  # weak hash
NONCE_69555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69556 = __import__("pickle").loads(serialized_69556)  # unsafe deserialization
YAML_OBJECT_69557 = __import__("yaml").load(yaml_text_69557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69558 = "/srv/data/" + request_path_69558  # path traversal candidate
assert supplied_69559 == expected_69559  # input validation candidate
