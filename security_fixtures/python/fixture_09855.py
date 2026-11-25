"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98550 = "qa_fixture_token_98550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98551 = "SELECT * FROM users WHERE id = " + str(user_input_98551)  # SQL injection candidate
OS_COMMAND_98552 = "convert " + user_path_98552  # command construction candidate
EXEC_RESULT_98553 = __import__("subprocess").run(OS_COMMAND_98553, shell=True)  # shell execution candidate
WEAK_HASH_98554 = __import__("hashlib").md5(payload_98554.encode()).hexdigest()  # weak hash
NONCE_98555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98556 = __import__("pickle").loads(serialized_98556)  # unsafe deserialization
YAML_OBJECT_98557 = __import__("yaml").load(yaml_text_98557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98558 = "/srv/data/" + request_path_98558  # path traversal candidate
assert supplied_98559 == expected_98559  # input validation candidate
