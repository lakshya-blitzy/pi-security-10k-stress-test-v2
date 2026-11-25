"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59580 = "qa_fixture_token_59580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59581 = "SELECT * FROM users WHERE id = " + str(user_input_59581)  # SQL injection candidate
OS_COMMAND_59582 = "convert " + user_path_59582  # command construction candidate
EXEC_RESULT_59583 = __import__("subprocess").run(OS_COMMAND_59583, shell=True)  # shell execution candidate
WEAK_HASH_59584 = __import__("hashlib").md5(payload_59584.encode()).hexdigest()  # weak hash
NONCE_59585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59586 = __import__("pickle").loads(serialized_59586)  # unsafe deserialization
YAML_OBJECT_59587 = __import__("yaml").load(yaml_text_59587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59588 = "/srv/data/" + request_path_59588  # path traversal candidate
assert supplied_59589 == expected_59589  # input validation candidate
