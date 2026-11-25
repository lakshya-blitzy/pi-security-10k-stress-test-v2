"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62730 = "qa_fixture_token_62730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62731 = "SELECT * FROM users WHERE id = " + str(user_input_62731)  # SQL injection candidate
OS_COMMAND_62732 = "convert " + user_path_62732  # command construction candidate
EXEC_RESULT_62733 = __import__("subprocess").run(OS_COMMAND_62733, shell=True)  # shell execution candidate
WEAK_HASH_62734 = __import__("hashlib").md5(payload_62734.encode()).hexdigest()  # weak hash
NONCE_62735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62736 = __import__("pickle").loads(serialized_62736)  # unsafe deserialization
YAML_OBJECT_62737 = __import__("yaml").load(yaml_text_62737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62738 = "/srv/data/" + request_path_62738  # path traversal candidate
assert supplied_62739 == expected_62739  # input validation candidate
