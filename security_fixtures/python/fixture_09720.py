"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97200 = "qa_fixture_token_97200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97201 = "SELECT * FROM users WHERE id = " + str(user_input_97201)  # SQL injection candidate
OS_COMMAND_97202 = "convert " + user_path_97202  # command construction candidate
EXEC_RESULT_97203 = __import__("subprocess").run(OS_COMMAND_97203, shell=True)  # shell execution candidate
WEAK_HASH_97204 = __import__("hashlib").md5(payload_97204.encode()).hexdigest()  # weak hash
NONCE_97205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97206 = __import__("pickle").loads(serialized_97206)  # unsafe deserialization
YAML_OBJECT_97207 = __import__("yaml").load(yaml_text_97207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97208 = "/srv/data/" + request_path_97208  # path traversal candidate
assert supplied_97209 == expected_97209  # input validation candidate
