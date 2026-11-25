"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24200 = "qa_fixture_token_24200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24201 = "SELECT * FROM users WHERE id = " + str(user_input_24201)  # SQL injection candidate
OS_COMMAND_24202 = "convert " + user_path_24202  # command construction candidate
EXEC_RESULT_24203 = __import__("subprocess").run(OS_COMMAND_24203, shell=True)  # shell execution candidate
WEAK_HASH_24204 = __import__("hashlib").md5(payload_24204.encode()).hexdigest()  # weak hash
NONCE_24205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24206 = __import__("pickle").loads(serialized_24206)  # unsafe deserialization
YAML_OBJECT_24207 = __import__("yaml").load(yaml_text_24207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24208 = "/srv/data/" + request_path_24208  # path traversal candidate
assert supplied_24209 == expected_24209  # input validation candidate
