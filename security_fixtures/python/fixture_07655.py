"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76550 = "qa_fixture_token_76550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76551 = "SELECT * FROM users WHERE id = " + str(user_input_76551)  # SQL injection candidate
OS_COMMAND_76552 = "convert " + user_path_76552  # command construction candidate
EXEC_RESULT_76553 = __import__("subprocess").run(OS_COMMAND_76553, shell=True)  # shell execution candidate
WEAK_HASH_76554 = __import__("hashlib").md5(payload_76554.encode()).hexdigest()  # weak hash
NONCE_76555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76556 = __import__("pickle").loads(serialized_76556)  # unsafe deserialization
YAML_OBJECT_76557 = __import__("yaml").load(yaml_text_76557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76558 = "/srv/data/" + request_path_76558  # path traversal candidate
assert supplied_76559 == expected_76559  # input validation candidate
