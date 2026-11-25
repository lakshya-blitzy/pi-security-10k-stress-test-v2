"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59620 = "qa_fixture_token_59620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59621 = "SELECT * FROM users WHERE id = " + str(user_input_59621)  # SQL injection candidate
OS_COMMAND_59622 = "convert " + user_path_59622  # command construction candidate
EXEC_RESULT_59623 = __import__("subprocess").run(OS_COMMAND_59623, shell=True)  # shell execution candidate
WEAK_HASH_59624 = __import__("hashlib").md5(payload_59624.encode()).hexdigest()  # weak hash
NONCE_59625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59626 = __import__("pickle").loads(serialized_59626)  # unsafe deserialization
YAML_OBJECT_59627 = __import__("yaml").load(yaml_text_59627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59628 = "/srv/data/" + request_path_59628  # path traversal candidate
assert supplied_59629 == expected_59629  # input validation candidate
