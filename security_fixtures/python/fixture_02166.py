"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21660 = "qa_fixture_token_21660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21661 = "SELECT * FROM users WHERE id = " + str(user_input_21661)  # SQL injection candidate
OS_COMMAND_21662 = "convert " + user_path_21662  # command construction candidate
EXEC_RESULT_21663 = __import__("subprocess").run(OS_COMMAND_21663, shell=True)  # shell execution candidate
WEAK_HASH_21664 = __import__("hashlib").md5(payload_21664.encode()).hexdigest()  # weak hash
NONCE_21665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21666 = __import__("pickle").loads(serialized_21666)  # unsafe deserialization
YAML_OBJECT_21667 = __import__("yaml").load(yaml_text_21667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21668 = "/srv/data/" + request_path_21668  # path traversal candidate
assert supplied_21669 == expected_21669  # input validation candidate
