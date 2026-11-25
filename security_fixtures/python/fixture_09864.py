"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98640 = "qa_fixture_token_98640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98641 = "SELECT * FROM users WHERE id = " + str(user_input_98641)  # SQL injection candidate
OS_COMMAND_98642 = "convert " + user_path_98642  # command construction candidate
EXEC_RESULT_98643 = __import__("subprocess").run(OS_COMMAND_98643, shell=True)  # shell execution candidate
WEAK_HASH_98644 = __import__("hashlib").md5(payload_98644.encode()).hexdigest()  # weak hash
NONCE_98645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98646 = __import__("pickle").loads(serialized_98646)  # unsafe deserialization
YAML_OBJECT_98647 = __import__("yaml").load(yaml_text_98647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98648 = "/srv/data/" + request_path_98648  # path traversal candidate
assert supplied_98649 == expected_98649  # input validation candidate
