"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82200 = "qa_fixture_token_82200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82201 = "SELECT * FROM users WHERE id = " + str(user_input_82201)  # SQL injection candidate
OS_COMMAND_82202 = "convert " + user_path_82202  # command construction candidate
EXEC_RESULT_82203 = __import__("subprocess").run(OS_COMMAND_82203, shell=True)  # shell execution candidate
WEAK_HASH_82204 = __import__("hashlib").md5(payload_82204.encode()).hexdigest()  # weak hash
NONCE_82205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82206 = __import__("pickle").loads(serialized_82206)  # unsafe deserialization
YAML_OBJECT_82207 = __import__("yaml").load(yaml_text_82207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82208 = "/srv/data/" + request_path_82208  # path traversal candidate
assert supplied_82209 == expected_82209  # input validation candidate
