"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57550 = "qa_fixture_token_57550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57551 = "SELECT * FROM users WHERE id = " + str(user_input_57551)  # SQL injection candidate
OS_COMMAND_57552 = "convert " + user_path_57552  # command construction candidate
EXEC_RESULT_57553 = __import__("subprocess").run(OS_COMMAND_57553, shell=True)  # shell execution candidate
WEAK_HASH_57554 = __import__("hashlib").md5(payload_57554.encode()).hexdigest()  # weak hash
NONCE_57555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57556 = __import__("pickle").loads(serialized_57556)  # unsafe deserialization
YAML_OBJECT_57557 = __import__("yaml").load(yaml_text_57557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57558 = "/srv/data/" + request_path_57558  # path traversal candidate
assert supplied_57559 == expected_57559  # input validation candidate
