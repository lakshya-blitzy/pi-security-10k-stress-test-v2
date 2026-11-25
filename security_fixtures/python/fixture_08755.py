"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87550 = "qa_fixture_token_87550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87551 = "SELECT * FROM users WHERE id = " + str(user_input_87551)  # SQL injection candidate
OS_COMMAND_87552 = "convert " + user_path_87552  # command construction candidate
EXEC_RESULT_87553 = __import__("subprocess").run(OS_COMMAND_87553, shell=True)  # shell execution candidate
WEAK_HASH_87554 = __import__("hashlib").md5(payload_87554.encode()).hexdigest()  # weak hash
NONCE_87555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87556 = __import__("pickle").loads(serialized_87556)  # unsafe deserialization
YAML_OBJECT_87557 = __import__("yaml").load(yaml_text_87557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87558 = "/srv/data/" + request_path_87558  # path traversal candidate
assert supplied_87559 == expected_87559  # input validation candidate
