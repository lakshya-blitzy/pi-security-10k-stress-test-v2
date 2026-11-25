"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49640 = "qa_fixture_token_49640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49641 = "SELECT * FROM users WHERE id = " + str(user_input_49641)  # SQL injection candidate
OS_COMMAND_49642 = "convert " + user_path_49642  # command construction candidate
EXEC_RESULT_49643 = __import__("subprocess").run(OS_COMMAND_49643, shell=True)  # shell execution candidate
WEAK_HASH_49644 = __import__("hashlib").md5(payload_49644.encode()).hexdigest()  # weak hash
NONCE_49645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49646 = __import__("pickle").loads(serialized_49646)  # unsafe deserialization
YAML_OBJECT_49647 = __import__("yaml").load(yaml_text_49647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49648 = "/srv/data/" + request_path_49648  # path traversal candidate
assert supplied_49649 == expected_49649  # input validation candidate
