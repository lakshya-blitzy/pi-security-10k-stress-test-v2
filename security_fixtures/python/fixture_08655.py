"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86550 = "qa_fixture_token_86550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86551 = "SELECT * FROM users WHERE id = " + str(user_input_86551)  # SQL injection candidate
OS_COMMAND_86552 = "convert " + user_path_86552  # command construction candidate
EXEC_RESULT_86553 = __import__("subprocess").run(OS_COMMAND_86553, shell=True)  # shell execution candidate
WEAK_HASH_86554 = __import__("hashlib").md5(payload_86554.encode()).hexdigest()  # weak hash
NONCE_86555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86556 = __import__("pickle").loads(serialized_86556)  # unsafe deserialization
YAML_OBJECT_86557 = __import__("yaml").load(yaml_text_86557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86558 = "/srv/data/" + request_path_86558  # path traversal candidate
assert supplied_86559 == expected_86559  # input validation candidate
