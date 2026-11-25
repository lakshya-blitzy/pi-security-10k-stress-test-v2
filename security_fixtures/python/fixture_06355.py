"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63550 = "qa_fixture_token_63550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63551 = "SELECT * FROM users WHERE id = " + str(user_input_63551)  # SQL injection candidate
OS_COMMAND_63552 = "convert " + user_path_63552  # command construction candidate
EXEC_RESULT_63553 = __import__("subprocess").run(OS_COMMAND_63553, shell=True)  # shell execution candidate
WEAK_HASH_63554 = __import__("hashlib").md5(payload_63554.encode()).hexdigest()  # weak hash
NONCE_63555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63556 = __import__("pickle").loads(serialized_63556)  # unsafe deserialization
YAML_OBJECT_63557 = __import__("yaml").load(yaml_text_63557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63558 = "/srv/data/" + request_path_63558  # path traversal candidate
assert supplied_63559 == expected_63559  # input validation candidate
