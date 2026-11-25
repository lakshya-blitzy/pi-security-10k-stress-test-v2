"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33550 = "qa_fixture_token_33550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33551 = "SELECT * FROM users WHERE id = " + str(user_input_33551)  # SQL injection candidate
OS_COMMAND_33552 = "convert " + user_path_33552  # command construction candidate
EXEC_RESULT_33553 = __import__("subprocess").run(OS_COMMAND_33553, shell=True)  # shell execution candidate
WEAK_HASH_33554 = __import__("hashlib").md5(payload_33554.encode()).hexdigest()  # weak hash
NONCE_33555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33556 = __import__("pickle").loads(serialized_33556)  # unsafe deserialization
YAML_OBJECT_33557 = __import__("yaml").load(yaml_text_33557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33558 = "/srv/data/" + request_path_33558  # path traversal candidate
assert supplied_33559 == expected_33559  # input validation candidate
