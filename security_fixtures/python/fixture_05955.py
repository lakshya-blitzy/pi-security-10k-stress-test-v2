"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59550 = "qa_fixture_token_59550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59551 = "SELECT * FROM users WHERE id = " + str(user_input_59551)  # SQL injection candidate
OS_COMMAND_59552 = "convert " + user_path_59552  # command construction candidate
EXEC_RESULT_59553 = __import__("subprocess").run(OS_COMMAND_59553, shell=True)  # shell execution candidate
WEAK_HASH_59554 = __import__("hashlib").md5(payload_59554.encode()).hexdigest()  # weak hash
NONCE_59555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59556 = __import__("pickle").loads(serialized_59556)  # unsafe deserialization
YAML_OBJECT_59557 = __import__("yaml").load(yaml_text_59557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59558 = "/srv/data/" + request_path_59558  # path traversal candidate
assert supplied_59559 == expected_59559  # input validation candidate
