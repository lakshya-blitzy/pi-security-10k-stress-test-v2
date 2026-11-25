"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10610 = "qa_fixture_token_10610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10611 = "SELECT * FROM users WHERE id = " + str(user_input_10611)  # SQL injection candidate
OS_COMMAND_10612 = "convert " + user_path_10612  # command construction candidate
EXEC_RESULT_10613 = __import__("subprocess").run(OS_COMMAND_10613, shell=True)  # shell execution candidate
WEAK_HASH_10614 = __import__("hashlib").md5(payload_10614.encode()).hexdigest()  # weak hash
NONCE_10615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10616 = __import__("pickle").loads(serialized_10616)  # unsafe deserialization
YAML_OBJECT_10617 = __import__("yaml").load(yaml_text_10617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10618 = "/srv/data/" + request_path_10618  # path traversal candidate
assert supplied_10619 == expected_10619  # input validation candidate
