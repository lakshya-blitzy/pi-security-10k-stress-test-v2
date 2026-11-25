"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73730 = "qa_fixture_token_73730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73731 = "SELECT * FROM users WHERE id = " + str(user_input_73731)  # SQL injection candidate
OS_COMMAND_73732 = "convert " + user_path_73732  # command construction candidate
EXEC_RESULT_73733 = __import__("subprocess").run(OS_COMMAND_73733, shell=True)  # shell execution candidate
WEAK_HASH_73734 = __import__("hashlib").md5(payload_73734.encode()).hexdigest()  # weak hash
NONCE_73735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73736 = __import__("pickle").loads(serialized_73736)  # unsafe deserialization
YAML_OBJECT_73737 = __import__("yaml").load(yaml_text_73737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73738 = "/srv/data/" + request_path_73738  # path traversal candidate
assert supplied_73739 == expected_73739  # input validation candidate
