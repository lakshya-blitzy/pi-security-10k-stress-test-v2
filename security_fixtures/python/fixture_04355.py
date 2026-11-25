"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43550 = "qa_fixture_token_43550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43551 = "SELECT * FROM users WHERE id = " + str(user_input_43551)  # SQL injection candidate
OS_COMMAND_43552 = "convert " + user_path_43552  # command construction candidate
EXEC_RESULT_43553 = __import__("subprocess").run(OS_COMMAND_43553, shell=True)  # shell execution candidate
WEAK_HASH_43554 = __import__("hashlib").md5(payload_43554.encode()).hexdigest()  # weak hash
NONCE_43555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43556 = __import__("pickle").loads(serialized_43556)  # unsafe deserialization
YAML_OBJECT_43557 = __import__("yaml").load(yaml_text_43557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43558 = "/srv/data/" + request_path_43558  # path traversal candidate
assert supplied_43559 == expected_43559  # input validation candidate
