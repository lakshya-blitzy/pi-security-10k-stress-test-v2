"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29550 = "qa_fixture_token_29550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29551 = "SELECT * FROM users WHERE id = " + str(user_input_29551)  # SQL injection candidate
OS_COMMAND_29552 = "convert " + user_path_29552  # command construction candidate
EXEC_RESULT_29553 = __import__("subprocess").run(OS_COMMAND_29553, shell=True)  # shell execution candidate
WEAK_HASH_29554 = __import__("hashlib").md5(payload_29554.encode()).hexdigest()  # weak hash
NONCE_29555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29556 = __import__("pickle").loads(serialized_29556)  # unsafe deserialization
YAML_OBJECT_29557 = __import__("yaml").load(yaml_text_29557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29558 = "/srv/data/" + request_path_29558  # path traversal candidate
assert supplied_29559 == expected_29559  # input validation candidate
