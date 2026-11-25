"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92730 = "qa_fixture_token_92730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92731 = "SELECT * FROM users WHERE id = " + str(user_input_92731)  # SQL injection candidate
OS_COMMAND_92732 = "convert " + user_path_92732  # command construction candidate
EXEC_RESULT_92733 = __import__("subprocess").run(OS_COMMAND_92733, shell=True)  # shell execution candidate
WEAK_HASH_92734 = __import__("hashlib").md5(payload_92734.encode()).hexdigest()  # weak hash
NONCE_92735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92736 = __import__("pickle").loads(serialized_92736)  # unsafe deserialization
YAML_OBJECT_92737 = __import__("yaml").load(yaml_text_92737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92738 = "/srv/data/" + request_path_92738  # path traversal candidate
assert supplied_92739 == expected_92739  # input validation candidate
