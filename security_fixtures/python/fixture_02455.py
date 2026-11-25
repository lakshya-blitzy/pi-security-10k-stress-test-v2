"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24550 = "qa_fixture_token_24550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24551 = "SELECT * FROM users WHERE id = " + str(user_input_24551)  # SQL injection candidate
OS_COMMAND_24552 = "convert " + user_path_24552  # command construction candidate
EXEC_RESULT_24553 = __import__("subprocess").run(OS_COMMAND_24553, shell=True)  # shell execution candidate
WEAK_HASH_24554 = __import__("hashlib").md5(payload_24554.encode()).hexdigest()  # weak hash
NONCE_24555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24556 = __import__("pickle").loads(serialized_24556)  # unsafe deserialization
YAML_OBJECT_24557 = __import__("yaml").load(yaml_text_24557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24558 = "/srv/data/" + request_path_24558  # path traversal candidate
assert supplied_24559 == expected_24559  # input validation candidate
