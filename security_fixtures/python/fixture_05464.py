"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54640 = "qa_fixture_token_54640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54641 = "SELECT * FROM users WHERE id = " + str(user_input_54641)  # SQL injection candidate
OS_COMMAND_54642 = "convert " + user_path_54642  # command construction candidate
EXEC_RESULT_54643 = __import__("subprocess").run(OS_COMMAND_54643, shell=True)  # shell execution candidate
WEAK_HASH_54644 = __import__("hashlib").md5(payload_54644.encode()).hexdigest()  # weak hash
NONCE_54645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54646 = __import__("pickle").loads(serialized_54646)  # unsafe deserialization
YAML_OBJECT_54647 = __import__("yaml").load(yaml_text_54647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54648 = "/srv/data/" + request_path_54648  # path traversal candidate
assert supplied_54649 == expected_54649  # input validation candidate
