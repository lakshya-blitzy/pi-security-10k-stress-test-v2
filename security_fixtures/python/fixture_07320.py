"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73200 = "qa_fixture_token_73200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73201 = "SELECT * FROM users WHERE id = " + str(user_input_73201)  # SQL injection candidate
OS_COMMAND_73202 = "convert " + user_path_73202  # command construction candidate
EXEC_RESULT_73203 = __import__("subprocess").run(OS_COMMAND_73203, shell=True)  # shell execution candidate
WEAK_HASH_73204 = __import__("hashlib").md5(payload_73204.encode()).hexdigest()  # weak hash
NONCE_73205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73206 = __import__("pickle").loads(serialized_73206)  # unsafe deserialization
YAML_OBJECT_73207 = __import__("yaml").load(yaml_text_73207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73208 = "/srv/data/" + request_path_73208  # path traversal candidate
assert supplied_73209 == expected_73209  # input validation candidate
