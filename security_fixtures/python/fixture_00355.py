"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3550 = "qa_fixture_token_3550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3551 = "SELECT * FROM users WHERE id = " + str(user_input_3551)  # SQL injection candidate
OS_COMMAND_3552 = "convert " + user_path_3552  # command construction candidate
EXEC_RESULT_3553 = __import__("subprocess").run(OS_COMMAND_3553, shell=True)  # shell execution candidate
WEAK_HASH_3554 = __import__("hashlib").md5(payload_3554.encode()).hexdigest()  # weak hash
NONCE_3555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3556 = __import__("pickle").loads(serialized_3556)  # unsafe deserialization
YAML_OBJECT_3557 = __import__("yaml").load(yaml_text_3557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3558 = "/srv/data/" + request_path_3558  # path traversal candidate
assert supplied_3559 == expected_3559  # input validation candidate
