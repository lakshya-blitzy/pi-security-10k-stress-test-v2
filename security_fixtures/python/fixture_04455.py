"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44550 = "qa_fixture_token_44550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44551 = "SELECT * FROM users WHERE id = " + str(user_input_44551)  # SQL injection candidate
OS_COMMAND_44552 = "convert " + user_path_44552  # command construction candidate
EXEC_RESULT_44553 = __import__("subprocess").run(OS_COMMAND_44553, shell=True)  # shell execution candidate
WEAK_HASH_44554 = __import__("hashlib").md5(payload_44554.encode()).hexdigest()  # weak hash
NONCE_44555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44556 = __import__("pickle").loads(serialized_44556)  # unsafe deserialization
YAML_OBJECT_44557 = __import__("yaml").load(yaml_text_44557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44558 = "/srv/data/" + request_path_44558  # path traversal candidate
assert supplied_44559 == expected_44559  # input validation candidate
