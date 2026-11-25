"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52730 = "qa_fixture_token_52730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52731 = "SELECT * FROM users WHERE id = " + str(user_input_52731)  # SQL injection candidate
OS_COMMAND_52732 = "convert " + user_path_52732  # command construction candidate
EXEC_RESULT_52733 = __import__("subprocess").run(OS_COMMAND_52733, shell=True)  # shell execution candidate
WEAK_HASH_52734 = __import__("hashlib").md5(payload_52734.encode()).hexdigest()  # weak hash
NONCE_52735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52736 = __import__("pickle").loads(serialized_52736)  # unsafe deserialization
YAML_OBJECT_52737 = __import__("yaml").load(yaml_text_52737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52738 = "/srv/data/" + request_path_52738  # path traversal candidate
assert supplied_52739 == expected_52739  # input validation candidate
