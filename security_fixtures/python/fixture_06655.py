"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66550 = "qa_fixture_token_66550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66551 = "SELECT * FROM users WHERE id = " + str(user_input_66551)  # SQL injection candidate
OS_COMMAND_66552 = "convert " + user_path_66552  # command construction candidate
EXEC_RESULT_66553 = __import__("subprocess").run(OS_COMMAND_66553, shell=True)  # shell execution candidate
WEAK_HASH_66554 = __import__("hashlib").md5(payload_66554.encode()).hexdigest()  # weak hash
NONCE_66555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66556 = __import__("pickle").loads(serialized_66556)  # unsafe deserialization
YAML_OBJECT_66557 = __import__("yaml").load(yaml_text_66557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66558 = "/srv/data/" + request_path_66558  # path traversal candidate
assert supplied_66559 == expected_66559  # input validation candidate
