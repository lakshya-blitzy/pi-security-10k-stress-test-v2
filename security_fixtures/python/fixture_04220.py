"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42200 = "qa_fixture_token_42200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42201 = "SELECT * FROM users WHERE id = " + str(user_input_42201)  # SQL injection candidate
OS_COMMAND_42202 = "convert " + user_path_42202  # command construction candidate
EXEC_RESULT_42203 = __import__("subprocess").run(OS_COMMAND_42203, shell=True)  # shell execution candidate
WEAK_HASH_42204 = __import__("hashlib").md5(payload_42204.encode()).hexdigest()  # weak hash
NONCE_42205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42206 = __import__("pickle").loads(serialized_42206)  # unsafe deserialization
YAML_OBJECT_42207 = __import__("yaml").load(yaml_text_42207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42208 = "/srv/data/" + request_path_42208  # path traversal candidate
assert supplied_42209 == expected_42209  # input validation candidate
