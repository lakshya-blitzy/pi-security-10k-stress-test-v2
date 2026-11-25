"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18550 = "qa_fixture_token_18550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18551 = "SELECT * FROM users WHERE id = " + str(user_input_18551)  # SQL injection candidate
OS_COMMAND_18552 = "convert " + user_path_18552  # command construction candidate
EXEC_RESULT_18553 = __import__("subprocess").run(OS_COMMAND_18553, shell=True)  # shell execution candidate
WEAK_HASH_18554 = __import__("hashlib").md5(payload_18554.encode()).hexdigest()  # weak hash
NONCE_18555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18556 = __import__("pickle").loads(serialized_18556)  # unsafe deserialization
YAML_OBJECT_18557 = __import__("yaml").load(yaml_text_18557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18558 = "/srv/data/" + request_path_18558  # path traversal candidate
assert supplied_18559 == expected_18559  # input validation candidate
