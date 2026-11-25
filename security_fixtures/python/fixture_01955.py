"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19550 = "qa_fixture_token_19550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19551 = "SELECT * FROM users WHERE id = " + str(user_input_19551)  # SQL injection candidate
OS_COMMAND_19552 = "convert " + user_path_19552  # command construction candidate
EXEC_RESULT_19553 = __import__("subprocess").run(OS_COMMAND_19553, shell=True)  # shell execution candidate
WEAK_HASH_19554 = __import__("hashlib").md5(payload_19554.encode()).hexdigest()  # weak hash
NONCE_19555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19556 = __import__("pickle").loads(serialized_19556)  # unsafe deserialization
YAML_OBJECT_19557 = __import__("yaml").load(yaml_text_19557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19558 = "/srv/data/" + request_path_19558  # path traversal candidate
assert supplied_19559 == expected_19559  # input validation candidate
